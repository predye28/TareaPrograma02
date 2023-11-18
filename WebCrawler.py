import requests
from bs4 import BeautifulSoup
import csv
import nltk
from nltk.stem import SnowballStemmer
import time

# Definir la URL de Wikipedia de inicio
start_url = "https://es.wikipedia.org/wiki/Casa"

# Definir el límite de páginas a rastrear (ajústalo según tus necesidades)
max_pages_to_crawl = 1000

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

# Configurar el límite de solicitudes por minuto
requests_per_minute_limit = 50
seconds_per_request = 60 / requests_per_minute_limit

# Comenzar el rastreo desde la página principal de Wikipedia
visited_urls = set([start_url])
pages_processed = 0

while visited_urls and pages_processed < max_pages_to_crawl:
    current_url = visited_urls.pop()
    try:
        # Hacer la solicitud solo una vez
        response = requests.get(current_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Procesar la página actual
            extract_page_data(current_url)

            # Recorrer enlaces para añadir a la lista de URLs si aún no se han visitado
            links = soup.find_all("a", href=True)
            for link in links:
                next_url = link["href"]
                if next_url.startswith("/wiki/"):
                    next_url = "https://es.wikipedia.org" + next_url
                    if next_url not in visited_urls:
                        visited_urls.add(next_url)

            # Incrementar el contador de páginas procesadas
            pages_processed += 1

            # Guardar datos en el archivo CSV cada 50 páginas
            if pages_processed % 50 == 0:
                with open("wikipedia_data.csv", "a", newline="", encoding="utf-8") as csv_file:
                    csv_writer = csv.writer(csv_file)

                    # Escribir los datos de las últimas páginas procesadas en el archivo CSV
                    for page_data in pages_data[-50:]:
                        title = page_data["title"]
                        
                        # Escribir información de subtítulos y texto
                        for subtitle, text in zip(page_data["subtitles"], page_data["text"]):
                            csv_writer.writerow([title, subtitle, text, "", "", "", ""])  # Dejamos las columnas de imágenes y referencias en blanco

                        # Escribir información de imágenes
                        for image in page_data["images"]:
                            csv_writer.writerow([title, "", "", image["src"], "|".join(image["alt"]), "", ""])  # Dejamos las columnas de subtítulo y referencias en blanco

                        # Escribir información de referencias
                        for reference in page_data["references"]:
                            csv_writer.writerow([title, "", "", "", "", reference["link"], reference["description"]])  # Dejamos las columnas de subtítulo e imágenes en blanco

                print(f"Guardando datos después de procesar {pages_processed} páginas")

            # Esperar antes de la siguiente solicitud para no sobrecargar el servidor
            time.sleep(seconds_per_request)

    except requests.RequestException as e:
        print(f"Error al procesar {current_url}: {e}")

# Al final, guardar los datos restantes en el archivo CSV
with open("wikipedia_data.csv", "a", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Escribir la fila de encabezados si el archivo está vacío
    if csv_file.tell() == 0:
        csv_writer.writerow(["Page_Title", "Subtitle", "Subtitle_Text", "Image_SRC", "Image_ALT", "Reference_Link", "Reference_Description"])

    # Escribir los datos de cada página en el archivo CSV
    for page_data in pages_data:
        title = page_data["title"]
        
        # Escribir información de subtítulos y texto
        for subtitle, text in zip(page_data["subtitles"], page_data["text"]):
            csv_writer.writerow([title, subtitle, text, "", "", "", ""])  # Dejamos las columnas de imágenes y referencias en blanco

        # Escribir información de imágenes
        for image in page_data["images"]:
            csv_writer.writerow([title, "", "", image["src"], "|".join(image["alt"]), "", ""])  # Dejamos las columnas de subtítulo y referencias en blanco

        # Escribir información de referencias
        for reference in page_data["references"]:
            csv_writer.writerow([title, "", "", "", "", reference["link"], reference["description"]])  # Dejamos las columnas de subtítulo e imágenes en blanco

print(f"Los datos se han guardado en el archivo CSV: wikipedia_data.csv")