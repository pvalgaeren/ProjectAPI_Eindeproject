from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta

import auth
import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

data_tags = [
    {
        "name": "movie id",
        "description": "Allows you to retrieve a specific movie by its id."
    },
    {
        "name": "movie list",
        "description": "Returns a list of all movies."
    },
    {
        "name": "log in",
        "description": "This endpoint defines a route that retrieves the current user's information and returns it as a response."
    },
    {
        "name": "OAuth2",
        "description": "This endpoint will be automatically called by the OpenAPI docs Authorize interface. After a successful login it will also place the JWT in the header of each following request"
    },
    {
        "name": "add movie",
        "description": "You can add a new movie to the list."
    },
    {
        "name": "movie update",
        "description": "Allows you to update an movie by sending a PUT request with a JSON payload containing the updated movie data."
    },
    {
        "name": "movie delete",
        "description": "Allows you to delete a movie by giving the id of this movie."
    }

]

app = FastAPI(openapi_tags=data_tags,
    title="Movie generator",
    description="This API is a movieAPI, it helps you to choose a movie.",
    contact={
        "naam": "Pauline Valgaeren",
        "email": "r0781850@student.thomasmore.be",
        "klas": "2CCS1"
    })

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# GET requests
@app.get("/movies", tags=["movie list"])
def get_all_movies(db: Session = Depends(get_db)):
    movies = crud.get_movies(db)
    return movies

@app.get("/movies/{movie_id}", tags=["movie id"])
def get_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id=movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with specified id not found.")
    return movie

@app.get("/users/me", response_model=schemas.User, tags=["log in"])
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user


# POST requests
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/movies/{title}", tags=["add movie"])
def add_movie(title: str, movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_name(db, name=title)
    if title in db_movie:
        raise HTTPException(status_code=409, detail="Movie with that title already exists.")
    new_movie = crud.create_movie(db, movie=movie)
    return new_movie

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# PUT request
@app.put("/movies/{title}", response_model=schemas.MovieBase, tags=["movie update"])
def update_movie(title: str, updates: schemas.MovieUpdate, db: Session = Depends(get_db)):
    movie_you_want_to_update = crud.get_movie_by_name(db, name=title)
    if movie_you_want_to_update not in db:
        raise HTTPException(status_code=404, detail="The movie you are trying to find is not listed")
    return crud.update_movieList(movie=movie_you_want_to_update, updates=updates, db=db)



# DELETE request
@app.delete("/movies/{movie_id}", response_model=schemas.Movie, tags=["movie delete"])
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie_you_want_to_delete = crud.delete_movie(db=db, movie_id=movie_id)
    if not movie_you_want_to_delete:
        raise HTTPException(status_code=404, detail="The movie you are trying to find is not listed")
    return movie_you_want_to_delete
