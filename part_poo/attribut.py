class Voiture: #convention majuscule
    couleur = "Bleu" #attribut de classe
    voitures_crees = 0
    def __init__(self, marque):
        Voiture.voitures_crees += 1
        self.marque = marque #attribut d'instance
    def afficher_marque(self): #methode
        print(f"La voiture est une {self.marque}")
    
    
a_110 = Voiture("Alpine") #une instance
mustang = Voiture("Ford")


a_110.couleur = "Rouge"
Voiture.couleur = "Violet" #attribut d'instances

# print(Voiture.marque)
# print(Voiture.couleur)
print(a_110.marque)
print(a_110.couleur)
print(Voiture.voitures_crees)
a_110.afficher_marque()
Voiture.afficher_marque(mustang)