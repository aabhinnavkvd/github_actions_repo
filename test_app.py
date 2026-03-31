import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Flask GitHub Actions Practice!" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add(client):
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.get_json() == {
        "a": 2,
        "b": 3,
        "result": 5
    }