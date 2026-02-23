"""Tests unitaires pour les endpoints de l'API et la fonction de comparaison de stats."""
from fastapi.testclient import TestClient
from app.utils.pokeapi import battle_compare_stats
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

def test_battle_compare_stats_first_wins():
    """ Test si le premier pokemon gagne avec plus de stats supérieures """
    stats1 = {"hp": 100, "attack": 50, "speed": 30}
    stats2 = {"hp": 80, "attack": 40, "speed": 40}
    assert battle_compare_stats(stats1, stats2) == 1

def test_battle_compare_stats_draw():
    """ Test si le combat finit en match nul """
    stats1 = {"hp": 50, "attack": 50}
    stats2 = {"hp": 50, "attack": 50}
    assert battle_compare_stats(stats1, stats2) == 0

def test_battle_compare_stats_second_wins():
    """ Test si le deuxième pokemon gagne """
    stats1 = {"hp": 10, "attack": 10}
    stats2 = {"hp": 20, "attack": 20}
    assert battle_compare_stats(stats1, stats2) == -1