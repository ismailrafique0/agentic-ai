# Phase 06 - From API Integration to Agent Tools

**Selected Operation:** Retrieve a specific post by ID (GET /posts/{id})

**Tool Specification:**

| Field | Value |
|-------|-------|
| Tool Name | `get_post` |
| Description | Retrieve a specific blog post by its ID from JSONPlaceholder API |
| HTTP Method | GET |
| Endpoint | `https://jsonplaceholder.typicode.com/posts/{post_id}` |
| Required Inputs | `post_id` (integer) |
| Optional Inputs | None |
| Expected Output | JSON object with id, userId, title, body |
| Possible Errors | 404 (Not Found), 429 (Rate Limited), 500 (Server Error), Timeout, Network Error |
| Authentication Required | No (for JSONPlaceholder) |

## Task 25: Design an Agent Tool Interface

**Agent-Oriented Tool Definition:**

```json
{
  "name": "get_post",
  "description": "Retrieve a post using its ID",
  "input_schema": {
    "type": "object",
    "properties": {
      "post_id": {
        "type": "integer",
        "description": "The ID of the post to retrieve"
      }
    },
    "required": ["post_id"]
  },
  "output": {
    "type": "object",
    "properties": {
      "id": {"type": "integer"},
      "title": {"type": "string"},
      "body": {"type": "string"},
      "userId": {"type": "integer"}
    }
  },
  "possible_errors": ["404", "429", "500", "Timeout"]
}
```

**Purpose:** This API operation can be represented as an agent tool, allowing an AI agent to autonomously fetch post data when needed without manually writing HTTP requests.
