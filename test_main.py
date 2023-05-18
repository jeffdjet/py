from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    assert response.json()[0] == {
         "firstname": "jeff",
         "lastname": "givera",
         "gender": "M",
         "age": 18}