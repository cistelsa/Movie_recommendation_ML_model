import pandas as pd
import numpy as np

# Función para crear una lista de idiomas y se puedan seleccionar en un campo de selección en html a través de ajax
def language_list_to_html():
    df_language = pd.read_csv("data/launch/spoken_languages.csv")
    df_language = df_language.dropna(subset=['name'])
    df_movie = pd.read_csv("data/launch/movies.csv")
    df_movie = df_movie.dropna(subset=['title'])
    df_collection = pd.read_csv("data/launch/belongs_to_collection.csv")
    df_collection = df_collection.dropna(subset=['name'])
    df_countries = pd.read_csv("data/launch/production_countries.csv")
    df_countries = df_countries.dropna(subset=['name'])
    df_companies = pd.read_csv("data/launch/production_companies.csv")
    df_companies = df_companies.dropna(subset=['name'])
    df_crew = pd.read_csv("data/launch/crew.csv")
    df_crew_persons = pd.read_csv("data/launch/crew_persons.csv")
    df_jobs = pd.read_csv("data/launch/crew_jobs.csv")
    # Filtrar las filas del DataFrame df_jobs por el trabajo "Director"
    director_job_id = df_jobs[df_jobs['job'] == "Director"]['job_id'].values[0]
    # Filtrar las filas del DataFrame df_crew por el ID de trabajo del director
    director_ids = df_crew[df_crew['job_id'] == director_job_id]['crew_id'].tolist()
    # Filtrar las filas del DataFrame df_crew_persons por los IDs de directores
    df_directors = df_crew_persons[df_crew_persons['crew_id'].isin(director_ids)][['name']]
    # Resetear los índices del DataFrame resultante
    df_directors = df_directors.reset_index(drop=True)
    # Eliminar Duplicados
    df_directors = df_directors.drop_duplicates()
    return df_language["name"].tolist(), df_movie["title"].tolist(), df_collection["name"].tolist(), df_countries["name"].tolist(), df_companies["name"].tolist(),  df_directors["name"].tolist()

# Función para obtener la cuenta de películas por idioma y usarlo dentro del decorador @app.get("/peliculas_idioma")
def get_language_id_count(language):
    df_movies_lang = pd.read_csv("data/launch/movies.csv")
    df_language = pd.read_csv("data/launch/spoken_languages.csv")
    
    df_movie_languages = pd.merge(df_movies_lang, df_language[['cod', 'name']], left_on='original_language', right_on='cod', how='left')
    df_movie_languages['name'] = df_movie_languages['name'].fillna('')
    
    language_id_counts = df_movie_languages.groupby('name')['id'].count().reset_index()
    
    # Convertir el idioma a minúsculas para hacerlo insensible a mayúsculas y minúsculas
    language_lower = language.lower()

    result = language_id_counts[language_id_counts['name'].str.lower() == language_lower]
    
    if not result.empty:
        name, id_count = result.iloc[0]
        return id_count
    else:
        return(0)
    
# Función para obtener la cuenta de películas, ganancia total y promedio total por franquicias y usarlo dentro del decorador @app.get("/franquicias")
def get_collection_count_revenue_mean(collection):
    # Cargo los datos de las películas\n",
    df_movies_ = pd.read_csv("data/launch/movies.csv")
    df_collection = pd.read_csv("data/launch/belongs_to_collection.csv")
    df_movie_collection = pd.read_csv("data/launch/movie_collection.csv")
    
    df_movie_collection_2 = pd.merge(df_movie_collection, df_collection[['collection_id', 'name']], on='collection_id', how='left')
    grouped_collection = df_movie_collection_2.groupby('id')['name'].agg(' '.join).reset_index()
    df_movies_ = pd.merge(df_movies_, grouped_collection, on='id', how='left')
    df_movies_ = df_movies_.rename(columns={'name': 'collection_name'})
    df_movies_ = df_movies_.astype({'collection_name': 'string'})
    df_movies_ = df_movies_.dropna(subset=['collection_name'])
    
    # Agrupar y agregar información en un solo paso
    result_df = df_movies_.groupby('collection_name').agg(
        total_movies=('id', 'count'),
        total_revenue=('revenue', 'sum'),
        average_revenue=('revenue', 'mean'),
    ).reset_index()

    # Convertir el idioma a minúsculas para hacerlo insensible a mayúsculas y minúsculas
    collection_lower = collection.lower()

    result = result_df[result_df['collection_name'].str.lower() == collection_lower]
        
    if not result.empty:
        collection_name, total_movies, total_revenue, average_revenue = result.iloc[0]
        return total_movies, total_revenue, average_revenue
    else:
        return(0)
    
