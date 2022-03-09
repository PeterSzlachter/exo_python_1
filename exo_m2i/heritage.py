#!/usr/bin/env python3

class myobject:
    def __init__(self):
        self.value=0
        self.weight=0

    def setvalue(self, value):
        self.value=value
    def getvalue(self):
        return (self.value)

    def setweight(self, weight):
        self.weight=weight
    def getweight(self):
        return (self.weight)

# Ici la classe qui herite de la classe objet possede "de base" 
# tous les attributs et les methodes de la classe dont elle herite
class sword(myobject):
    def __init__(self):
        self.damage=0
    def setdamage(self, damage):
        self.damage=damage
    def getdamage(self):
        return (self.damage)


mysword=sword()
mysword.setvalue(10)
mysword.setweight(50)
mysword.setdamage(20)

print(mysword.getvalue())
print(mysword.getweight())
print(mysword.getdamage())

