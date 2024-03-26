file = open("regions_notes.csv")
lines = file.readlines()
file.close()

data = {}
for line in lines:
    [region, note] = line.split(",")
    try:
        region = int(region)
        note = int(note)
        if not region in data:
            data[region] = [note]
        else:
            data[region].append(note)
    except ValueError:
        # Do nothing, ignore lines that are not numbers
        pass

print(data)


def int_input(msg):
    value = None
    while value == None:
        try:
            value = int(input(msg))
        except ValueError:
            print("Taper un entier")
    return value
        
def moyenne():
    region = int_input("Quelle région ? ")
    if not region in data:
        print("Pas de notes pour cette région")
    else:
        moyenne = sum(data[region])/len(data[region])
        print(moyenne)


def somme():
    region = input("Quelle région ? ")
    region = int(region)
    if not region in data:
        print("Pas de notes pour cette région")
    else:
        moyenne = sum(data[region])
        print(moyenne)

def quit():
    exit()



commands = {
    "moyenne": moyenne,
    "sum" : somme,
    "quit": quit
}


while True:
    print("Quelle information souhaitez vous avoir ?")
    print("  - moyenne")
    print("  - max")
    command = input("> ")
    if command in commands: commands[command]()
    else: print("commande inconnue")
