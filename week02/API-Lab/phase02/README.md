# Phase 02 - HTTP Requests, Responses & REST

## Task 04: Analyze a URL

**URL:** https://api.example.com/students/101

| Component | Value |
|-----------|-------|
| Protocol | https |
| Host | api.example.com |
| Path | /students/101 |
| Resource | students |
| Resource identifier | 101 |

## Task 05: Build a REST API Operation Table

| Operation | HTTP Method | Endpoint |
|-----------|-------------|----------|
| Retrieve all students | GET | /students |
| Create a student | POST | /students |
| Retrieve student 101 | GET | /students/101 |
| Update student 101 | PUT | /students/101 |
| Delete student 101 | DELETE | /students/101 |

**Explanation:** Different HTTP methods are used because they represent different operations on resources. GET retrieves data, POST creates new resources, PUT/PATCH updates existing resources, and DELETE removes resources. This follows REST conventions where the method defines the action.

## Task 06: Test GET Requests

| Endpoint | HTTP method | Status code | Response body |
|----------|-------------|-------------|---------------|
| /posts/1 | GET | 200 OK | {"userId": 1, "id": 1, "title": "...", "body": "..."} |
| /posts/2 | GET | 200 OK | {"userId": 1, "id": 2, "title": "...", "body": "..."} |
| /posts/3 | GET | 200 OK | {"userId": 1, "id": 3, "title": "...", "body": "..."} |

**Evidence:** Three successful API requests with status codes and response data

## Task 07: Test POST

- HTTP method: POST
- Endpoint: https://jsonplaceholder.typicode.com/posts
- Request body: `{"title": "My API Lab", "body": "Testing POST request", "userId": 1}`
- Response status code: 201 Created
- Response body: `{"title": "My API Lab", "body": "Testing POST request", "userId": 1, "id": 101}`

## Task 08: Test PUT

- Request method: PUT
- Endpoint: https://jsonplaceholder.typicode.com/posts/1
- Request body: `{"id": 1, "title": "Updated Title", "body": "Updated body content", "userId": 1}`
- Status code: 200 OK
- Response: `{"id": 1, "title": "Updated Title", "body": "Updated body content", "userId": 1}`

## Task 09: Test DELETE

- Request method: DELETE
- Endpoint: https://jsonplaceholder.typicode.com/posts/1
- Status code: 200 OK
- Response: `{}`

**Explanation:** DELETE removes the specified resource from the server. It is intended to permanently delete the resource identified by the URI.

## Task 10: Investigate HTTP Status Codes

| Status Code | Meaning | Your Test |
|-------------|---------|-----------|
| 200 | OK - Request succeeded | GET /posts/1 returned post successfully |
| 201 | Created - Resource successfully created | POST /posts created new resource with id 101 |
| 404 | Not Found - Resource doesn't exist | GET /posts/99999 returns not found/error |

**Difference:** A successful request (2xx) means the server fulfilled the valid request. A 404 means the request was valid but the server cannot find the requested resource at that URI.
