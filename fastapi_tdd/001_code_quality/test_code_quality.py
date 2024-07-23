from code_quality import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_first_case():
    response = client.get("/11")
    assert response.status_code == 200
    assert response.json() == {"1": 2}


def test_second_case():
    response = client.get("/21")
    assert response.status_code == 200
    assert response.json() == {"1": 1, "2": 1}
