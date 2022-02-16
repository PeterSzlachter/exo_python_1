from genericpath import exists
import os
import random
from pprint import pprint

chemin = "C:/Users/peter/desktop/Python_tuto"

dossier = os.path.join(chemin, "dossier", "test")

if not os.path.exists(dossier) :
    os.makedirs(dossier,exist_ok=True)

if os.path.exists(dossier):
    os.removedirs(dossier)

print(dossier)
# print(dir(os))
# pprint(dir(random))
# print(help(random.gauss))
print(callable(pprint))
print(callable(os.putenv))
# pprint(dir(os))
print(os.name)
