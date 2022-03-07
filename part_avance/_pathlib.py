#os, shutil, glob -> utilisation de string
from pathlib import Path
# import shutil

print(Path.home())
print(Path.cwd())

chemin = Path(Path.cwd()/"exo_python_1/part_avance/DossierTest/sousdossiertest")
# print(dir(chemin))
print(chemin/"truc")
print(chemin.joinpath("main.py"))
print(chemin.joinpath("main.py").suffix)

p = Path("exo_python_1/part_avance/index.html")
print(p.name,p.stem,p.suffix,p.parent,p.suffixes,p.parts,p.exists(),p.is_dir(),p.is_file())

chemin.mkdir(exist_ok=True,parents=True)

f = chemin / "test.py"
f.touch()
f.write_text("print(\"Hello Test\")")
print(f.read_text())
# f.unlink()

# shutil.rmtree(chemin.parent)

for e in Path.cwd().iterdir():
    print(e.name)

liste = [t for t in Path.cwd().iterdir() if t.is_dir()]
print(liste)

dl = Path.home() / "downloads"

# for j in dl.glob("*.rdp"): #scan les fichier finissant par .rdp
#     j.unlink() #supprime toutes les itérations

for i in range(10):
    (f.parent / (f.stem + f"_0{i}" + f.suffix)).touch()
    
for k in f.parent.glob("test*"):
    k.unlink()

# p.unlink()
chemin.rmdir()
chemin.parent.rmdir()

