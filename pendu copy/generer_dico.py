from pathlib import Path
import json

chemin = Path(__file__).parent / "dico.txt"

with open(chemin, "r", encoding="utf-8") as f:
    dick = json.load(f)

i= 0

# while i < 5:
#     creation = input("Entrez un mot qui va s'ajouter à notre super dico\n")
#     dick.append(creation)
#     i += 1
    
with open(chemin, "w", encoding="utf-8") as f:
    json.dump(dick, f, indent=4)
    


print(dick)