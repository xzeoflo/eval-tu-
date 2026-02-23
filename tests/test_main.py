from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_get_all_trainers():
    response = client.get("/trainers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_trainer_success():
    payload = {"name": "Sacha Bourg-Palette", "birthdate": "1997-05-22"}
    response = client.post("/trainers/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Sacha Bourg-Palette"
    assert "id" in data

def test_get_trainer_404():
    response = client.get("/trainers/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Trainer not found"

def test_get_items_format():
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    if len(items) > 0:
        assert "name" in items[0]
        assert "id" in items[0]

def test_create_trainer_invalid_data():
    response = client.post("/trainers/", json={})
    assert response.status_code == 422  