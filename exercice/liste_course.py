liste = ["Pomme", "Radis"]
choice = 0

while choice != "5" :
    print("""
        Choisissez parmi les 5 options suivantes :
        1: Ajouter un élément à la liste
        2: Retirer un élément de la liste
        3: Afficher la liste
        4: Vider la liste
        5: Quitter
        __________________________""")

    choice = input("👉 Votre Choix : ")
    
    if choice == "1" :
        element = input("Entrer le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(element.capitalize())
        print(f"L'élément {element.capitalize()} a bien été ajouté à la liste")
    elif choice == "2" :
        print("Voici le contenu de votre liste de course : ")
        for i, element in enumerate(liste,1):
            print(f"{i}. {element}")
        element = input("Quel élément retirer de la liste ? ").capitalize()
        if element in liste :
            liste.remove(element.capitalize())
            print(f"L'élément {element} n'est pas la liste.")
        else :
            print(f"{element} n'est pas dans la liste")
    elif choice == "3" :
        print("Voici le contenu de votre liste de course : ")
        for i, element in enumerate(liste,1):
            print(f"{i}. {element}")
    elif choice == "4" :
        liste.clear()
        if len(liste) == 0 :
            print("La liste a été vidée de son contenu")
    elif choice == "5" :
        break
    
print("Fin du programme")