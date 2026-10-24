import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Post ID: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")

if __name__ == "__main__":
    main()
