import re

chaine1 = "Une histoire, je ne sais pas moi, il est important d'avoir les bons reflexes et l'expérience adéquate"
chaine2 = "Une histoire, je ne sais pas moi, il faut avoir les bons reflexes et l'expérience adéquate"

pattern = "important"

if re.search(pattern,chaine1):
    print("chaine1 match "+pattern)

if not re.search(pattern,chaine2):
    print("chaine2 ne match pas "+pattern)

chaine1 = "ça coute 10€"
chaine2 = "les 10 coutent 20$"
chaine3 = "les 10 coutent 10$"
chaine4 = "20$ pour les 10"

pattern = "10."
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))

print("Chaines qui commencent par l")
pattern = '^l'
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))


print("Chaines qui finissent par $")
pattern = '\$$'
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))

print("Chaines vides")
chaine1 = ""
chaine2 = " "
chaine3 = "blabla"

pattern = "^$"
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))


print("Correspondance de chaine complète")
chaine1 = "Une histoire, je ne sais pas moi, il est important d'avoir les bons reflexes et l'expérience adéquate"
chaine2 = "Une histoire, je ne sais pas moi, il faut avoir les bons reflexes et l'expérience adéquate"
chaine3 = "important"

pattern = "^important$"
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))


print("[]")
chaine1 = "15"
chaine2 = "26"
chaine3 = "155"
chaine4 = "1"

pattern = "^[0-9][0-9]$"
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))


print("[] avec les prix (| pour les ou)")
chaine1 = "ça coute 10€"
chaine2 = "les 10 coutent 20$"
chaine3 = "les 10l coutent 100$"
chaine4 = "20$ pour les 10"

pattern = "([^0-9][0-9][0-9][\$\€])|(^[0-9][0-9][\$\€])"
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))

print("Majuscule 1")
chaine1 = "Un"
chaine2 = "Eins"
chaine3 = "eins"
chaine4 = "Premier"

pattern = "^[A-Z]"
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))

print("Majuscule 2: trouver les chaines qui contiennent au moins un mot qui ne commence pas par une majuscule")

chaine1 = "Un Deux Trois"
chaine2 = "Eins Zwei DreI"
chaine3 = "Eins zwei Drei"
chaine4 = "eins Zwei Drei"
chaine5 = "Premier Deuxième Troisième"
chaine6 = "a b"

pattern = "(^[a-z])|( [a-z])"
pattern = "(^| )[a-z]"
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))
print(re.search(pattern,chaine5))
print(re.search(pattern,chaine6))

print("Une majuscule suivi d'uniquement des lettres minuscules, au moins une")
chaine1 = "Troissss"
chaine2 = "DreI"
chaine3 = "Zweis"
chaine4 = "eins"
chaine5 = "P"
chaine6 = "a"

pattern = "^[A-Z][a-z]+$"
pattern = "^[A-Z][a-z]{3}$"  # exactement 3 caractères
pattern = "^[A-Z][a-z]{3,7}$"  # de 3 à 7 caractères
pattern = "^[A-Z][a-z]{3,}$"  # 3 caractères ou plus
pattern = "^[A-Z][a-z]{0,3}$"  # de 0 à 3 caractères
pattern = "^[A-Z][a-z]{,3}$"  # de 0 à 3 caractères
pattern = "^[A-Z][a-z]{,}$"  # 0 ou une succession quelconque de caractères
pattern = "^[A-Z][a-z]*$"  # 0 ou une succession quelconque de caractères
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))
print(re.search(pattern,chaine5))
print(re.search(pattern,chaine6))


print("Que des mots qui commencent par une majuscule")
chaine1 = "Un Deux Trois"
chaine2 = "Eins Zwei DreI"
chaine3 = "Eins zwei Drei"
chaine4 = "eins Zwei Drei"
chaine5 = "Premier Deuxième Troisième Quatrième Cinquième"
chaine6 = "a b"

pattern = "^((^| )[A-Z][a-zàéèêâîï¨ë]*)+$"
print(re.search(pattern,chaine1))
print(re.search(pattern,chaine2))
print(re.search(pattern,chaine3))
print(re.search(pattern,chaine4))
print(re.search(pattern,chaine5))
print(re.search(pattern,chaine6))



print("Validation d'email")
valides = [
    "toto@example.com",
    "prenom.nom@exemple.com",
    "prenom.nom@sous.domaine.exemple.com",
    "prenom-nom_surnom@sous.domaine.exemple.com",
    "prenom-nom_surnom@sous-domaine.exemple.com"
]
invalides = [
    "prenom-nom_surnom@bug@domaine.exemple.com",
    "toto@exemple",
    "@exemple.com",
    "toto@"
]
pattern = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-z]+$"
for i in valides:
    if re.search(pattern,i):
        print(i+": OK")
    else:
        print("Erreur de validation sur "+i)
for i in invalides:
    if not re.search(pattern,i):
        print(i+": OK")
    else:
        print("Erreur d'invalidation sur "+i)
        


# Substitutions
chaine1 = "Bonjour toto"
pattern = "toto"

print(re.sub(pattern,"Jack",chaine1))



print("Sub avec ()")
chaine1 = "Bonjour Toto comment vas tu ?"
pattern = "(.)([A-Z][a-zA-Z]+)"

print(re.sub(pattern,r"\1<\2>",chaine1))



chaine1 = "L'email de l'utilsateur est toto@gmail.com"
pattern = "(\s|^)[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-z]+(\s|$)"
replacement = "<masked email>"
print(re.search(pattern,chaine1))
print(re.sub(pattern,replacement,chaine1))




chaine = "1:31:44.742"
pattern = "(\d+):(\d+):(\d+)\.(\d+)"

heures = re.sub(pattern,r"\1",chaine)
heures = int(re.search(pattern,chaine).group(1))
minutes = int(re.search(pattern,chaine).group(2))
secondes = int(re.search(pattern,chaine).group(3))
milisecondes = int(re.search(pattern,chaine).group(4))
total = milisecondes + secondes * 1000 + minutes * 60000 + heures * 3600000
print(total)