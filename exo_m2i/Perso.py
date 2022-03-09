class Personnage :
    
    classe = ["Necromancien", "Petit", "Barbare", "Elfe"]
    
    perso_stat = {"Type": "",
                  "Pseudo": "",
                  "Sexe": "",
                  "Speed": 0,
                  "Force": 0,
                  "Intelligence": 0,
                  "Armure": 0,
                  "Agilite":0,
                  "Esquive": 0}
    
    def __init__(self,name,sexe,type):
        if type in self.classe:
            if type == "Necromancien":
                self.perso_stat["Type"] = "Necromancien"
                self.perso_stat["Pseudo"] = name
                self.perso_stat["Sexe"] = sexe
                self.perso_stat["Speed"] = 15
                self.perso_stat["Force"] = 10
                self.perso_stat["Intelligence"] = 50
                self.perso_stat["Armure"] = 50
                self.perso_stat["Agilite"] = 50
                self.perso_stat["Esquive"] = 50
            elif type == "Petit":
                self.perso_stat["Type"] = "Petit"
                self.perso_stat["Pseudo"] = name
                self.perso_stat["Sexe"] = sexe
                self.perso_stat["Speed"] = 25     
                self.perso_stat["Force"] = 10
                self.perso_stat["Intelligence"] = 50
                self.perso_stat["Armure"] = 30
                self.perso_stat["Agilite"] = 60
                self.perso_stat["Esquive"] = 50
            elif type == "Barbare":
                self.perso_stat["Type"] = "Barbare"
                self.perso_stat["Pseudo"] = name
                self.perso_stat["Sexe"] = sexe
                self.perso_stat["Speed"] = 15
                self.perso_stat["Force"] = 10
                self.perso_stat["Intelligence"] = 5
                self.perso_stat["Armure"] = 50
                self.perso_stat["Agilite"] = 10
                self.perso_stat["Esquive"] = 50
            elif type == "Elfe":
                self.perso_stat["Type"] = "Necromancien"
                self.perso_stat["Pseudo"] = name
                self.perso_stat["Sexe"] = sexe
                self.perso_stat["Speed"] = 30
                self.perso_stat["Force"] = 10
                self.perso_stat["Intelligence"] = 50
                self.perso_stat["Armure"] = 15
                self.perso_stat["Agilite"] = 50
                self.perso_stat["Esquive"] = 50
        else :
            print(f"Enter une classe valide parmis : {self.classe}")
        
    def settype(self,type):
        self.type = type
    
    def gettype(self):
        return self.type

pyt = Personnage("Pyt","M","Barbare")
pyt.settype("Barbare")

for stat in pyt.perso_stat:
    print(f"{stat} : {pyt.perso_stat[stat]}")