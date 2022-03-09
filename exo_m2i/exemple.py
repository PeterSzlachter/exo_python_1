
# Definition de la classe
class bonhomme:
    # Definition du constructeur
    def __init__(self):
        self.name="je suis un super bonhomme"
        self.strenght=0
    # Definition d'un destructeur
    def __del__(self):
        self.name="mon nom est personne"
        self.strenght=0

    # Definition d'un accesseur de force
    def setstrenght(self, value):
        self.strengt=value
    def getstrenght(self):
        return self.strengt


# Instanciation de l'objet
# mybonhomme = bonhomme()
# mybonhomme.setstrenght(69)
# print(mybonhomme.getstrenght())

# Realiser une classe personnage qui contient les attributs suivants :
# Nom
# Type de personnage ( necromancien / personne de petite taille / barbare / elfe)
# Sexe (M ou F)
# vitesse de deplacement (allant de 1 a 5)
# force (allant de 1 a 69)
# intelligence (allant de 1 a 69)
# armure (allant de 1 a 51)
# agilite (allant de 1 a 69)
# esquive (allant de 1 a 69)

# Regle du jeu. Chaque classe de personnage une fois instanciee possede des attributs par defaut :
# necromancien  => v = 2 / f = 10 / i = 30 / ar = 20 / ag = 20 / es = 40
# personne de petite taille => v = 2 / f = 30 / i = 15 / ar = 30 / ag = 10 / es = 30
# barbare => v = 2 / f = 40 / i = 10 / ar = 30 / ag = 20 / es = 20
# elfe => v= 4 / f = 20 / i = 20 / ar = 20 / ag = 20 / es = 20
# Le sexe ajoutera comme attributs : Si M force = +5 si F intelligence = +5

# TODO : Realiser les constructeur et destructeur de chaque personnage ainsi que les accesseurs de chaque attributs.