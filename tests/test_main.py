from fastapi.testclient import TestClient

from fastapi_tdd.main import app

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
    response = client.get("/1211")
    assert response.status_code == 200
    assert response.json() == {"1": 3, "2": 1}


def test_fourth_case():
    response = client.get("/111221")
    assert response.status_code == 200
    assert response.json() == {"1": 4, "2": 2}


def test_fifth_case():
    response = client.get("/007")
    assert response.status_code == 200
    assert response.json() == {"0": 2, "7": 1}
