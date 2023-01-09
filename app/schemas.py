from pydantic import BaseModel

# Movie models
class MovieBase(BaseModel):
    title: str
    year: int
    genre: str
    userID: int = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    movieID: int = None
    class Config:
        orm_mode = True

class MovieUpdate(BaseModel):
    title: str = None
    year: int = None
    genre: str = None
    userID: int = None


# User models
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    movies: list[Movie] = []

    class Config:
        orm_mode = True