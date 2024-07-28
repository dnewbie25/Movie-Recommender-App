from typing import Optional
from fastapi import FastAPI
import functions

app = FastAPI()


@app.get('/home')
async def root():
    return {'message': 'Welcome to my Data Engineering Project!!'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    return {'message': f'{functions.cantidad_filmaciones_mes(mes)} cantidad de peliculas que fueron estrenadas el mes de {mes.title()}'}

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str):
    return {'message':f"{functions.cantidad_filmaciones_dia(dia)} cantidad de peliculas que fueron estrenadas los dias {dia.title()}"}

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo):
    return functions.score_titulo(titulo)

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo):
    return functions.total_votos(titulo)

@app.get('/get_actor/{actor}')
def get_actor(actor=''):
    return functions.get_actor(actor)

@app.get('/get_director/{director}')
def get_director(director=''):
    return functions.get_director(director)
