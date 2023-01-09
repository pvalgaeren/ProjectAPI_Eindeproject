import requests
import json

# Test GET
def test_get_all_movies():
    url = "http://localhost:8000/movies"
    response = requests.get(url)
    assert response.status_code == 200
    response_list = response.json()
    assert type(response_list) == list

def test_get_movie_by_id():
    url = "http://localhost:8000/movies/4"
    response = requests.get(url)
    assert response.status_code == 200
    response_dict = response.json()
    assert type(response_dict) == dict


def test_get_invalid_movie_id():
    url = "http://localhost:8000/movies/20"
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Movie with specified id not found.'}

def test_get_users_me():
    url = "http://localhost:8000/users/me"
    response = requests.get(url)
    assert response.status_code == 401
    assert "id" not in response.json()
    assert "email" not in response.json()
    assert "name" not in response.json()
    assert "token" not in response.json()
    assert "db" not in response.json()


# Test POST
def test_add_movie():
    url = "http://localhost:8000/movies/Avatar"
    movie = {
                "title": "Avatar: The Way of Water",
                "year": 2022,
                "genre": "scifi",
                "userID": 0
            }
    response = requests.post(url, json=movie)
    assert response.status_code == 200
    assert response.json()["title"] == "Avatar: The Way of Water"
    assert response.json()["year"] == 2022
    assert response.json()["genre"] == "scifi"
    assert response.json()["userID"] == 0

    # Test for movie with already existing title
    response = requests.post(url, json=movie)
    assert response.status_code == 200
    assert response.json()["title"] == "Avatar: The Way of Water"
    assert response.json()["year"] == 2022
    assert response.json()["genre"] == "scifi"
    assert response.json()["userID"] == 0


def test_create_user():
    url = "http://localhost:8000/users/"
    user_data = {
    "email": "janedoe@gmail.com",
    "password": "ABC123"
    }
    response = requests.post(url, json=user_data)
    assert response.status_code == 200
    assert response.json()["email"] == "janedoe@gmail.com"

    # Test for user with already existing email
    response = requests.post(url, json=user_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


# DELETE
def test_delete_movie_not_found():
    url = f"http://localhost:8000/movies/{2}"
    response = requests.delete(url)
    assert response.status_code == 404

