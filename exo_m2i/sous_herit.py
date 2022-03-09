# A partir de l'exemple en PJ :
# Creer une classe objet qui contiendra les attributs / accesseurs pour :
# value
# weight

# Creer une classe qui en herite et qui definit les armes
# Creer des sous classe handweapons qui herite de l'arme:
# axe / sword / katana / shuriken / hummer / scythe
# Creer une sous classe distantweapons
# bow / crossbow / javelin
# Poitions
# LSD (augemente la vitesse de 5)
# mana (mana += 10 ) / vie (redonne la vie +10)
# full life / full mana
# Armure
# avec attributs aux choix selon vos envies.
# Les armes de poing possede les attributs : puissance (max 50) / duree de vie (max 50)
# Les armes a distance possedes les attributs suivants : puissance  (max 20 ) / duree de vie (max 100) / distance (max 100)

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

class weapons(myobject):    
    def __init__(self, power, durability):
        self.power=power
        self.durability=durability

class handweapons(weapons):
    def __init__(self):
        pass

class distantweapons(weapons):
    
    kind = ["axe" , "sword" , "katana" , "shuriken" , "hummer" , "scythe"]
    def __init__(self, shot_range):
        self.shot_range=shot_range
        pass
    
class potion(myobject):
    type_potion = ["Heal", "Mana", "LSD"]
    def __init__(self):
        pass