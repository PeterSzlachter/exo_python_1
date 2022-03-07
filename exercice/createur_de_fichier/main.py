from pathlib import Path
 
d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

CUR_DIR = Path(__file__).parent #Emplacement de la création des dossiers

for main_folder, sub_folder in d.items(): #iteration sur les valeurs
    for folder in sub_folder :  #iteration sur les tableaux
        path_dir = CUR_DIR / main_folder / folder #Emplacement/nom des sous dossiers
        path_dir.mkdir(exist_ok=True, parents= True) #création des dossiers et sous-dossiers