import matplotlib.pyplot as plt

print("Exercice 1")
# Données
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Graphique
plt.plot(x, y)

# Ajout de titres et d'étiquettes
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.title('Graphique basique')

# Affichage du graphique
plt.show()


tab = []
for i in y:
    tab.append(i+1)

print("Exercice 2")
# Graphique avec deux lignes
plt.plot(x, y, label='Ligne 1', color='blue', linestyle='solid')  # Ligne bleue pleine
plt.plot(x, [i+1 for i in y], label='Ligne 2', color='red', linestyle='dashed')  # Ligne rouge en pointillés

# Ajout de titres et d'étiquettes
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.title('Graphique personnalisé')
plt.legend(loc='upper left')  # Position de la légende

# Affichage du graphique
plt.show()



print("Exercice 3")
pays = ['USA', 'Chine', 'Inde', 'Russie', 'Japon']
population = [328, 1439, 1380, 146, 126]
# Diagramme à barres
plt.bar(pays, population, color='skyblue')

# Ajout de titres et d'étiquettes
plt.xlabel('Pays')
plt.ylabel('Population (en millions)')
plt.title('Population par pays')
plt.xticks(rotation=45)  # Rotation des étiquettes pour éviter le chevauchement

# Affichage du graphique
plt.show()



print("Exerice 4")
navigateurs = ['Chrome', 'Firefox', 'Edge', 'Safari', 'Autres']
parts = [650, 100, 80, 120, 50]  # Pourcentages
# Diagramme circulaire
explode = (0.1, 0, 0, 0, 0)  # Sépare "Chrome"
plt.pie(parts, labels=navigateurs, explode=explode, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'yellow'])

# Ajout de titre
plt.title('Parts de marché des navigateurs web')

# Affichage du graphique
plt.show()



print("Exercice 5")
# Données
maths = [70, 85, 60, 90, 55, 75]
physique = [60, 95, 70, 80, 45, 85]
noms = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

plt.scatter(maths,physique)
plt.plot(maths, physique, 'r--', label='Régression linéaire')

# Ajout des noms aux points
for nom, x, y in zip(noms, maths, physique):
    plt.text(x, y, nom, fontsize=8, ha='right')

# Ajout de titres et d'étiquettes
plt.xlabel('Scores de Mathématiques')
plt.ylabel('Scores de Physique')
plt.title('Scores de Mathématiques vs. Physique')
plt.legend(title='Noms', loc='best', bbox_to_anchor=(1, 1))

# Affichage du graphique
plt.show()
