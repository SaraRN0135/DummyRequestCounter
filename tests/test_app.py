from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_hit():
    response = client.get("/hit")
    assert response.status_code == 200
    data = response.json()
    assert "hits" in data or "error" in data
