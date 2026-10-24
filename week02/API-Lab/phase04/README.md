# Phase 04 - Authentication, API Keys & Secure Configuration

## Task 16: Public vs Protected API

| Aspect | Public API | Protected API |
|--------|------------|---------------|
| Credentials Required | No | Yes (API key, token, OAuth) |
| Why Authentication Used | N/A | To control access, rate limit, track usage, secure data |
| Example Auth Mechanism | Open access | Authorization: Bearer TOKEN or API Key header |
| Invalid Credentials | N/A or no restriction | Returns 401 Unauthorized |

## Task 17: Implement an Authorization Header

```python
import requests

url = "https://api.example.com/protected/resource"
headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE",
    "Content-Type": "application/json"
}

# Print sanitized configuration
print("Request Headers (sanitized):")
for key, value in headers.items():
    if "Authorization" in key:
        print(f"  {key}: Bearer ***")
    else:
        print(f"  {key}: {value}")

# response = requests.get(url, headers=headers)
```

## Task 18: Move Credentials to .env

**.env file:**
```env
API_KEY=your_key_here
```

**Python code:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}
```

**Requirements met:**
- ✓ Created .env
- ✓ Stored API key in .env
- ✓ Loaded using os.getenv()
- ✓ Not hardcoded in source
- ✓ Added .env to .gitignore
- ✓ Credential excluded from version control

**Important:** Never submit real API keys to repositories.
