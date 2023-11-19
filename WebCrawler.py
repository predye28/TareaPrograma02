import requests
from bs4 import BeautifulSoup
import csv
import nltk
from nltk.stem import SnowballStemmer
import time

start_url = "https://es.wikipedia.org/wiki/Casa_Blanca"

max_pages_to_crawl = 1000

pages_data = []

nltk.download("stopwords")
stemmer = SnowballStemmer("spanish")

def extract_page_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            page_data = {
                "title": soup.title.string,
                "subtitles": [],
                "text": [],
                "images": [],
                "references": [],
                "tags": []
            }


            subtitles = soup.find_all("span", {"class": "mw-headline"})
            #
            page_data["subtitles"] = [subtitle.get_text() for subtitle in subtitles]
            #
            page_data["text"] = [paragraph.get_text() for paragraph in soup.find_all('p')]

            #
            images = soup.find_all("img")
            for image in images:
                image_data = {
                    "src": image.get("src"),
                    "alt": [stemmer.stem(word) for word in nltk.word_tokenize(str(image.get("alt")))]
                }
                page_data["images"].append(image_data)

            #
            references = soup.find_all("a", {"class": "external text"})
            for reference in references:
                reference_data = {
                    "link": reference["href"],
                    "description": reference.get_text()
                }
                page_data["references"].append(reference_data)

            pages_data.append(page_data)

            print(f"Visitando: {url} - Páginas procesadas: {len(pages_data)}/{max_pages_to_crawl}")

    except Exception as e:
        print(f"Error al rastrear {url}: {e}")


requests_per_minute_limit = 50
seconds_per_request = 60 / requests_per_minute_limit


visited_urls = set([start_url])
pages_processed = 0

while visited_urls and pages_processed < max_pages_to_crawl:
    current_url = visited_urls.pop()
    try:

        response = requests.get(current_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            #la chicha 
            extract_page_data(current_url)


            links = soup.find_all("a", href=True)
            for link in links:
                next_url = link["href"]
                if next_url.startswith("/wiki/"):
                    next_url = "https://es.wikipedia.org" + next_url
                    if next_url not in visited_urls:
                        visited_urls.add(next_url)


            pages_processed += 1


            if pages_processed % 50 == 0:
                with open("wikipedia_data.csv", "a", newline="", encoding="utf-8") as csv_file:
                    csv_writer = csv.writer(csv_file)

                    for page_data in pages_data[-50:]:
                        title = page_data["title"]
                        
                        #
                        for subtitle, text in zip(page_data["subtitles"], page_data["text"]):
                            csv_writer.writerow([title, subtitle, text, "", "", "", ""])  # Dejamos las columnas de imágenes y referencias en blanco

                        # 
                        for image in page_data["images"]:
                            csv_writer.writerow([title, "", "", image["src"], "|".join(image["alt"]), "", ""])  # Dejamos las columnas de subtítulo y referencias en blanco

                        #
                        for reference in page_data["references"]:
                            csv_writer.writerow([title, "", "", "", "", reference["link"], reference["description"]])  # Dejamos las columnas de subtítulo e imágenes en blanco

                print(f"Guardando datos después de procesar {pages_processed} páginas")

            ##
            time.sleep(seconds_per_request)

    except requests.RequestException as e:
        print(f"Error al procesar {current_url}: {e}")

with open("wikipedia_data.csv", "a", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    if csv_file.tell() == 0:
        csv_writer.writerow(["Page_Title", "Subtitle", "Subtitle_Text", "Image_SRC", "Image_ALT", "Reference_Link", "Reference_Description"])

    for page_data in pages_data:
        title = page_data["title"]
        

        for subtitle, text in zip(page_data["subtitles"], page_data["text"]):
            csv_writer.writerow([title, subtitle, text, "", "", "", ""])


        for image in page_data["images"]:
            csv_writer.writerow([title, "", "", image["src"], "|".join(image["alt"]), "", ""])  


        for reference in page_data["references"]:
            csv_writer.writerow([title, "", "", "", "", reference["link"], reference["description"]])  

print(f"Los datos se han guardado en el archivo CSV: wikipedia_data.csv")