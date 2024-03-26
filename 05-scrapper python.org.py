import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

response = requests.get("https://www.python.org/downloads/")
#print(response.text)
print()

print("Start parsing")
soup = BeautifulSoup(response.text, 'html.parser')


## Accès direct via la class
div = soup.find('div',{"class":"download-os-source"})

buttons = div.find_all('a',{"class":"button"})
print(len(buttons))

## Recherche par le titre de la section (h1)
h1 = soup.find('h1',string=re.compile("Download the latest source release"))
print(h1)
div = h1.parent
button = div.find('a',{"class":"button"})
print(button.text)


## Tableau des versions
data = pd.DataFrame({
    "Release": [elt.text for elt in soup.find('ol',{"class":"list-row-container"}).find_all('span',{"class":"release-version"})],
    "Release End": [elt.text for elt in soup.find('ol',{"class":"list-row-container"}).find_all('span',{"class":"release-end"})]
})
print(data)


## Le même mais ligne à ligne
tableau = []
lignes = soup.find("h2",string=re.compile("Active Python Releases")).parent.find('ol').find_all('li')
for ligne in lignes:
    tableau.append([ligne.find('span',{"class":"release-version"}).text,ligne.find('span',{"class":"release-end"}).text])

print(tableau)

data = pd.DataFrame(tableau,columns=["Release","Release End"])
print(data)