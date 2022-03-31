from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Voiture:
    essence: int = 100
    nombre_de_trajet: ClassVar[int] = 0
    
    def afficher_reservoir(self):
        return print(f"La voiture contient {self.essence} litres d'essence")
    def compteur_trajet(self):
        Voiture.nombre_de_trajet += 1
        print(f"Vous avez fait {Voiture.nombre_de_trajet} trajets")
    
    def roule(self,km):
        essence_necessaire = (km*5) / 100
        print(essence_necessaire)
        self.essence -= essence_necessaire
        
        if self.essence <= 0:
            self.essence = 0
            self.afficher_reservoir()
            print("Vous n'avez plus assez d'essence")
        elif self.essence > 0 and self.essence <= 10:
            self.afficher_reservoir()
            self.compteur_trajet()
            print("Vous n'avez bientôt plus d'essence")
        else:
            self.compteur_trajet()
            self.afficher_reservoir()
        
            
    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir")
        
vet = Voiture()
while vet.essence != 0:
    vet.roule(25)
    