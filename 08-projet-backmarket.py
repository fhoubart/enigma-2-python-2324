"""
Objectif : collecter des informations sur le prix des ordinateurs portables sur le site de backmarket et créer une regression capable
d'estimer le prix de vente d'une machine a partir de ses caractéristiques
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import math
from sklearn.linear_model import LogisticRegression


BASE_URL = "https://www.backmarket.fr/"

def parseLaptopPage(url):
    """
    Parse une page de description d'un pc pour y récupérer les caractéristiques et le prix.
    Renvoie les données sous forme de dictionnaire, chaque clef correspondant au libellé de la caractéristique,
    et la clef "prix" pour le prix.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Récupérer le prix qui est dans un div avec un attribut data-test="normal-price"
    try:
        prix = float(re.sub(r"[^0-9]*(\d+),(\d+).*",r"\1.\2",soup.find('div',{"data-test":"normal-price"}).text.strip()))
    except:
        prix = pd.NA
    
    # Les caractéristiques sont dans une liste <ul><li> dans un bloc div qui commence par un entête h3 => on commence par
    # trouver l'entête pour remonter sur le div via le parent, et on y cherche tous les li
    caracteristiques = {}
    try:
        liCaracteristiques = soup.find('h3',string=re.compile("Tout ce que vous avez toujours voulu savoir sur ce produit")).parent.find_all('li')

        # Pour chaque li, on peut maintenant extraire les caractéristiques qui sont dans des blocs span
        for caracteristique in liCaracteristiques:
                key = re.sub(r"^(.*[^ ]) *: *$",r"\1",caracteristique.find('span', {"class":"body-1-bold"}).text.strip())
                value = caracteristique.find('span', {"class":"body-1-light"}).text.strip()
                caracteristiques[key] = value
    except:
        pass

    caracteristiques["prix"] = prix
    print(caracteristiques)
    return caracteristiques


def getProductLinks(url):
    """
    Récupère la liste des liens vers les pages descriptives des pc à partir d'une page de listing du catalogue
    Renvoie un tableau d'urls
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Les pc sur la page catalogue sont dans des div avec la class "productCard", et chaque div contient une balise <a> avec en href le lien vers la page descriptive du pc
    return [div.find('a')["href"] for div in soup.find_all('div',{"class":"productCard"})]



def collectDataFromWeb():
    """
    Navigue sur le site de backmarket et collecte les données
    Renvoi un pd.DataFrame
    """
    data = pd.DataFrame()

    index = 1
    # Loop on each page of the catalog
    for page in range(1,4):
        # Loop on each links of the catalogue pages
        for lien in getProductLinks(f"https://www.backmarket.fr/fr-fr/l/ordinateur-portable-bureautique-reconditionne/7684cc26-1f7e-4eff-9324-905ab7663162?page={page}"):
            print(BASE_URL+lien)

            # Ajoute le nouveau PC au DataFrame. On utilise pd.concat car les différents pc n'ont pas forcement le même nombre d'attributs. Concat va ajouter les colonnes et les valeurs NaN manquantes sur les autres lignes automatiquement
            data = pd.concat([
                data,
                # Le dictionnaire créé à la volé permet de convertir le dictionnaire {key:value} en { key: [value] } attendu par le constructeur pd.DataFrame()
                pd.DataFrame({k:[v] for k,v in parseLaptopPage(BASE_URL+lien).items()})
            ],ignore_index=True)
            #time.sleep(0.5)
            index = index + 1

    return data



# Collecte des données
#data = collectDataFromWeb()
# Sauvegarde du dataset
#data.to_csv("backmarket_data.csv")

data = pd.read_csv("backmarket_data.csv")

FEATURES = ["Capacité de stockage","Mémoire","Vitesse du processeur","Taille écran (pouces)","Poids"]

data = data[FEATURES+["prix"]].dropna()
# Transformation des données

# Suppression du Go sur la capacité de stockage
data["Capacité de stockage"] = data["Capacité de stockage"].apply(lambda x: int(re.match(r"([0-9]*)",x).group(1)))
# Suppression du Go sur la mémoire
data["Mémoire"] = data["Mémoire"].apply(lambda x: int(re.match(r"([0-9]*)",x).group(1)))
# Extraction de la valeur float sur la fréquence
data["Vitesse du processeur"] = data["Vitesse du processeur"].apply(lambda x: float(re.match(r"([0-9]*\.[0-9]*)",x).group(1)))
# Extraction de la valeur numérique sur la taille de l'écran
data["Taille écran (pouces)"] = data["Taille écran (pouces)"].apply(lambda x: float(x))
# Extraction de la valeur numérique pour le poids
data["Poids"] = data["Poids"].apply(lambda x: int(re.match(r"([0-9]*)",x).group(1)))
print(data)


# Création du modèle de régression
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import linear_model

logreg = linear_model.Lasso()


size = len(data)
learnSetRatio = 0.8

# Séparation du jeu de données en deux sous ensembles pour l'apprentissage et la validation
print(math.floor(size*learnSetRatio))
print(math.ceil(size*learnSetRatio))
learnData = data.head(math.floor(size*learnSetRatio))
testData = data.tail(math.ceil(size*learnSetRatio))


print("Learn Dataset")
print(learnData[FEATURES])
print(learnData["prix"])
print()
print("Test Dataset")
print(testData[FEATURES])
print(testData["prix"])

logreg.fit(learnData[FEATURES],learnData["prix"])
print(logreg.score(testData[FEATURES],testData["prix"]))

print(logreg.predict(pd.DataFrame({
"Capacité de stockage":[512],
"Mémoire": [8],
"Vitesse du processeur": [2.9],
"Taille écran (pouces)": [14],
"Poids": [4000]
})))




