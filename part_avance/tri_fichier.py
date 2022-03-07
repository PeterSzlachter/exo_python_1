from pathlib import Path

dirs = {".png": "Images",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".zip": "Archives",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".json": "Documents",
        ".xlsx": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques"
}

tri_dir = Path.home() / "Desktop" / "Document_administratif"
print(tri_dir)
files = [f for f in tri_dir.iterdir() if f.is_file()]
print(files)
for f in files:
    ouput_dir = tri_dir / dirs.get(f.suffix, "Autres")
    print(ouput_dir)
    ouput_dir.mkdir(exist_ok=True)
    f.rename(ouput_dir / f.name)
