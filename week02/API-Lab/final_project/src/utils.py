import os
import json
from typing import Dict, Any, Optional

def load_config():
    """Load configuration from environment variables."""
    from dotenv import load_dotenv
    load_dotenv()
    
    return {
        "api_key": os.getenv("API_KEY", ""),
        "base_url": os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com"),
        "timeout": int(os.getenv("TIMEOUT", "10"))
    }

def print_response_info(response, operation: str):
    """Print response information."""
    print(f"\n{'='*50}")
    print(f"Operation: {operation}")
    print(f"{'='*50}")
    print(f"Status Code: {response.status_code}")
    print(f"URL: {response.url}")
    print(f"{'='*50}")

def handle_errors(response) -> bool:
    """Handle different HTTP status codes. Returns True if successful."""
    status = response.status_code
    
    if 200 <= status < 300:
        print("✓ Request Successful")
        return True
    elif status == 400:
        print("✗ Bad Request (400) - Invalid request format")
        return False
    elif status == 401:
        print("✗ Unauthorized (401) - Authentication failed or missing")
        return False
    elif status == 404:
        print("✗ Not Found (404) - Resource does not exist")
        return False
    elif status == 429:
        print("✗ Too Many Requests (429) - Rate limit exceeded")
        return False
    elif 500 <= status < 600:
        print(f"✗ Server Error ({status}) - Internal server error")
        return False
    else:
        print(f"✗ Unexpected Status Code: {status}")
        return False
