#!/usr/bin/env python3
"""
Complete API Client - Week 02 Final Project
Demonstrates: API communication, HTTP methods, JSON processing,
authentication, error handling, timeouts, and rate limiting
"""

import requests
import sys
from utils import load_config, print_response_info, handle_errors

class APIClient:
    def __init__(self):
        self.config = load_config()
        self.base_url = self.config["base_url"]
        self.timeout = self.config["timeout"]
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "API-Lab-Client/1.0"
        }
        # Add authentication if API key exists
        if self.config["api_key"] and self.config["api_key"] != "your_api_key_here":
            self.headers["Authorization"] = f"Bearer {self.config['api_key']}"
    
    def get_all_posts(self):
        """GET - Retrieve all posts"""
        try:
            url = f"{self.base_url}/posts"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            print_response_info(response, "GET /posts (Retrieve All)")
            
            if handle_errors(response):
                posts = response.json()
                print(f"\nTotal posts retrieved: {len(posts)}")
                print("\nFirst 5 post titles:")
                for i, post in enumerate(posts[:5], 1):
                    print(f"  {i}. {post['title'][:60]}...")
                return posts
        except requests.exceptions.Timeout:
            print(f"\n✗ Timeout Error: Request exceeded {self.timeout} seconds")
        except requests.exceptions.ConnectionError:
            print("\n✗ Network Error: Failed to connect to API")
        except requests.exceptions.RequestException as e:
            print(f"\n✗ Request Error: {e}")
        return None
    
    def get_post(self, post_id):
        """GET - Retrieve specific post"""
        try:
            url = f"{self.base_url}/posts/{post_id}"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            print_response_info(response, f"GET /posts/{post_id}")
            
            if handle_errors(response):
                post = response.json()
                print(f"\nPost Details:")
                print(f"  ID: {post['id']}")
                print(f"  User ID: {post['userId']}")
                print(f"  Title: {post['title']}")
                print(f"  Body: {post['body'][:100]}...")
                return post
        except requests.exceptions.Timeout:
            print(f"\n✗ Timeout Error: Request exceeded {self.timeout} seconds")
        except requests.exceptions.ConnectionError:
            print("\n✗ Network Error: Failed to connect to API")
        except requests.exceptions.RequestException as e:
            print(f"\n✗ Request Error: {e}")
        return None
    
    def create_post(self):
        """POST - Create new post"""
        try:
            url = f"{self.base_url}/posts"
            data = {
                "title": "My API Lab",
                "body": "Testing POST request",
                "userId": 1
            }
            response = requests.post(url, headers=self.headers, json=data, timeout=self.timeout)
            print_response_info(response, "POST /posts (Create)")
            print(f"\nRequest Body:\n{data}")
            
            if handle_errors(response):
                created = response.json()
                print(f"\nCreated Post:")
                print(f"  ID: {created['id']}")
                print(f"  Title: {created['title']}")
                return created
        except requests.exceptions.Timeout:
            print(f"\n✗ Timeout Error: Request exceeded {self.timeout} seconds")
        except requests.exceptions.ConnectionError:
            print("\n✗ Network Error: Failed to connect to API")
        except requests.exceptions.RequestException as e:
            print(f"\n✗ Request Error: {e}")
        return None
    
    def update_post(self, post_id):
        """PUT - Update existing post"""
        try:
            url = f"{self.base_url}/posts/{post_id}"
            data = {
                "id": post_id,
                "title": "Updated Title",
                "body": "Updated body content",
                "userId": 1
            }
            response = requests.put(url, headers=self.headers, json=data, timeout=self.timeout)
            print_response_info(response, f"PUT /posts/{post_id} (Update)")
            print(f"\nRequest Body:\n{data}")
            
            if handle_errors(response):
                updated = response.json()
                print(f"\nUpdated Post:")
                print(f"  ID: {updated['id']}")
                print(f"  Title: {updated['title']}")
                return updated
        except requests.exceptions.Timeout:
            print(f"\n✗ Timeout Error: Request exceeded {self.timeout} seconds")
        except requests.exceptions.ConnectionError:
            print("\n✗ Network Error: Failed to connect to API")
        except requests.exceptions.RequestException as e:
            print(f"\n✗ Request Error: {e}")
        return None
    
    def delete_post(self, post_id):
        """DELETE - Remove post"""
        try:
            url = f"{self.base_url}/posts/{post_id}"
            response = requests.delete(url, headers=self.headers, timeout=self.timeout)
            print_response_info(response, f"DELETE /posts/{post_id}")
            
            if handle_errors(response):
                print(f"\n✓ Post {post_id} deleted successfully")
                return response.json()
        except requests.exceptions.Timeout:
            print(f"\n✗ Timeout Error: Request exceeded {self.timeout} seconds")
        except requests.exceptions.ConnectionError:
            print("\n✗ Network Error: Failed to connect to API")
        except requests.exceptions.RequestException as e:
            print(f"\n✗ Request Error: {e}")
        return None
    
    def test_404(self):
        """Test 404 error handling"""
        try:
            url = f"{self.base_url}/posts/99999"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            print_response_info(response, "GET /posts/99999 (Test 404)")
            handle_errors(response)
        except requests.exceptions.Timeout:
            print(f"\n✗ Timeout Error")
        except requests.exceptions.RequestException as e:
            print(f"\n✗ Request Error: {e}")

def main():
    print("="*50)
    print("API CLIENT - WEEK 02 FINAL PROJECT")
    print("="*50)
    
    client = APIClient()
    
    # Test GET operations
    client.get_post(1)
    client.get_all_posts()
    
    # Test POST
    client.create_post()
    
    # Test PUT
    client.update_post(1)
    
    # Test DELETE
    client.delete_post(1)
    
    # Test error handling
    client.test_404()
    
    print("\n" + "="*50)
    print("All operations completed")
    print("="*50)

if __name__ == "__main__":
    main()
