import pandas as pd
import numpy as np

# Liste de 70 noms
names = [
    'Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Henry', 'Isabel', 'John',
    'Kate', 'Liam', 'Mia', 'Nathan', 'Olivia', 'Peter', 'Quinn', 'Rachel', 'Samuel', 'Taylor',
    'Uma', 'Victor', 'Wendy', 'Xavier', 'Yvonne', 'Zane', 'Abigail', 'Benjamin', 'Chloe', 'Daniel',
    'Ella', 'Felix', 'Gemma', 'Hannah', 'Ian', 'Jasmine', 'Kevin', 'Luna', 'Matthew', 'Nora',
    'Oscar', 'Penny', 'Quincy', 'Riley', 'Sofia', 'Toby', 'Una', 'Violet', 'Willow', 'Xander',
    'Yara', 'Zara', 'Alex', 'Bella', 'Caleb', 'Diana', 'Ethan', 'Fiona', 'Gavin', 'Hazel',
    'Ivy', 'Jack', 'Kylie', 'Leo', 'Mila', 'Nolan', 'Olive', 'Parker', 'Quinn', 'Rory'
]

# Générer des données aléatoires pour 1000 étudiants
np.random.seed(0)
data = {
    'Name': np.random.choice(names, 1000),
    'Gender': np.random.choice(['Female', 'Male'], 1000),
    'Grade': np.random.randint(60, 101, 1000)  # Générer 1000 notes aléatoires entre 60 et 100 inclus
}

# Créer le DataFrame
df = pd.DataFrame(data)

# Enregistrer le DataFrame dans un fichier CSV
df.to_csv('students.csv', index=False)

print("Fichier students.csv généré avec succès!")
