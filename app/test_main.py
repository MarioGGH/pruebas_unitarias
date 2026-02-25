import requests
import pytest

BASE_URL = "http://localhost:8000"

def test_read_root():
    url = f"{BASE_URL}/"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"message": "Pruebas unitarias"}

def test_suma():
    url = f"{BASE_URL}/suma"
    params = {"numero1": -1, "numero2": -10}
    response = requests.get(url, params=params)
    assert response.status_code == 200
    expected_result = {
        "numero1": -1,
        "numero2": -10,
        "result": -11
    }
    assert response.json() == expected_result