"""Tests unitaires avec mocks pour les fonctions d'actions et d'intégration avec PokeAPI."""
import pytest
from unittest.mock import MagicMock, patch
from main import app
from app import actions
from app.utils.pokeapi import get_pokemon_name, battle_pokemon

@patch("app.actions.add_trainer_pokemon")
def test_mock_add_pokemon(mock_add):
    mock_add.return_value = {"id": 1, "name": "Pikachu", "trainer_id": 1}
    result = actions.add_trainer_pokemon(database=MagicMock(), pokemon=MagicMock(), trainer_id=1)
    assert result["name"] == "Pikachu"
    mock_add.assert_called_once()

@patch("app.utils.pokeapi.requests.get")
def test_mock_external_pokeapi(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"name": "bulbasaur", "weight": 69}
    from app.utils.pokeapi import get_pokemon_name
    name = get_pokemon_name(1)
    assert name == "bulbasaur"

@patch("app.actions.get_items")
def test_mock_get_items_empty(mock_items):
    mock_items.return_value = []
    result = actions.get_items(database=MagicMock())
    assert len(result) == 0

@patch("app.utils.pokeapi.get_pokemon_data")
def test_mock_get_pokemon_name(mock_data):
    """ Test la récupération du nom via un mock de la donnée brute """
    mock_data.return_value = {"name": "pikachu"}
    assert get_pokemon_name(25) == "pikachu"

@patch("app.utils.pokeapi.get_pokemon_stats")
@patch("app.utils.pokeapi.get_pokemon_name")
def test_mock_battle_pokemon_victory(mock_name, mock_stats):
    """ Test le flux complet du combat simulé avec des mocks """
    mock_name.side_effect = ["Pikachu", "Magicarpe"]
    mock_stats.side_effect = [{"hp": 50}, {"hp": 10}]
    
    result = battle_pokemon(25, 129)
    
    assert result["winner"] == "Pikachu"
    assert result["status"] == "victory"