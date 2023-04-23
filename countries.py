import requests
from bs4 import BeautifulSoup

url = 'http://www.scrapethissite.com/pages/simple/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Pour chaque bloque de pays
for countryBlock in soup.find_all('h3', class_="country-name"):
    # Affiche le nom du pays
    print(countryBlock.get_text())