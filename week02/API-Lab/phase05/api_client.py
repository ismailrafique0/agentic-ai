import requests

def main():
    try:
        # Test timeout
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=10
        )
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print("Successful request")
        elif response.status_code == 404:
            print("Resource not found")
        elif response.status_code == 429:
            print("Rate limit exceeded")
        elif response.status_code >= 500:
            print("Server error")
        
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Network error")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    main()
