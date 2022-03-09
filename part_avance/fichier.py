from pathlib import Path

chemin = r"C:\Users\pszlachter\Desktop\tuto_python"
chemin = "C:\\Users\\pszlachter\\Desktop\\tuto_python"
chemin = "C:/Users/pszlachter/Desktop/tuto_python/fichier.txt"
chemin = Path(__file__).parent / "fichier.txt"
# print(chemin)

# files = open(chemin,"r") #mode read
# # files.seek(10) #position du curseur au 10e char

# print(files)

# files.close()

with open(chemin,"r",encoding="utf8") as f:
    # print(repr(f.read()).replace("\\n", " "))
    contenu = f.readlines()
    # contenu = f.read().splitlines() #sépare les retours à ligne
    print(contenu)

# with open(chemin,"w",encoding="utf8") as f:
#     f.write("Ecrire dans un fichier")

# with open(chemin,"a",encoding="utf8") as f:
#     f.write("\nAjouter après le texte")