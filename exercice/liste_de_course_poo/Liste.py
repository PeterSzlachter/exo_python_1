from dataclasses import dataclass
import json #classes de données depuis Python 3.7
from typing import ClassVar
from pathlib import Path
import logging

CUR_DIR = Path(__file__).resolve().parent
LOGGER = logging.getLogger()

@dataclass
class Liste(list):
    name_list: str
     
    def ajouter(self, item):
        if not isinstance(item,str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères !")
        
        if item in self:
            LOGGER.error(f"{item} est déjà dans la liste ")
            return False
                    
        self.append(str(item))
        return True
        
    def supprimer(self, item):
        if item in self:
            self.remove(item)
            return True 
        else:
            LOGGER.error(f"{item} n'est pas dans la liste ")
            print(f"{item} not found")
            return False
        
    def afficher(self):
        print("Ma liste de course :")
        for item in self:
            print(f" - {item}")
        
    def sauvegarder(self):
        chemin = CUR_DIR / f"liste_{self.name_list}"
        
        with open(chemin/".json", 'w') as f:
            json.dump(self , f , indent=4)
            
        return True
if __name__ == '__main__':    
    l = Liste("courses")

    l.ajouter("Nounours")
    l.ajouter("Nounours")
    l.ajouter("Nounours")
    l.ajouter("Nounours")
    l.supprimer("Nounours")
    l.afficher()
    l.sauvegarder()

           