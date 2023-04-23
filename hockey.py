import requests
import csv
from bs4 import BeautifulSoup

# Fonction pour scrapt la page courant
def scrapt(page, writer):
    url = 'http://www.scrapethissite.com/pages/forms/?page_num=' + str(page)

    print("Trying to scrapt...", url)

    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')

    # Récupération de chaque lignes
    for row in table.find_all('tr', class_="team"):
        # Récupération de chaque cellules
        cells = row.find_all('td')
        if cells:
            teamName = cells[0].text.strip()
            year = cells[1].text.strip()
            wins = cells[2].text.strip()
            losses = cells[3].text.strip()
            ot_losses = cells[4].text.strip()
            win_percentage = cells[5].text.strip()
            gf = cells[6].text.strip()
            ga = cells[7].text.strip()
            diff = cells[8].text.strip()

            if int(diff) > 0:
                if int(ga) < 300:
                    # Ecrit à l'aide du writer dans le fichier CSV
                    writer.writerow([teamName, year, wins, losses, ot_losses, win_percentage, gf, ga, diff])

# Ouverture du fichier result.csv
with open('result.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # Ecriture du header du CSV
    writer.writerow(['Team Name, Year, Wins, Losses, OT Losses, Win %, Goals For (GF), Goals Againts (GA), +/-'])
    
    # Sauvegarde de la page courant
    current_page = 1
    # Execute jusqu'a que la page soit égale à 10
    while current_page <= 10:
        # Appel la fonction scrapt
        scrapt(current_page, writer)

        # Incrémente la page courant de 1
        current_page += 1
