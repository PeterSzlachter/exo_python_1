# Créer une classe pour instancier des monstres :
# - Squelette
# - Orc
# - Gobelin

# Les monstres auront les caractéristiques :
# PV
# Degats
# Armure
# Esquive

# Squelette -> 50 PV, 15 degats, 20 armure, 15 esquive
# Orc -> 150 PV, 25 degats, 30 armure, 10 esquive
# Gobelin -> 25 PV, 10 dégâts, 10 armure, 30 esquive

# Les monstres doivent se grouper de manière aléatoire (quantité et type de monstre) de 1 à 4 par groupe a chaque nouveau objet de la classe "monstre"

import random

class monstres :
    
    races = ["Squelette", "Orc", "Gobelin"]
    
    groupe = {}
    
    stats = {}
    
    def __init__(self):
        
        self.nombre_de_monstre = random.randint(1,10)
        
        for i in range(1,(self.nombre_de_monstre)+1):
            self.groupe[i] = self.races[random.randint(0,2)]
            self.stat_monstre(self.groupe[i])
            self.groupe[f"stat_monstre_{i}"] = self.stats
            self.stats = {}
        
    def stat_monstre(self,type):
        
        if type in self.races :
            if type == "Squelette":
                self.stats["PV"] = 50
                self.stats["Degats"] = 15
                self.stats["Armure"] = 20
                self.stats["Esquive"] = 15
            elif type == "Orc":
                self.stats["PV"] = 150
                self.stats["Degats"] = 25
                self.stats["Armure"] = 30
                self.stats["Esquive"] = 10
            elif type == "Gobelin":
                self.stats["PV"] = 25
                self.stats["Degats"] = 10
                self.stats["Armure"] = 10
                self.stats["Esquive"] = 30
        else:
            print("Erreur type de monstre inconnu")
    
    def show_stat(self):
        for m in self.groupe:
            print(f"{m} : {self.groupe[m]}")

mob = monstres()
mob.show_stat()