# Función para obtener la cuenta de películas, por país y usarlo dentro del decorador @app.get("/franquicias")
def get_countries_movie_count(country):
    # Cargo los datos de las películas\n",
    df_countries = pd.read_csv("data/launch/production_countries.csv")
    df_movie_countries = pd.read_csv("data/launch/movie_countries.csv")
    
    df_movie_countries_2 = pd.merge(df_movie_countries, df_countries[['country_id', 'name']], on='country_id', how='left')
    df_movie_countries_2 = df_movie_countries_2.rename(columns={'name': 'countries_name'})
    df_movie_countries_2= df_movie_countries_2.astype({'countries_name': 'string'})
    df_movie_countries_2 = df_movie_countries_2.dropna(subset=['countries_name'])

    
    # Contar la cantidad de películas por país
    df_countries_id_counts = df_movie_countries_2['countries_name'].value_counts().reset_index()
    df_countries_id_counts.columns = ['countries_name', 'id_count']

    # Convertir el idioma a minúsculas para hacerlo insensible a mayúsculas y minúsculas
    country_lower = country.lower()

    result = df_countries_id_counts[df_countries_id_counts['countries_name'].str.lower() == country_lower]
        
    if not result.empty:
        countries_name, id_count = result.iloc[0]
        return id_count
    else:
        return(0)
    

# Función para obtener la cuenta de películas, por compañía productora y revenue total y usarlo dentro del decorador @app.get("/productoras_exitosas")
def get_companies_movie_count(company):
    # Cargo los datos de las películas\n",
    df_movies_ = pd.read_csv("data/launch/movies.csv")
    df_companies = pd.read_csv("data/launch/production_companies.csv")
    df_movie_companies = pd.read_csv("data/launch/movie_companies.csv")

    # Unir la información de las productoras por ID de película
    df_movie_companies_2 = pd.merge(df_movie_companies, df_companies[['production_companies_id', 'name']], on='production_companies_id', how='left')
    
    # Unir la información de las películas con las productoras
    grouped_companies = df_movie_companies_2.groupby('id')['name'].agg(', '.join).reset_index()
    df_movies_ = pd.merge(df_movies_, grouped_companies, on='id', how='left')
    df_movies_ = df_movies_.rename(columns={'name': 'companies_name'})
    df_movies_ = df_movies_.astype({'companies_name': 'string'})
    df_movies_ = df_movies_.dropna(subset=['companies_name'])

    # Contar la cantidad de películas por productora
    companies_id_counts = df_movie_companies_2['name'].value_counts().reset_index()
    companies_id_counts.columns = ['companies_name', 'id_count']

    # Calcular la suma de 'revenue' por productora
    revenue_by_company = df_movies_.groupby('companies_name')['revenue'].sum().reset_index()
    revenue_by_company.columns = ['companies_name', 'total_revenue']

    # Combinar los resultados de conteo y suma
    pre_result = pd.merge(companies_id_counts, revenue_by_company, on='companies_name')

    # Convertir el idioma a minúsculas para hacerlo insensible a mayúsculas y minúsculas
    company_lower = company.lower()

    result = pre_result[pre_result['companies_name'].str.lower() == company_lower]
        
    if not result.empty:
        companies_name, id_count, total_revenue = result.iloc[0]
        return id_count, total_revenue
    else:
        return(0)

# Función para obtener el retorno total de las películas, por director y titulo, fecha, revenue, budget, retorno en forma de lista y usarlo dentro del decorador @app.get("/get_director")    
def get_director_movies_info(director_name):

    # Cargo los datos de las películas\n",
    df_movies_ = pd.read_csv("data/launch/movies.csv")
    df_crew = pd.read_csv("data/launch/crew.csv")
    df_crew_persons = pd.read_csv("data/launch/crew_persons.csv")
    df_jobs = pd.read_csv("data/launch/crew_jobs.csv")
    # Filtrar las filas del DataFrame df_crew_persons por el nombre del director
    director_id = df_crew_persons[df_crew_persons['name'] == director_name]['crew_id'].values[0]

    # Filtrar las filas del DataFrame df_crew por el ID del director y el trabajo "Director"
    director_job_id = df_jobs[df_jobs['job'] == "Director"]['job_id'].values[0]
    movie_ids_directed_by_director = df_crew[
        (df_crew['crew_id'] == director_id) & (df_crew['job_id'] == director_job_id)
    ]['id'].tolist()

    # Filtrar las filas del DataFrame df_movies_ por los IDs de las películas dirigidas por el director
    df_movies_directed_by_director = df_movies_[df_movies_['id'].isin(movie_ids_directed_by_director)]

    # Calcular la suma del retorno de todas las películas dirigidas por el director
    total_return = df_movies_directed_by_director['return'].sum()

    # Preparar la información de las películas en formato de lista
    movies_info = []
    for index, row in df_movies_directed_by_director.iterrows():
        movie_info = {
            'title': row['title'],
            'release_date': row['release_date'],
            'return': row['return'],
            'budget': row['budget'],
            'revenue': row['revenue']
        }
        movies_info.append(movie_info)

    return total_return, movies_info

def get_recommendations_for_title(title, preview_recommendations):
    # Cargar el DataFrame precalculado desde el archivo CSV
    recommendations = preview_recommendations[preview_recommendations['movie_title'] == title]
    if not recommendations.empty:
        recommended_titles = recommendations.iloc[0]['recommended_titles']
        return recommended_titles.split(', ')
    else:
        return ["Película no encontrada en la Base de Datos."]
    
# Función para obtener la duración de las peliculas y el año
def get_runtime_by_title(title):
    df_movies = pd.read_csv("data/launch/movies.csv")
    movie = df_movies[df_movies["title"] == title]
    
    if not movie.empty:
        runtime = movie.iloc[0]["runtime"]
        year = movie.iloc[0]["release_year"]
        return runtime, year
    else:
        return None  # Película no encontrada