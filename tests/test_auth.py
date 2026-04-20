from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_missing_api_key_returns_401():
    response = client.get("/auth/me")
    assert response.status_code == 401

def test_create_api_key_returns_key():
    response = client.post("/auth/create-api-key")
    assert response.status_code == 200

    body = response.json()
    assert "api_key" in body
    assert body["api_key"].startswith("ins_")

def test_valid_api_key_passes():
    create_reponse = client.post("auth/create-api-key")
    api_key = create_reponse.json()["api_key"]

    response = client.get("/auth/me", headers={"X-API-Key": api_key})
    assert response.status_code == 200
    assert "id" in response.json()