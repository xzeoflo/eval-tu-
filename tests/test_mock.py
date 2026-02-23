from fastapi.testclient import TestClient
from application.main import app, return_square

client = TestClient(app)

def test_return_square_(mocker):
    mocker.patch("application.main.get_square", return_value=25)
    result = 50
    response = client.get("/twice/5")
    assert result == response.json()
    assert response.status_code == 200
