<h1 align="center">
  API Mobile Aptitude Test - Documentation
</h1>

<h2 align="center">
  Information
</h2>
<p align="center">
    This documentation has been created to guide mobile developers about the Aptitude Test API endpoints.
</p>

<div style="width:  60%; margin: auto;">
  <hr style="border: none; height:  1px; background-color: gray;">
</div>

### URL bases

**Production:** *https://apitestemobile-production.up.railway.app*  

<hr style="border: none; height:  1px; background-color: gray;">

### `POST` _Login (Token)_

>The endpoint functions by validating credentials and generating access token, enabling the utilization of other endpoints.

<!-- **Method:** **<span style="color:#87bdd8">POST</span>**   -->
**Endpoint:** /login  
**Content-Type:** JSON  

**Request Body Types:**

`username: String (Required)`  
`password: String (Required)`

**Request Body Example:**

```json
{
    "username": "example",
    "password": "example"
}
```

**Response Example - 200:**

`POST - /api/login`

```json
{
	"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNzA0MjY1LCJpYXQiOjE3MDM3MDM5NjUsImp0aSI6IjdmOTZjZDExMzc4MDQzZDY5ZmRkZDgxYjliMjRmNDFhIiwidXNlcl9pZCI6MjEyfQnXPYekgNFsRSUdMrw3giB7pF21-KA5iOsTIHkxP5NLM"
}
```

<hr style="border: none; height:  1px; background-color: gray;">

### `GET` _Retrieve Tree Data_

>This endpoint is utilized to retrieve the tree contents.

<!-- **Method:** **<span style="color:green">GET</span>**     -->
**Endpoint:** /tree  
**Authentication:** Bearer: Access Token  

**Response Example - 200:**

`GET - /tree`

```json
[
    {
        "id": 1,
        "name": "AREA 1",
        "level": 0,
        "parent": null
    },
    {
        "id": 2,
        "name": "AREA 2",
        "level": 0,
        "parent": null
    },
	...
]
```

**Some examples of error responses:**

`GET - /tree`

* 401 - Unauthorized

```json
{
	"msg": "Missing Authorization Header"
}
```

<hr style="border: none; height:  1px; background-color: gray;">

### `POST` _Updated Tree Node Data_

>This endpoint is designed to update the tree node information.

<!-- **Method:** **<span style="color:blue">POST</span>**      -->
**Endpoint:** /tree  
**Authentication:** Bearer: Access Token  
**Content-Type:** JSON    

**Request Body Example:**

`id: Integer (Required)`  
`name: String (Required)`

**Request Body Example:**

```json
{
    "id": 1,
    "password": "New Area"
}
```

**Response Example - 200:**

`POST - /tree`

```json
  {
	"msg": "Node updated successfully."
  }
```
**Response Error Example:**

`POST - /tree`

* 401 - Unauthorized

```json
{
	"msg": "Missing Authorization Header"
}
```

`POST - /tree`

* 400 - Bad Request

```json
{
	"msg": "Missing Parameters."
}
```

<hr style="border: none; height:  1px; background-color: gray;">

<div style="width:  60%; margin: auto;">
  <hr style="border: none; height:  1px; background-color: gray;">
  <p align="center">
    Copyright @Semeq - All rights reserved
  </p>
</div>