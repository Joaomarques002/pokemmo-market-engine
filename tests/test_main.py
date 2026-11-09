from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_read_root():
    """Testa se o endpoint raiz responde corretamente e está online."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "project": "PokeMMO Market Engine"}