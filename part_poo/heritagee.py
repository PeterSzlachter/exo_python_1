projets = ["pr_Python", "php", "pr_app"]

class Utilisateur:
    def __init__(self,prenom,nom):
        self.nom = nom
        self.prenom = prenom
    
    def __str__(self):
        return f"Utilisateur {self.prenom} {self.nom}"
    
    def afficher_projets(self):
        for projet in projets:
            print(projet)

class Junior(Utilisateur):
    def __init__(self,prenom,nom):
        Utilisateur.__init__(self,prenom,nom)
        # super().__init__(prenom,nom)
        
    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)
 
pyt = Junior("Pyt", "S")
print(pyt.prenom,pyt.nom)
print(pyt)
pyt.afficher_projets()