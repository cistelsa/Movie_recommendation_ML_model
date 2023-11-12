import pandas as pd
import numpy as np
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import functions as f

app = FastAPI()

app.mount("/static", StaticFiles(directory="./public/static"), name="static")
app.mount("/launch", StaticFiles(directory="./data/launch"), name="launch")

templates = Jinja2Templates(directory="./public/templates")



@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    selected_data_language, selected_data_movies, selected_data_collection, selected_data_countries, selected_data_companies, selected_data_directors =  f.language_list_to_html()
    context = {"request": request, "selected_data_language": selected_data_language, "selected_data_movies":selected_data_movies, "selected_data_collection": selected_data_collection, "selected_data_countries": selected_data_countries, "selected_data_companies": selected_data_companies, "selected_data_directors": selected_data_directors}
    return templates.TemplateResponse("index.html", context)

@app.get("/peliculas_idioma")
def peliculas_idioma(idioma: str):
    cantidad = f.get_language_id_count(idioma)  # Obtener la cantidad de películas por idioma
    response_data = {"idioma": idioma, "cantidad":int(cantidad)}
    return JSONResponse(content=response_data)

@app.get("/peliculas_duracion")
def peliculas_duracion(pelicula: str):
    runtime, year = f.get_runtime_by_title(pelicula)
    response_data = {"duracion": int(runtime), "anio": int(year)}
    return JSONResponse(content=response_data)

@app.get("/franquicia")
def franquicia(franquicia: str):
    cantidad, ganancia, promedio = f.get_collection_count_revenue_mean(franquicia)
    response_data = {"franquicia": franquicia, "cantidad":int(cantidad), "ganancia":ganancia, "promedio": promedio}
    return JSONResponse(content=response_data)

@app.get("/peliculas_pais")
def peliculas_pais(pais: str):
    cantidad = f.get_countries_movie_count(pais)  # Obtener la cantidad de películas por idioma
    response_data = {"pais": pais, "cantidad":int(cantidad)}
    return JSONResponse(content=response_data)

@app.get("/productoras_exitosas")
def productoras_exitosas( productora: str ):
    cantidad, ganancia = f.get_companies_movie_count(productora)  # Obtener la cantidad de películas por idioma
    response_data = {"productora": productora, "cantidad":int(cantidad), "ganancia": ganancia}
    return JSONResponse(content=response_data)

@app.get("/get_director")
def get_director( director: str ):
    retorno, peliculas = f.get_director_movies_info(director)  # Obtener la cantidad de películas por idioma
    response_data = {"retorno": round(retorno, 2), "peliculas":peliculas}
    return JSONResponse(content=response_data)

@app.get("/recomendacion_1")
def recomendacion_1( titulo: str ):
    csv_recomendaciones_1 = pd.read_csv("data/ML/recomendaciones_peliculas_1.csv")
    recomendacion_1 = f.get_recommendations_for_title(titulo, csv_recomendaciones_1)
    csv_recomendaciones_2 = pd.read_csv("data/ML/recomendaciones_peliculas_2.csv")
    recomendacion_2 = f.get_recommendations_for_title(titulo, csv_recomendaciones_2)
    
    response_data = {"recomendacion_1":recomendacion_1, "recomendacion_2":recomendacion_2}
    return JSONResponse(content=response_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
