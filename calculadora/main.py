from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get(
        "/", 
        summary="Raíz de la API", 
        description="Devuelve un mensaje de bienvenida a la calculadora API."
        )
def read_root():
    return JSONResponse(content={"message": "Bienvenido a la calculadora API!"})

@app.get(
        "/Division",
        summary="División de dos números",
        description="Realiza la división de dos números y devuelve el resultado."
        )
def division(divisor: float = 0, dividendo: float = 1):
    try:
        if divisor == 0 and dividendo == 0:
            return JSONResponse(content={"error": "Indeterminación: 0 dividido por 0 no tiene un resultado definido."}, status_code=400)
        resultado = divisor / dividendo
        return JSONResponse(content={
            "resultado": resultado,
            "dividendo": dividendo,
            "divisor": divisor})
    except ZeroDivisionError:
        return JSONResponse(content={"error": "No se puede dividir por cero."}, status_code=400)
    


