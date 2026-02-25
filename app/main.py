from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    data = {"message": "Pruebas unitarias"}
    return JSONResponse(status_code= 200, content=data)

@app.get("/suma")
async def suma(numero1: int = 0, numero2: int = 0):
    suma = numero1 + numero2
    data = {
        "numero1": numero1,
        "numero2": numero2,
        "result": suma
        }
    return JSONResponse(status_code=200, content=data)