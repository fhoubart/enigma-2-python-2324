import pandas as pd


print("Exercice 1")
# Read data from csv
df = pd.read_csv("./fr-en-ecoles-effectifs-nb_classes.csv", sep=";")
# shape of dataset
print("Shape (nb lines, nb columns): ",df.shape)
#  statistics
print(df.describe())

print("Exercice 2")
print("Les effectifs moyens au global sont :")
print("CP  :" , df['nombre_eleves_cp_hors_ulis'].mean())
print("CE1 :" , df['nombre_eleves_ce1_hors_ulis'].mean())
print("CE2 :" , df['nombre_eleves_ce2_hors_ulis'].mean())
print("CM1 :" , df['nombre_eleves_cm1_hors_ulis'].mean())
print("CM2 :" , df['nombre_eleves_cm2_hors_ulis'].mean())

print("Exercice 3")
print(df.groupby('academie')[[
    'nombre_eleves_cp_hors_ulis',
    'nombre_eleves_ce1_hors_ulis',
    'nombre_eleves_ce2_hors_ulis',
    'nombre_eleves_cm1_hors_ulis',
    'nombre_eleves_cm2_hors_ulis']].mean().sort_values('nombre_eleves_cp_hors_ulis'))


import matplotlib.pyplot as plt

print("Exercice 4")
filtered = df[df['numero_ecole']=="0030701W"]
print(filtered)
plt.plot(filtered["rentree_scolaire"],filtered["nombre_eleves_cp_hors_ulis"], label="CP")
plt.plot(filtered["rentree_scolaire"],filtered["nombre_eleves_ce1_hors_ulis"], label="CE1")
plt.plot(filtered["rentree_scolaire"],filtered["nombre_eleves_ce2_hors_ulis"], label="CE2")
plt.xlabel('Année')
plt.ylabel('Effectif')
plt.title('Effectifs')
plt.legend(loc='upper left')  # Position de la légende
plt.show()

# scikit-learn
# pytorch


# collab.research.google.com