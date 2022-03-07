#clé:valeur, clés uniques

d = {"clé" : "valeur"}

print(d["clé"])
print(d.get("clé"))

films = {
    "Le Seigneur des Anneaux" : 12,
    "Harry Potter": 9,
    "Blade Runner": 7.5
}

films["Inglorious Basterd"] = 15
prix = 0

for k in films:
    prix += films.get(k)
    
print(prix)

if "Inglorious Basterd" in films:
    del films["Inglorious Basterd"]

print(films.keys())
print(films.values())

for cle in films:
    print(cle,":",films[cle])
    
print(films.items())

employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

del employes["id03"]
employes["id02"]["age"] = 26
print(employes.get("id01").get("age"))
print(employes)

d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

for key, value in d.items():
    print(key, value)