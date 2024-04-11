# API Documentation

Welcome to the API documentation for Blogs Web Application. This document provides comprehensive information about the endpoints available, their functionalities, request methods, request parameters, and response formats.


## Base URL

The base URL for all API endpoints is: http://localhost:8000/


## Authentication

Blogs Web Application API requires authentication for most endpoints. Authentication is achieved via __bearer tokens__. To obtain a token, users must register and authenticate using their credentials.


## Endpoints

### Users
---
__Register User__
* Endpoint: POST /users/register/
* Description: Register a new user.

__Request Body:__
```
{
    "username": "string",
    "password": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string"
}
```

__Response:__
* Status: 201 Created
* Content-Type: application/json
* Body
```
{
    "username": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string"
}
```

---

__Generate Access Token__
* Endpoint: POST /users/token/
* Description: Generate an access token for user authentication.
* Request Body:
```
{
    "username": "string",
    "password": "string"
}
```

__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body:
```
{
    "refresh": "string",
    "access": "string"
}
```
---

__Refresh Access Token__
* Endpoint: POST /users/token/refresh/
* Description: Refresh the access token.
* Request Body:
```
{
    "refresh": "string"
}
```

__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body:
```
{
    "access": "string"
}
```

---
__Change Password__
* Endpoint: PUT /users/change_password/{username}/
* Description: Change user password.
* Authorization: Bearer Token
* Request Body:
```
{
    "username": "string",
    "old_password": "string",
    "new_password": "string"
}
```
__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body:
```
{
    "message": "string",
    "details": "string",
    "status": 0
}
```
---
__Modify User Details__
* Endpoint: PUT /users/change_password/{username}/
* Description: Change user password.
* Authorization: Bearer Token
* Request Body:
```
{
    "username": "string",
    "first_name": "string",
    "last_name": "string"
}
```
__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body:
```
{
    "message": "string",
    "updated_details": {
        "username": "string",
        "first_name": "string",
        "last_name": "string",
        "email": "string"
    },
    "status": 0
}
```

---
### Blogs
__Create Post__
* Endpoint: POST /blogs/posts/
* Description: Create a new blog post.
* Authorization: Bearer Token
* Request Body:
```
{
    "title": "string",
    "content": "string"
}
```
__Response:__
* Status: 201 Created
* Content-Type: application/json
* Body:
```
{
    "post_id": "int",
    "title": "string",
    "author": "string",
    "content": "string",
    "published_on": "string",
    "modified_on": "string"
}
```
---
__Retrieve Posts__
* Endpoint: GET /blogs/posts/
* Description: Retrieve a list of blog posts.
* Authorization: Bearer Token
* Query Parameters:
    * page (optional): Page number for pagination (default: 1)
    * limit (optional): Number of posts per page (default: 10)

__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body:
```
{
    "count": "int",
    "next": "string",
    "previous": "string",
    "results": [
        {
            "post_id": "int",
            "title": "string",
            "author": "string",
            "content": "string",
            "published_on": "string",
            "modified_on": "string"
        }
    ]
}
```
---
__Retrieve Single Post__
* Endpoint: GET /blogs/posts/{post_id}/
* Description: Retrieve a single blog post by its ID.
* Authorization: Bearer Token

__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body:
```
{
    "post_id": "int",
    "title": "string",
    "author": "string",
    "content": "string",
    "published_on": "string",
    "modified_on": "string"
}
```
---
__Update Post__
* Endpoint: PUT /blogs/posts/{post_id}/
* Description: Update an existing blog post by its ID.
* Authorization: Bearer Token
* Request Body:
```
{
    "title": "string",
    "content": "string"
}
```
__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body:
```
{
    "post_id": "int",
    "title": "string",
    "author": "string",
    "content": "string",
    "published_on": "string",
    "modified_on": "string"
}
```
__Delete Post__
* Endpoint: DELETE /blogs/posts/{post_id}/
* Description: Delete a blog post by its ID.
* Authorization: Bearer Token

__Response:__
* Status: 200 OK

---

### Comments
__Add Comment__
* Endpoint: POST /blogs/comments/
* Description: Add a comment to a blog post.
* Authorization: Bearer Token
* Request Body:
```
{
    "comment": "string",
    "post_id": "int"
}
```
* Authorization: Bearer Token

__Response:__
* Status: 201 Created
* Content-Type: application/json
* Body:
```
{
    "comment_id": 0,
    "post_id": 0,
    "user_id": "",
    "comment": "",
    "published_on": "",
    "modified_on": ""
}
```
---
__Retrieve Comments__
* Endpoint: GET /blogs/comments/
* Description: Retrieve comments for blogs.
* Authorization: Bearer Token

__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body: Response body contains details of each comment.
---
__Delete Post__
* Endpoint: DELETE /blogs/comments/7/
* Description: Delete a specific comment on a blog.
* Authorization: Bearer Token

__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body:
```
{
    "status": 0,
    "message": ""
}
```
---
__Modify Comment__
* Endpoint: PUT /blogs/comments/7/
* Description: Update a comment on a specific blog post.
* Request Body:
```
{
    "comment": "string",
    "post_id": "int"
}
```
* Authorization: Bearer Token

__Response:__
* Status: 200 OK
* Content-Type: application/json
* Body: Response body contains updated comment details.

---


### Errors
In case of errors, the API will return appropriate HTTP status codes along with error messages in the response body.



For using API collection, import the collection json file in Postman.