import random

def show(tab):
    print(" ".join(tab))

def check_error(user_choice):
    while len(user_choice) != 1 or not user_choice.isalpha():
        print("N'essaye pas de hacker le game, rentre une seule lettre, merci")
        user_choice = input("Tapez une lettre : ")

def robot_check_len(dico, solution):
    dico_robot = []
    for word in dico:
        if len(word) == len(solution):
            dico_robot.append(word)
    return dico_robot

def robot_check_lettre(dico_robot, tab):
    index = 0
    for word in dico_robot:
        for lettre in word:
            if lettre == tab[index]:
                pass
            index += 1

# début du programme :

dico = ["oignon","poney","cacatohes","banane","pantoufle","cacochyme","xylophone","cucurbitace","phagocyte","grillage","ultracrepidarianisme","formateur","detrusor","souris","balai","lapsus","potiron"]
solution = random.choice(dico)
dico_robot = robot_check_len(dico, solution) # on récupère les mots de même taille que la solution dans le dictionnaire
tab = []
erreur = 0
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for l in range(len(solution)): # on rempli tab de "_" a la bonne taille
    tab.append("_")

print(f"{bcolors.WARNING}Bienvenue à vous hardcore g@merz dans le jeu de survie le plus hardu de 2032{bcolors.RESET}")
while erreur < 8:

    index = 0
    user_choice = input("Tapez une lettre : ").lower() # en lower pour éviter les conflits avec la casse
    robot_choice = dico_robot[0]

    check_error(user_choice)

    if solution.find(user_choice) == -1: # si la lettre n'est pas présente, le compteur d'erreur +1
        erreur += 1

    else:
        for l in solution:
            if l == user_choice:
                tab[index] = l
            index += 1

    show(tab)
    if solution == "".join(tab): # si les deux mots sont les memes, on a gagné > on arrête
        break


if erreur < 8:
    print(f"Bravo c'est une victoire amplement méritée") 
else:
    print(f"""
      YOU DIED
    ==========Y= 
    ||/       |  
    ||        0  
    ||       /|\ 
    ||       / \ 
    ||           
    ==============\n
    Le mot était : {solution}""")