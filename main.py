from typing import Optional
from fastapi import FastAPI
import functions

app = FastAPI()


@app.get("/home")
async def root():
    return {"message": "Welcome to my Machine Engineering Project"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/cantidad_filmaciones_mes/{item}")
def cantidad_filmaciones_mes(mes: str):
    return {"message": f"{functions.cantidad_filmaciones_mes(mes)} cantidad de peliculas que fueron estrenadas el mes de {mes.title()}"}

@app.get("/cantidad_filmaciones_dia/{item}")
def cantidad_filmaciones_dia(dia: str):
    return {"message":f"{functions.cantidad_filmaciones_dia(dia)} cantidad de peliculas que fueron estrenadas los dias {dia.title()}"}

@app.get("/votos_titulo/{item}")
def total_votos(titulo):
    return {"message":f""}