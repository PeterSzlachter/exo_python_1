from pathlib import Path

CUR_DIR = Path(__file__).parent

fichier = CUR_DIR / input("Entrer le nom du fichier à ouvrir : ")

try:
    print(fichier.read_text())

except UnicodeDecodeError as e:
    print("Erreur :",e)
except FileNotFoundError as e:
    print("Erreur :",e)