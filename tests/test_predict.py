from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_returns_valid_response():
    payload = {
        "age": 45,
        "bmi": 31.2,
        "smoker": True,
        "region": "southwest",
        "children": 2
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200

    data = response.json()

    assert "risk_score" in data
    assert "risk_level" in data
    assert "explanation" in data

    assert isinstance(data["risk_score"], float)
    assert data["risk_level"] in ["low", "medium", "high"]
    assert isinstance(data["explanation"], str)