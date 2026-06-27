import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("=== HR RAG API Test Suite ===\n")
    
    # Test 1: Health check
    print("1. Testing health endpoints...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Root endpoint: {response.json()}")
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health check: {response.json()}\n")
    
    # Test 2: Register user
    print("2. Testing user registration...")
    register_data = {
        "username": "test_user_" + str(hash("test") % 1000),
        "password": "test123",
        "department": "IT"
    }
    
    response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
    if response.status_code == 200:
        register_result = response.json()
        print(f"Registration successful: {register_result['username']}")
        token = register_result['token']
    else:
        print(f"Registration failed: {response.status_code} - {response.text}")
        return
    
    # Test 3: Login with existing user
    print("\n3. Testing login with existing user...")
    login_data = {
        "username": "john_doe",
        "password": "password123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    if response.status_code == 200:
        login_result = response.json()
        print(f"Login successful: {login_result['username']}")
        token = login_result['token']  # Use existing user's token for tests
    else:
        print(f"Login failed: {response.status_code} - {response.text}")
    
    # Test 4: Chat questions
    print("\n4. Testing chat questions...")
    headers = {"Authorization": f"Bearer {token}"}
    
    questions = [
        "How many leaves do I have?",
        "What is my salary?", 
        "Show my payslip",
        "What was my performance rating?",
        "Show my salary and leave balance"
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        response = requests.post(
            f"{BASE_URL}/api/ask",
            json={"message": question},
            headers=headers
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"Answer: {result['answer'][:100]}...")
            print(f"Sources: {result['sources']}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_api()