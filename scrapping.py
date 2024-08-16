# librerias a utilzar
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Definición de función para escrapear los titulos de una página
def scrape_blog_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content , 'html.parser')
        titles = [title.get_text() for title in soup.find_all('h2', class_='post-title')]
        return titles
    else:
        print (f'Error al obtener página. Código de error: {response.status_code}')
        return []
    

try:
    blog_url = '' # aquí hay que definir la url
    titles = scrape_blog_titles(blog_url)
    if titles: # Validar si se encontraron títulos
        df = pd.DataFrame(titles,columns = 'Titles')        
        df.to_csv('titulos.csv', index = False)
        print ('Scrap ejecutado y archivo almacanedo')
    else: 
        print ('No se encontraron titulos')
except Exception as e:
    print (f'Error: {e}')
