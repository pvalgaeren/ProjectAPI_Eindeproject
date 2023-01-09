from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, unique=True)
    hashed_password = Column(String)

    movies = relationship("Movie", back_populates="users")


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer, index=True)
    genre = Column(String, index=True)
    userID = Column(Integer, ForeignKey("users.id"), index=True)

    users = relationship("User", back_populates="movies")