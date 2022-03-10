from pathlib import Path
import json

chemin = Path(__file__).parent / "dico.json"

dick = ["oignon","poney","cacatohes","banane","pantoufle","cacochyme","xylophone","cucurbitace","phagocyte","grillage","ultracrepidarianisme" ,"formateur","detrusor","souris","balai","lapsus","potiron","python","phallange","vis-a-vis","marteau-piqueur","frein-moteur","asperge","cornichon"]

with open(chemin, "w", encoding="utf-8") as f:
    json.dump(dick, f, indent=4)

with open(chemin, "r", encoding="utf-8") as f:
    content = json.load(f)

print(content)