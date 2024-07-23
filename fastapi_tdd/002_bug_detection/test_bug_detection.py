from bug_detection import app
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


def test_third_case():
    response = client.get("/007")
    assert response.status_code == 200
    assert response.json() == {"0": 2, "7": 1}
