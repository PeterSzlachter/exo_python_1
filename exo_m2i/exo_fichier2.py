from pathlib import Path

fichier = Path(__file__).parent / "fichier_a.txt"
counter = 0
voyelle = ["a","e","i","o","u","y"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
intrus = [".","-",",","*","(",")",":","/"]

with open(fichier, 'r', encoding='utf-8') as f: 
    content = f.read().lower()
    texte = content.splitlines()
    
count_voyelle = sum(content.count(e) for e in voyelle)
count_letter = sum(content.count(e) for e in alphabet)

print("Nombre de voyelle :", count_voyelle)    
print("Nombre de lettre :", count_letter)
 
texte_clean = []
for line in texte:
    for mot in line.split(" "):
        for char in intrus:
            mot = mot.replace(char,"")
        if mot.isalpha():
            texte_clean.append(mot)

print("Nombre de mot dans le texte :",len(texte_clean))

for char in alphabet:
    counter = content.count(char)
    print(f"Nombre de {char} dans le texte : {counter}")
    counter = 0
    
texte_clean.sort()    

unique_texte_clean = []
for e in texte_clean:
    if e not in unique_texte_clean:
        unique_texte_clean.append(e)

counter = 0
for word in unique_texte_clean:
    counter = content.count(word)
    print(f"Nombre de {word} dans le texte : {counter}")
    
# Ouvrir le fichier en piece jointe et et afficher :
# Le nombre de mots global dans le fichier
# Le nombre de lettre global dans le fichier
# Le nombre de consonne et de voyelles (for toto in ('a','e','i','o','u','y') )
# Pour chaque lettre PRESENTE dans le fichier -> Le nombre d'iteration de la lettre
# Pour chaque mot PRESENT dans le fichier -> Le nombre d'iteration du mot (trie par ordre alphbetique)
# Exemple :
# Le fichier contient 1022 mots et 5930 lettres
# Nombre de voyelles: 1882 nombre de consonnes 4048
# Lettres:
# a: 194
# b : 19
# c: 28
# ...
# v: 18
# Mots:
# a: 21
# choucroute: 17
# le: 99
# voiture: 11
# ...