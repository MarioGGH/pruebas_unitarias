import pytest
import requests
BASE_URL = "http://localhost:8000/Division"  

def test_division():
    divisor = 10
    dividendo = 2
    params = {"divisor": divisor, "dividendo": dividendo} 
    resultado = divisor / dividendo
    response = requests.get(f"{BASE_URL}", params=params)
    data = {
        "resultado": resultado,
        "dividendo": dividendo,
        "divisor": divisor
    }
    assert response.status_code == 200
    assert response.json() == data

def test_division_por_cero():
    divisor = 10
    dividendo = 0
    params = {"divisor": divisor, "dividendo": dividendo}
    response = requests.get(f"{BASE_URL}", params=params)
    assert response.status_code == 400
    assert response.json() == {"error": "No se puede dividir por cero."}

def test_division_indeterminada():
    divisor = 0
    dividendo = 0
    params = {"divisor": divisor, "dividendo": dividendo}
    response = requests.get(f"{BASE_URL}", params=params)
    assert response.status_code == 400
    assert response.json() == {"error": "Indeterminación: 0 dividido por 0 no tiene un resultado definido."}