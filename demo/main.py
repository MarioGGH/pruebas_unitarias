import requests
import random
import time

BASE_URL = "https://iotdemo-422f3-default-rtdb.firebaseio.com/sensores/sucursal1.json"

def get_sensores():
    response = requests.get(BASE_URL)
    print(response.status_code)
    print (response.json())

def simular_sensores():
    while True:
        data = {
            "temperatura": random.uniform(0, 40),
            "humedad": random.uniform(0, 100)
        }
        response = requests.put(BASE_URL, json=data)
        print("Datos enviados:", data)
        print(response.status_code)
        time.sleep(1)

if __name__ == "__main__":
    get_sensores()
    simular_sensores()