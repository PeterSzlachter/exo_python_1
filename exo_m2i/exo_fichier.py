from pathlib import Path

chemin = Path(__file__).parent / "fichierfourni.csv"
target = Path(__file__).parent / "moyenne.csv"

print(chemin)
dict = {}
datas = []
result = []
moyenne = 0

with open(chemin,"r",encoding="utf8") as f:
    contenu = f.read().splitlines()
print(contenu)
    
for line in contenu[1:]:
    prenom = (line.split(",")[1]).capitalize()
    nom = (line.split(",")[0]).capitalize()
    age = line.split(",")[2]
    moyenne = (float(line.split(",")[3]) + float(line.split(",")[-1]))/2
    moyenne = round(moyenne,3)
    result.append(f"{age} ans,{nom},{prenom},{moyenne}/20")

with open(target,"w",encoding="utf8") as f:
    f.write("\n".join(result))

# for i in range(1,len(datas)):
#     for e in datas[i]:
#         e = e.capitalize()
# print(datas)
    
# A partir du fichier fourni, calculer les moyennes. Le resultats attendus est un fichier csv (moyennes.csv qui contient :
# Age,Prenom,Nom,Moyenne
# Le prenom et le nom devront TOUJOURS etre "premiere lettre majuscule puis le reste en minuscule" Ex: Thibaut Salut
# la moyenne sera avec 3 chiffres apres la virgule