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

    validate(instance=response, schema=user_schema)
    assert "name" in response
    assert response["email"] == payload["email"]
    assert "id" in response
    assert isinstance(response["id"], int)  

def test_create_user_invalid_email(api, faker):
    payload = {
        "username": faker.user_name(),
        "email": "irfan"  # invalid email
    }

    response = api.create_user(payload)

    # System should ideally reject invalid email, but currently accepts it
    assert response["email"] == payload["email"]

    # Observation: validation gap
    assert "@" not in payload["email"]

def test_create_user_invalid_payload(api):
    payload = {
        "name": "",  # empty name
        "email": "irfan",  # invalid email
        "goal": "irfan"  # unexpected field
    }

    response = api.create_user(payload)

    # API is accepting invalid payload
    assert response["email"] == payload["email"]

    # Observation: system is not validating required fields or schema strictly

def test_create_user_empty_payload(api):
    payload = {}

    response = api.create_user(payload)

    # API is accepting empty payload
    assert isinstance(response, dict)

    # Observation: system should reject empty payload but currently accepts it


def test_create_user_invalid_datatype(api):
    payload = {
        "name": 123,
        "email": 999
    }

    response = api.create_user(payload)

    # API is accepting invalid datatypes
    assert response["email"] == payload["email"]
    assert response["name"] == payload["name"]