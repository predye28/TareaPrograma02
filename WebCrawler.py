import requests
from bs4 import BeautifulSoup
import json  # Para almacenar los datos en formato JSON
import nltk
from nltk.stem import SnowballStemmer

# Definir la URL de Wikipedia de inicio
start_url = "https://es.wikipedia.org/wiki/Ambiente_construido"

# Definir el límite de páginas a rastrear (ajústalo según tus necesidades)
max_pages_to_crawl = 2

# Crear una lista para almacenar los datos de cada página
pages_data = []

# Configuración de NLTK para el Stemming
nltk.download("stopwords")
stemmer = SnowballStemmer("spanish")

def extract_page_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Extraer información de la página
            page_data = {
                "title": soup.title.string,
                "subtitles": [],
                "text": [],
                "images": [],
                "references": [],
                "tags": []
            }

            # Extraer subtítulos
            subtitles = soup.find_all("span", {"class": "mw-headline"})
            page_data["subtitles"] = [subtitle.get_text() for subtitle in subtitles]

            # Extraer texto, evitando elementos que no son cadena de texto
            page_data["text"] = [str(element) for element in soup.find_all(string=True) if isinstance(element, (str, bytes))]


            # Extraer imágenes y aplicar Stemming al "alt" texto
            images = soup.find_all("img")
            for image in images:
                image_data = {
                    "src": image.get("src"),
                    "alt": [stemmer.stem(word) for word in nltk.word_tokenize(str(image.get("alt")))]
                }
                page_data["images"].append(image_data)

            # Extraer referencias
            references = soup.find_all("a", {"class": "external text"})
            for reference in references:
                reference_data = {
                    "link": reference["href"],
                    "description": reference.get_text()
                }
                page_data["references"].append(reference_data)

            # Puedes agregar más procesamiento para los tags y otros datos si es necesario

            # Agregar los datos de la página a la lista
            pages_data.append(page_data)

            # Mostrar el progreso
            print(f"Visitando: {url} - Páginas procesadas: {len(pages_data)}/{max_pages_to_crawl}")

    except Exception as e:
        print(f"Error al rastrear {url}: {e}")

# Comenzar el rastreo desde la página principal de Wikipedia
visited_urls = [start_url]

while visited_urls and len(pages_data) < max_pages_to_crawl:
    current_url = visited_urls.pop(0)
    extract_page_data(current_url)

    # Recorrer enlaces para añadir a la lista de URLs si aún no se han visitado
    try:
        response = requests.get(current_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a", href=True)
            for link in links:
                next_url = link["href"]
                if next_url.startswith("/wiki/"):
                    next_url = "https://es.wikipedia.org" + next_url
                    if next_url not in visited_urls:
                        visited_urls.append(next_url)

    except Exception as e:
        print(f"Error al obtener enlaces de {current_url}: {e}")

# Al final, guardar los datos en un archivo JSON
with open("wikipedia_data.json", "w", encoding="utf-8") as json_file:
    json.dump(pages_data, json_file, ensure_ascii=False, indent=4)