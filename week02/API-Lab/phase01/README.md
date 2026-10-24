# Phase 01 - API & Client-Server Fundamentals

## Task 01: Explore an API Using a Browser
**URL:** https://jsonplaceholder.typicode.com/posts/1

**Returned JSON fields:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

**Values recorded:**
- userId: 1
- id: 1
- title: "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
- body: "quia et suscipit..."

**Testing other posts:**
- /posts/2: Returns different post with id: 2
- /posts/3: Returns different post with id: 3

**Explanation:** The response changes because the resource identifier in the URL path (/1, /2, /3) tells the server which specific post to retrieve. Each ID maps to a different record in the database.

**Evidence:** Screenshots of /posts/1, /posts/2, /posts/3

## Task 02: Identify the Client, API and Server

**Diagram:**
```
Browser (Client) → API (REST Endpoint) → Server (JSONPlaceholder) → Response (JSON)
```

**Components:**
- **Browser (Client):** Initiates the request by entering the URL
- **API:** The interface/endpoint that accepts HTTP requests
- **Server:** Processes request, retrieves data from database
- **Response:** Returns JSON data to the client

**Explanation:** When requesting /posts/1, the browser sends an HTTP GET request to the server. The API routes this to the posts resource handler, the server queries for post with id=1, and returns a JSON response with status 200. The browser receives and displays this response.

## Task 03: Identify API Resources

| Endpoint | Resource | Specific Resource? |
|----------|----------|-------------------|
| /posts | Collection of all posts | No - returns array of all post resources |
| /posts/1 | Post resource with ID 1 | Yes - returns a single specific post |
| /posts/2 | Post resource with ID 2 | Yes - returns a single specific post |
