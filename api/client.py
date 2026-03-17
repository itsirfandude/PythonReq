import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_user(self, user_id):

        response = requests.get(f"{self.base_url}/users/{user_id}")
        assert response.status_code == 200

        return response.json()

    def get_user_schema(self):

        response = requests.get(f"{self.base_url}/users")
        assert response.status_code == 200

        return response.json()

    def get_post(self, post_id):

        response = requests.get(f"{self.base_url}/posts/{post_id}")
        assert response.status_code == 200

        return response.json()

    def get_users(self):

        response = requests.get(f"{self.base_url}/users")
        assert response.status_code == 200
        return response.json()

    def create_user(self, payload):

        response = requests.post(f"{self.base_url}/users", json=payload)
        assert response.status_code in [200, 201]
        return response.json()