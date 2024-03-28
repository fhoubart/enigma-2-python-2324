file = open("fr-en-ecoles-effectifs-nb_classes.csv")
lines = file.readlines()
file.close()


print("##### Methode 1 #####")
### 1
# {
#    "NORD": [ ['2022','AUVERGNE-ET-RHONE-ALPES', ...], [...], ]
# }

data1 = {}
for line in lines[1:]:
    ecole = line.strip().split(";")
    # ecole = ['2022','AUVERGNE-ET-RHONE-ALPES', ...]
    region = ecole[3]
    if not region in data1: # le secteur n'est pas encore dans le dictionnaire
        data1[region] = []
    data1[region].append(ecole)

print("Infos pour le NORD")
nord = data1["NORD"]
public = 0
prive = 0
sum_cp = 0
total_cp = 0
for ecole in nord:
    if ecole[8] == "PRIVE": prive += 1
    if ecole[8] == "PUBLIC": public += 1
    sum_cp += int(ecole[16])
    total_cp += 1

print(f"ration PUBLIC/PRIVE: {public/prive}")
print(f"moyenne du nombre d'élève en CP: {sum_cp/total_cp}")


print("##### Methode 2 #####")
### 2
# {
#    "NORD": {public: 49, prive: 23, sum_cp: 45, total_cp: 140}
# }

data2 = {}
for line in lines[1:]:
    ecole = line.strip().split(";")
    # ecole = ['2022','AUVERGNE-ET-RHONE-ALPES', ...]
    region = ecole[3]
    if not region in data2: # le secteur n'est pas encore dans le dictionnaire
        data2[region] = {
            "public": 0,
            "prive": 0,
            "sum_cp": 0,
            "total_cp": 0
        }
    if ecole[8] == "PRIVE": data2[region]["prive"] += 1
    if ecole[8] == "PUBLIC": data2[region]["public"] += 1
    data2[region]["sum_cp"] += int(ecole[16])
    data2[region]["total_cp"] += 1
    
print("Infos pour le NORD")
nord = data2["NORD"]
print(f"ration PUBLIC/PRIVE: {nord["public"]/nord["prive"]}")
print(f"moyenne du nombre d'élève en CP: {nord["sum_cp"]/nord["total_cp"]}")
