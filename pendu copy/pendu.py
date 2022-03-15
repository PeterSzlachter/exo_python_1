import random

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #ppyYELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def show(tab):
    print(" ".join(tab))

def check_error(user_choice):
    while len(user_choice) != 1 or not user_choice.isalpha():
        print("N'essaye pas de hacker le game, rentre une seule lettre, merci")
        user_choice = input("Tapez une lettre : ")

# début du programme :

dico = ["oignon","poney","cacatohes","banane","pantoufle","cacochyme","xylophone","cucurbitace","phagocyte","grillage","ultracrepidarianisme","formateur","detrusor","souris","balai","lapsus","potiron"]
# solution = random.choice(dico).lower()
solution = "pétit-cul"
tab = []
erreur = 0

for l in range(len(solution)): # on rempli tab de "_" a la bonne taille "-" si c'est un mot composé
    if solution[l] == "-":
        tab.append("-")
    else:
        tab.append("_")

print(f"{bcolors.WARNING}Bienvenue à vous hardcore g@merz dans le jeu de survie le plus hardu de 2032{bcolors.RESET}")
while erreur < 8:

    index = 0
    user_choice = input("Tapez une lettre : ").lower() # en lower pour éviter les conflits avec la casse
    
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
    print(f"{bcolors.OK}Bravo c'est une victoire amplement méritée{bcolors.RESET}") 
else:
    print(f"""
      {bcolors.FAIL}YOU DIED
    ==========Y= 
    ||/       |  
    ||        0  
    ||       /|\ 
    ||       / \ 
    ||           
    ==============\n{bcolors.RESET}
    Le mot était : {bcolors.OK}{solution}{bcolors.RESET}""") 