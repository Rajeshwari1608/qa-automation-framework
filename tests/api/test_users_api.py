import time
from jsonschema import validate

from utils.api_client import APIClient
from utils.config import Config


BASE_URL = "https://jsonplaceholder.typicode.com"

api_client = APIClient(Config.API_BASE_URL)


def test_get_users():

    response = api_client.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_user():

    response = api_client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data
    assert "email" in data


def test_create_user():

    payload = {
        "name": "Rajeshwari",
        "username": "rajeshwari_test",
        "email": "rajeshwari@example.com"
    }

    response = api_client.post("/users", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]


def test_update_user():

    payload = {
        "name": "Updated User",
        "email": "updated@example.com"
    }

    response = api_client.put("/users/1", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]


def test_delete_user():

    response = api_client.delete("/users/1")

    assert response.status_code == 200


def test_get_invalid_user():

    response = api_client.get("/users/9999")

    assert response.status_code == 404


def test_invalid_endpoint():

    response = api_client.get("/invalid-endpoint")

    assert response.status_code == 404


def test_user_response_structure():

    response = api_client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    required_fields = [
        "id",
        "name",
        "username",
        "email"
    ]

    for field in required_fields:
        assert field in data


def test_api_response_time():

    start_time = time.time()

    response = api_client.get("/users")

    end_time = time.time()

    response_time = end_time - start_time

    assert response.status_code == 200
    assert response_time < 2


def test_user_response_schema():

    response = api_client.get("/users/1")

    assert response.status_code == 200

    schema = {
        "type": "object",
        "required": [
            "id",
            "name",
            "username",
            "email"
        ],
        "properties": {
            "id": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "username": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        }
    }

    validate(
        instance=response.json(),
        schema=schema
    )