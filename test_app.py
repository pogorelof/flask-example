import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello(client):
    response = client.get('/hello/ChatGPT')
    assert response.status_code == 200
    assert "Привет, ChatGPT!" in response.data.decode("utf-8")
