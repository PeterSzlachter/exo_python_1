# Trier une liste de noms dans un fichier texte

from pathlib import Path

#chemin du fichier à trier
target_file = Path(__file__).parent / "prenoms.txt"
#chemin du fichier triés
final_file = Path(__file__).parent / "prenoms_tries.txt"

#On recupère les valeurs du fichier texte chaque ligne par index
content_file = target_file.read_text(encoding='utf-8').splitlines()

# with open(target_file, "r", encoding="utf-8") as f :
#     data = f.read().splitlines()

prenoms = []

#on itere sur chaque ligne on place chaque prénom dans un nouveau tableau
for line in content_file:
    prenoms.extend(line.split())

#on nettoie le tableau prénom 
prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

#on écrit le tableau dans le nouveau fichier en ajoutant des saut de ligne et en classant les prénoms
final_file.write_text("\n".join(sorted(prenoms_final)), encoding='utf-8')


# with open(Path(__file__).parent / "fichier_final.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(sorted(prenoms_final)))