"""
Données sources disponibles ici : https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32
Le but est d'essayer de construire un modèle de prédiction de pluie en fonction des données des stations météo
"""

import math
import pandas as pd
from sklearn.linear_model import LogisticRegression


# Import des données météo
data = pd.read_csv("synop.202403.csv",sep=";")
# Eliminer les données manquantes
data = data[data["pmer"]!="mq"]
data = data[data["rr1"]!="mq"]

size = data.size
learnSetRatio = 0.9

# Séparation du jeu de données en deux sous ensembles pour l'apprentissage et la validation
learnData = data.head(math.floor(size/learnSetRatio))
testData = data.tail(math.ceil(size/learnSetRatio))

# Création du modèle de régression
logreg = LogisticRegression()
# Apprentissage du modèle
logreg.fit(learnData[["pmer"]],learnData["rr1"])

# Validation du modèle
print(logreg.score(testData[["pmer"]],testData["rr1"]))
