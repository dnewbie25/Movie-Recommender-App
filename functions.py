"""Este archivo devuelve las funciones correspondientes para la API"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

movies = pd.read_csv("Machine Learning Model/movies_dataset_cleaned.csv")
final_data_set = pd.read_csv("Machine Learning Model/final_movie_set.csv",compression="gzip")
actors = pd.read_csv("Machine Learning Model/actors.csv",compression="gzip")
crew = pd.read_csv("Machine Learning Model/crew.csv",compression="gzip")

def cantidad_filmaciones_mes(mes):
  meses = {
        "enero":1,
        "febrero":2,
        "marzo":3,
        "abril":4,
        "mayo":5,
        "junio":6,
        "julio":7,
        "agosto":8,
        "septiembre":9,
        "octubre":10,
        "noviembre":11,
        "diciembre":12
    }
  valor = meses[mes]
  movies["release_date"] = pd.to_datetime(movies['release_date'], errors='coerce')
  return movies[movies["release_date"].dt.month == valor]["release_date"].count()


def cantidad_filmaciones_dia(dia):
  dias = {
    "lunes":"Monday",
    "martes":"Tuesday",
    "miercoles":"Wednesday",
    "jueves":"Thursday",
    "viernes":"Friday",
    "sabado":"Saturday",
    "domingo":"Sunday"
  }
  valor = dias[dia]
  movies["release_date"] = pd.to_datetime(movies['release_date'], errors='coerce')
  return movies[movies["release_date"].dt.strftime('%A') == valor]["release_date"].count()

def total_votos(titulo=""):
  titulo = titulo.title()
  return movies["title"].str.title()

print(total_votos())