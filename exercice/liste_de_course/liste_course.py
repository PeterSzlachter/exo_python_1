import sys,os,json

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre Choix : """

MENU_CHOICES = ["1","2","3","4","5"]

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH  = os.path.join(CUR_DIR,"liste.json")
print(LISTE_PATH)

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f :
        LISTE = json.load(f)
else:
    LISTE = []

def affichage_liste(liste):
    if liste:
        print("Voici le contenu de votre liste de course : ")
        for i, element in enumerate(liste,1):
            print(f"{i}. {element}")
    else:
        print("Votre liste est vide")

while True :
    
    user_choice = input(MENU)
    
    if user_choice not in MENU_CHOICES:
        print("Choisir une option valide !")
        
    if user_choice == "1" :
        element = input("Entrer le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(element.capitalize())
        print(f"L'élément {element.capitalize()} a bien été ajouté à la liste")
            
    elif user_choice == "2" :
        affichage_liste(LISTE)
        element = input("Quel élément retirer de la liste ? ").capitalize()
        if element in LISTE :
            LISTE.remove(element.capitalize())
            print(f"L'élément {element} a été supprimé.")
        else :
            print(f"{element} n'est pas dans la liste")
                
    elif user_choice == "3" :
        affichage_liste(LISTE)
                    
    elif user_choice == "4" :
        LISTE.clear()
        if len(LISTE) == 0 :
            print("La liste a été vidée de son contenu")
                
    elif user_choice == "5" :
        with open(LISTE_PATH,"w") as f:
            json.dump(LISTE, f, indent=4)
        print("Fin du programme : Votre liste a été sauvegardé 📜")
        sys.exit()