import requests
from bs4 import BeautifulSoup
import pandas as pd


def getYear(year):
    response = requests.get(f"https://www.formula1.com/en/results.html/${year}/races.html")
    soup = BeautifulSoup(response.text, 'html.parser')


    # Vérifier qu'il n'y a bien qu'une seule table avec la bonne classe
    if len(soup.find_all('table',{"class":"resultsarchive-table"})) != 1:
        print("Il n'y a pas qu'un seul tableau avec la class resultsarchive-table")
        exit()

    data = []
    for ligne in soup.find('table',{"class":"resultsarchive-table"}).find('tbody').find_all('tr'):
        tds = ligne.find_all('td')
        data.append([
            tds[1].get_text().strip(),
            tds[2].get_text().strip(),
            " ".join(span.text.strip() for span in tds[3].find_all('span')[:2]),
            tds[4].get_text().strip(),
            int(tds[5].get_text().strip()),
            tds[6].get_text().strip()
        ])
    return data


dataFrame = pd.DataFrame()
for year in range(2024,2025):
    dataFrame = pd.concat([dataFrame,pd.DataFrame(getYear(year),columns=["grandPrix","date","gagnant","voiture","tours","temps"])], ignore_index=True)

print(dataFrame)