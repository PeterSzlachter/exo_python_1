import json

fichier = "truc.json"
print(fichier)

with open(fichier, "r") as f:
    settings = json.load(f)

with open(fichier, "w") as f:
    settings["fontSize"] = 15
    json.dump(settings,f, indent=4)


print(settings)