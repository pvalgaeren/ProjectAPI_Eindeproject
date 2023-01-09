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


## Postman
### GET
/movies:

![image](https://user-images.githubusercontent.com/91118410/211191125-51bf8720-45d0-44bd-9af2-b46cccc6ce68.png)

/movies/{movie_id}:

![image](https://user-images.githubusercontent.com/91118410/211193027-c2fa014d-1e36-42ad-ab35-9ef876ed1203.png)

/users/me:
![image](https://user-images.githubusercontent.com/91118410/211207345-cb685fb7-686a-4a05-b76d-b2a192ae9d63.png)


### POST

/movies/{title}:

![image](https://user-images.githubusercontent.com/91118410/211191060-3456e164-b00e-4c56-91a1-1c76ce5f633a.png)

/users: 

![image](https://user-images.githubusercontent.com/91118410/211207239-a9c2bd60-890f-4d4f-8135-2473830ba872.png)


### PUT
/movies/{title}:

![image](https://user-images.githubusercontent.com/91118410/211207435-ecfe260d-d398-4a13-84a3-08a17b96360b.png)

### DELETE
/movies/{movie_id}:

![image](https://user-images.githubusercontent.com/91118410/211193084-dba833ec-6a2a-4ca1-8470-e5e2eb53a745.png)


## OpenAI docs
### GET
/movies:

![image](https://user-images.githubusercontent.com/91118410/211191571-95c052c4-57bc-47be-bb63-fa45a0c71635.png)
![image](https://user-images.githubusercontent.com/91118410/211191580-2e656fd4-78e1-4147-a63c-3f8d3f1f30d1.png)

/movies/{movie_id}:

![image](https://user-images.githubusercontent.com/91118410/211191439-7527e690-8db1-44ea-8e07-a776e7e03885.png)
![image](https://user-images.githubusercontent.com/91118410/211191458-c0cff774-5f94-43df-91b9-e61b34d8fb44.png)

/movies/search:

![image](https://user-images.githubusercontent.com/91118410/211198745-2cedf05b-b632-44ba-a87a-a48d1cd54dc6.png)
![image](https://user-images.githubusercontent.com/91118410/211198760-1f09d9de-af8c-4c9f-a58f-5ad2619758c9.png)


### POST
/token:

![image](https://user-images.githubusercontent.com/91118410/211206839-6f5ec6f3-200c-4d8c-9b26-d282f0bf2a5d.png)
![image](https://user-images.githubusercontent.com/91118410/211206858-b23862f8-e00a-4dde-91e6-7be7a01c2f64.png)
![image](https://user-images.githubusercontent.com/91118410/211206868-b3baf46b-d1ae-4d29-a742-3175158ac9fb.png)


/movies/{title}:

![image](https://user-images.githubusercontent.com/91118410/211191521-612354c7-8a0b-4d3b-89a7-e5f15aa47db6.png)
![image](https://user-images.githubusercontent.com/91118410/211191536-d2661ba6-abee-4a56-b1b3-89dd1bd98b2a.png)

/users:

![image](https://user-images.githubusercontent.com/91118410/211205652-f5119e3b-ccfc-4641-ba05-e8eb478baa86.png)
![image](https://user-images.githubusercontent.com/91118410/211205664-020b01a9-ff63-436c-8cea-b4b92f9b53cc.png)


### PUT
/movies/{title}:
![image](https://user-images.githubusercontent.com/91118410/211200729-909e063f-10c8-4380-b3a5-a4ef0cda283b.png)
![image](https://user-images.githubusercontent.com/91118410/211200746-e426e78a-68e8-47cc-bd50-8c8e6593e84d.png)


### DELETE
/movies/{movie_id}:

![image](https://user-images.githubusercontent.com/91118410/211192745-0a7eb69a-8894-4e95-9ee1-321c6b94407b.png)
![image](https://user-images.githubusercontent.com/91118410/211192761-63d9a007-0ab8-4aff-b6ae-fe8c1f16c0be.png)

## Authorization
![image](https://user-images.githubusercontent.com/91118410/211206171-e3ef45ff-2b09-495d-821a-06efc2800189.png)


## Testing

### GET

/movies:
![image](https://user-images.githubusercontent.com/91118410/211200115-6fa08680-ca66-432f-9a48-a3871039e980.png)


/movies/{movie_id}:

![image](https://user-images.githubusercontent.com/91118410/211200419-f09b5ae8-5a97-4337-bae5-d5415db14833.png)
![image](https://user-images.githubusercontent.com/91118410/211202513-1d29d167-d9cb-4ba5-bfdb-eedb64f06791.png)

/users/me:

![image](https://user-images.githubusercontent.com/91118410/211214166-bf58b18c-de33-4a91-847f-1aca66bec2a4.png)

### POST

/movies/{title}:

![image](https://user-images.githubusercontent.com/91118410/211214719-75fc6783-d1b7-4375-9b42-d632c676a2f0.png)

## Links
Okteto: https://github.com/pvalgaeren/ProjectAPI_Eindeproject.git
