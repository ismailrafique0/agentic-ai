import os
import requests
from dotenv import load_dotenv

load_dotenv()

def main():
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    
    headers = {
        "Authorization": f"Bearer {api_key}" if api_key and api_key != "your_key_here" else None,
        "Content-Type": "application/json"
    }
    
    print("Request Headers (sanitized):")
    for k, v in headers.items():
        if k == "Authorization" and v:
            print(f"  {k}: Bearer ***")
        else:
            print(f"  {k}: {v}")
    
    # Example request
    url = f"{base_url}/posts/1"
    req_headers = {k: v for k, v in headers.items() if v is not None}
    response = requests.get(url, headers=req_headers, timeout=10)
    print(f"\nStatus: {response.status_code}")

if __name__ == "__main__":
    main()
