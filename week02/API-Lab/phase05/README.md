# Phase 05 - Errors, Timeouts & Rate Limits

## Task 19: Handle a 404 Error

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/99999"
try:
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        print("Request failed.")
        print(f"Status Code: {response.status_code}")
        print("Resource not found.")
    elif response.status_code == 200:
        print(response.json())
    else:
        print(f"Status: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
```

**Expected behavior:** Request failed. Status Code: 404. Resource not found.

## Task 20: Handle Multiple HTTP Errors

```python
if response.status_code == 200:
    print("Success")
elif response.status_code == 400:
    print("Bad Request - Invalid syntax")
elif response.status_code == 401:
    print("Unauthorized - Authentication required")
elif response.status_code == 404:
    print("Not Found - Resource doesn't exist")
elif response.status_code == 429:
    print("Too Many Requests - Rate limit exceeded")
elif response.status_code >= 500:
    print("Server Error - Try again later")
```

## Task 21: Add Request Timeout

```python
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
    print(response.status_code)
except requests.exceptions.Timeout:
    print("Request timed out")
```

**Why timeout is necessary:** Prevents the program from hanging indefinitely if the server is slow or unresponsive. It ensures graceful failure and better user experience.

## Task 22: Handle Network/API Failure

```python
import requests

try:
    response = requests.get(url, timeout=10)
    if response.ok:
        print("Successful request")
    else:
        print(f"API error: {response.status_code}")
except requests.exceptions.Timeout:
    print("Timeout")
except requests.exceptions.ConnectionError:
    print("Network/request failure")
except Exception as e:
    print(f"Error: {e}")
```

## Task 23: Investigate Rate Limiting

**What is a rate limit?** A restriction on the number of API requests a client can make within a time period.

**Why do APIs impose rate limits?** To prevent abuse, ensure fair usage, protect server resources, and maintain service stability.

**What does HTTP 429 mean?** "Too Many Requests" - the client has sent too many requests in a given time window.

**Why can automated programs generate too many requests?** Loops, scripts, or bots can make rapid requests without human delays.

**Why is this important for agentic systems?** Agentic AI systems can autonomously make many API calls; without rate limit awareness, they can get blocked, incur costs, or cause service disruptions. Implementing rate limiting/backoff is critical.
