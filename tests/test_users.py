import pytest
from jsonschema import validate
from tests.schema import user_schema


def test_fake_user_data(faker):

    name = faker.name()
    email = faker.email()

    print(f"Generated Name: {name}")
    print(f"Generated Email: {email}")

    assert isinstance(name, str)
    assert "@" in email

def test_users_schema(api):

    users = api.get_users()

    for user in users:
        validate(instance=user, schema=user_schema)

@pytest.mark.smoke
def test_user(api):
    user = api.get_user(1)

    assert user["id"] == 1
    assert "email" in user

@pytest.mark.regression
@pytest.mark.parametrize("user_id", [1,2,3,4])
def test_multiple_user_ids(api, user_id):

    user = api.get_user(user_id)
    
    assert user["id"] == user_id
    assert "email" in user
    assert isinstance(user["id"], int)
    assert "username" in user

def test_create_user_with_faker(api, faker):

    payload = {
        "name": faker.name(),
        "username": faker.user_name(),
        "email": faker.email()
    }

    print(f"Payload: {payload}")

    response = api.create_user(payload)

    assert response["name"] == payload["name"]
    assert response["email"] == payload["email"]