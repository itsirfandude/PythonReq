import requests
import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"



def get_response(url):
    response = requests.get(url)
    assert response.status_code == 200
    return response.json()

def test_user(base_url):

    data = get_response(f"{base_url}/users/1")

    assert data["id"] == 1
    assert "email" in data
    
    print("User API test passed")


def test_post(base_url):

    data = get_response(f"{base_url}/posts/1")

    assert data["id"] == 1
    assert data["userId"] == 1

    print("Post API test passed")

def test_user_not_found(base_url):

    response = requests.get(f"{base_url}/users/9999")

    assert response.status_code == 404

    print("Negative test passed: user not found returns 404")


def test_post_fields(base_url):

    data = get_response(f"{base_url}/posts/1")

    assert data["title"] != ""
    assert data["body"] != ""
    assert len(data["title"]) > 5, "Title too short"
    print("Post fields test passed")

def test_multiple_users(base_url):

    data = get_response(f"{base_url}/users")

    for user in data:

       assert "id" in user, "User missing id field"
       assert "name" in user, "User missing name field"
       assert "email" in user, "User missing email field"
       assert "@" in user["email"], "Invalid email format"

    print("Multiple users validation passed")

def test_posts_list():

    data =get_response("https://jsonplaceholder.typicode.com/posts")

    for post in data:

        assert "id" in post, "Post missing id field"
        assert "title" in post, "Post missing title field"
        assert "body" in post, "Post missing body field"
        assert post["body"] != "", "Post body is empty"
    print("Posts list validation passed")

def test_post_lifecycle():

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={
            "title": "API Test",
            "body": "Automation lifecycle test",
            "userId": 1
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == "API Test"
    assert data["userId"] == 1

    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json={
            "id": 1,
            "title": "Updated Title",
            "body": "Updated body",
            "userId": 1
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Updated Title"

    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    assert response.status_code == 200

def test_user_schema():

    data = get_response("https://jsonplaceholder.typicode.com/users")

    for user in data:

       assert "id" in user, "User missing id field"
       assert "name" in user, "User missing name field"
       assert "username" in user, "User missing username field"
       assert "email" in user, "User missing email field"
       assert "@" in user["email"], "Invalid email format"
       assert isinstance(user["id"], int), "User id is not an integer"

@pytest.mark.parametrize("user_id", [1,2,3,4])
def test_multiple_user_ids(base_url, user_id):

    data = get_response(f"{base_url}/users/{user_id}")
    
    assert data["id"] == user_id
   






