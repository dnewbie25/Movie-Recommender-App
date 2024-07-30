from typing import Optional
from fastapi import FastAPI
import functions

app = FastAPI()


@app.get('/home')
async def root():
    return {'message': 'Welcome to my Data Engineering Project!! Please enter https://movie-recommender-app-ejx7.onrender.com/docs to see the full API'}

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

@app.get('/movie_recommender/{titulo}')
def movie_recommender(titulo=''):
    return functions.recommend_movie(titulo)
