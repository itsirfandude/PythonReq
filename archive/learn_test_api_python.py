import requests

def get_response(url):
    response = requests.get(url)
    assert response.status_code == 200
    return response.json()

def test_user():

    data = get_response("https://jsonplaceholder.typicode.com/users/1")

    assert data["id"] == 1
    assert "email" in data
    
    print("User API test passed")


def test_post():

    data = get_response("https://jsonplaceholder.typicode.com/posts/1")

    assert data["id"] == 1
    assert data["userId"] == 1

    print("Post API test passed")

def test_user_not_found():

    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")

    assert response.status_code == 404

    print("Negative test passed: user not found returns 404")


def test_post_fields():

    data = get_response("https://jsonplaceholder.typicode.com/posts/1")

    assert data["title"] != ""
    assert data["body"] != ""
    assert len(data["title"]) > 5, "Title too short"
    print("Post fields test passed")

def test_multiple_users():

    data = get_response("https://jsonplaceholder.typicode.com/users")

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

if __name__ == "__main__":
    test_user()
    test_post()
    test_user_not_found()
    test_post_fields()
    test_multiple_users()
    test_posts_list()
    test_post_lifecycle()