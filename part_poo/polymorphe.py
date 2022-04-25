class Vehicule:
    def avance(self):
        print("Le véhicule démarre")
        
class Voiture(Vehicule):
    def avance(self):
        super().avance() #on augmente la méthode
        print("La voiture roule")
        
class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("l'avion vol")
        
v = Voiture()
a = Avion()

a.avance()
v.avance()