from pathlib import Path

dirs = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents"
}

tri_dir = Path(__file__).parent / "data" #repertoire à trier

files = [f for f in tri_dir.iterdir() if f.is_file()] # Liste fichier à trier (liste de WindowPath)

for f in files: #boucle de tri
    output_dir = tri_dir / dirs.get(f.suffix, "Autres") #nom des répertoires où seront placés les fichiers
    output_dir.mkdir(exist_ok=True) #création des répertoires si non existant
    f.rename(output_dir / f.name) #déplace le fichier

# tri_dir.rename(tri_dir.parent / "data_sorted")

# print(tri_dir.name)


