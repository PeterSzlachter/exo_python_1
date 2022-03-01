import json

chemin = "C:/Users/pszlachter/Desktop/tuto_python/fichier.json"

with open(chemin, "w", encoding="utf-8") as f:
    json.dump(list(range(10)), f, indent=4)

with open(chemin, "r", encoding="utf-8") as f:
    liste = json.load(f)
    print(type(liste))
    
with open(chemin, "r", encoding="utf-8") as f:
    donnees = json.load(f) #recuperer les données
    print(donnees)

donnees.append(10) #modifier les données
donnees.append("Pêche")

with open(chemin, "w", encoding="utf-8") as f: #ecraser les données en rajoutant les modifs
    json.dump(donnees, f, indent=4, ensure_ascii=False)