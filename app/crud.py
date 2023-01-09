import models
import schemas
import auth
from sqlalchemy.orm import Session


# CREATE

# More information about the function create_movie(db, movie: schemas.MovieCreate)

# This function creates a new movie in the database.
# It takes a db parameter which is a database session and an album parameter which is an object of type schemas.MovieCreate.
# The function first creates a models.Movie object from the album object by expanding
# the dictionary representation of album using the ** operator.
# It then adds the movie_database object to the db session using the add method.
# The changes are then committed to the database using the commit method.
# Finally, the refresh method is called on the movie_database object to refresh its state with the state of the object
# in the database. The refreshed movie_database object is then returned.
def create_movie(db: Session, movie: schemas.MovieCreate):
    movie_database = models.Movie(**movie.dict())
    db.add(movie_database)
    db.commit()
    db.refresh(movie_database)
    return movie_database


# More information about the function create_user(db, user: schemas.UserCreate)

# This code creates a user in the database using the provided user object, which should contain an email and a password.
# The password is hashed using the auth.get_password_hash function,
# and the resulting hashed_password is used to create a db_user object, which is then added to the database.
# The function then commits the changes to the database and refreshes the db_user object before returning it.
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



# READ

# More information about the function get_movie(db, movie_id: int)

# This is a function definition in Python that queries a database using the query method of an object called db.
# It filters the results of the query by the id field of the Movie model, and returns the first result of the filtered query.
#
# The db object is expected to be an instance of a class that has a query method which can be used to execute a query and return the results.
# The query method is typically used to specify which model or models to query and any filters to apply to the query.
#
# The filter method is used to specify the conditions that should be used to filter the results of the query.
# In this case, the condition is that the id field of the Movie model should be equal to the value of the movie_id argument passed to the get_movie function.
#
# Finally, the first method is called on the filtered query to return the first result of the query. If there are no results, None will be returned.
def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


# More information about the function get_movie_by_name(db, name:str)

# This code defines a function called "get_movie_by_name" which takes in two arguments: a database object and a string representing the name of a movie.
# The function queries the database for a movie with the specified title and returns the result of the query.
def get_movie_by_name(db: Session, name: str):
    return db.query(models.Movie).filter(models.Movie.title == name)


# More information about the function get_movie_by_genre(db, genre: str)

# This code is a function that takes in a database (db) and a string (genre) as arguments and returns a query
# of all movies in the database that have a genre matching the provided genre string.
# It does this by using the query function on the Movie model from the models module,
# and filtering the results by using the filter function with a condition that the genre of the movie must equal the provided genre string.
def get_movie_by_genre(db: Session, genre: str):
    return db.query(models.Movie).filter(models.Movie.genre == genre)


# More information about the function get_movies(db):

# This code defines a function called "get_movies" that takes in a database (represented by the variable "db") as an argument.
# The function returns a list of all movies in the database by querying the "Movie" model and calling the "all" function on the result.
def get_movies(db: Session):
    return db.query(models.Movie).all()


# More information about the function get_user_by_email(db: Session, email: str)

# This code defines a function get_user_by_email that takes two arguments:
# db, a Session object from the sqlalchemy.orm module, represents a session with the database
# email, a string, represents the email of the user being searched for
# The function queries the User table of the database to find the first user with a matching email.
# If a matching user is found, the user object is returned. If no matching user is found, None is returned.
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()



# UPDATE

# More information about the function update_movieList(db, movie: schemas.Movie, updates: schemas.MovieUpdate)

# This code defines a function called "update_movieList" that takes in three arguments: "db", "movie", and "updates".
# The function first loops through the items in the "updates" object, using the "setattr" function to set the attributes of the "movie" object
# to the corresponding values in the "updates" object. It then adds the updated "movie" object to the database specified by "db",
# commits the changes to the database, refreshes the "movie" object with the updated version from the database, and returns the updated "movie" object.
def update_movieList(db: Session, movie: schemas.Movie, updates: schemas.MovieUpdate):
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(movie, field, value)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie



# DELETE

# More information about the function delete_movie(db, movie_id: int)

# This code is a function that deletes a movie from a database.
# The function takes two arguments: a database object and a movie ID (an integer).
# The function first searches the database for the movie with the specified ID and stores it in a variable called "movie".
# If no movie is found, the function returns None. If a movie is found, the function deletes the movie from the database and commits the change.
# Finally, the function returns the deleted movie.
def delete_movie(db, movie_id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        return None
    db.delete(movie)
    db.commit()
    return movie
