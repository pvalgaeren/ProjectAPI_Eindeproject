# Movie API

## Chosen theme
For this API I have chosen the theme of movies, this is because I myself love watching movies.
In my spare time, I like to watch movies at home. My personal preference is usually scifi movies, but in this api I chose to list more genres. 
I found my information about the movies on the Internet. 
Everyone has had the problem of wanting to watch a movie but not knowing which one. 
Therefore, this api returns a list of movies so that you can choose easily. 

I got the information about writing this movie api from the course "API development" and the Internet. My basic knowledge also helped me a bit in writing these codes, since I myself am not very good at this I deliberately chose easy codes. 

## Endpoints
### GET
- /movies: This endpoint allows you to retrieve a list of all movies. It does not accept any parameters and returns a list of all movies in the database.

- /movies/{movie_id}: This endpoint allows you to retrieve a movie by its id. It accepts a movie id as a path parameter and returns the movie with the specified id. If a movie with the specified id is not found, it returns a 404 error.

- /users/me: This endpoint is accessed via an HTTP GET request to the "/users/me" route. The endpoint returns a response that is based on the "schemas.User" model, which likely contains information about a user. The endpoint also has two dependencies: a database session (provided by the "get_db" function) and an OAuth2 token (provided by the "oauth2_scheme" function). The endpoint retrieves the current active user from the database using the "auth.get_current_active_user" function, and returns this user as the response.

### POST
- /token: This endpoint is used to authenticate a user and get an access token. It requires a username and password in the request body. If the provided credentials are correct, it returns a JSON object with an access_token and token_type (which is always "bearer"). If the credentials are incorrect, it returns a 401 status code with an error message.

- /movies/{title}: This endpoint is used to add a new movie to the database. It requires a title in the URL path and a MovieCreate object in the request body. If a movie with the same title already exists in the database, it returns a 409 status code with an error message. Otherwise, it returns the new movie object.

- /users/: This endpoint that allows users to create a new account by providing their email address and other required information. The endpoint is accessed via a POST request to the "/users/" route and expects a request body that is modeled by the "schemas.UserCreate" class. The function will check if the provided email is already registered in the database and return a 400 error if it is. If the email is not registered, it will create a new user account in the database using the provided information and return the resulting user object, which is modeled by the "schemas.User" class. The function also depends on a database session, which is provided by the "get_db" function.

### PUT
- /movies/{title}: This endpoint allows you to update an existing movie in the database. It accepts a title parameter in the URL path and a schemas.MovieUpdate object in the request body, and returns a schemas.MovieBase object with the updated movie information. To use this endpoint, send a PUT request to /movies/{title} with the title of the movie you want to update and the updates you want to make in the request body. If the movie with the specified title does not exist, it will return a 404 error.

### DELETE
- /movies/{movie_id}: This endpoint allows you to delete a movie from the database by specifying the movie's ID. If the movie is successfully deleted, the endpoint will return the deleted movie object. If the movie with the specified ID is not found, the endpoint will return a 404 error.
