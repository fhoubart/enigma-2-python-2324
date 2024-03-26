import pandas as pd
import random

# Liste des régions
regions = []
for i in range(99):
    regions.append(i)


# Fonction pour générer une note aléatoire entre 0 et 100
def generate_random_score():
    return random.randint(0, 100)

# Création des données
data = {
    'Region': [],
    'Note': []
}

# Génération de 1000 lignes avec des régions et des notes aléatoires
for _ in range(1000):
    region = random.choice(regions)
    score = generate_random_score()
    data['Region'].append(region)
    data['Note'].append(score)

# Création du DataFrame
df = pd.DataFrame(data)

# Écriture du DataFrame dans un fichier CSV
df.to_csv('regions_notes.csv', index=False)

print("Fichier CSV 'regions_notes.csv' créé avec succès.")



# Charger le ficheir
# Demander à l'utilisateur une commande :
#  - moyenne : demande une région et affiche la moyenne de la région
#  - max : demand 