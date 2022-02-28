import random

essais = 5
nb_mystere = random.randint(1,100)
compteur = 0

def input_choice():
    return input(f"Devinez le nombre mystère, nombre entier entre 1 et 100 ! Il vous reste {essais} essai(s).")
    
while essais > 0 :
    user_choice = input_choice()
    if not user_choice.isdigit():
        print("Entrer une valeur valide ! Un nombre entier entre 1 et 100")
        continue
    essais -= 1
    compteur += 1
    user_choice = int(user_choice)
    if user_choice < nb_mystere:
        print(f"C'est plus grand ! Il vous reste {essais} essai(s).")
    elif user_choice > nb_mystere:
        print(f"C'est plus petit ! Il vous reste {essais} essai(s).")
    else:
        print(f"Bravo 🥳 ! Vous avez trouvé le nombre mystère en {compteur} essai(s) ")
        break

if user_choice != nb_mystere:
    print("Perdu 😞")
print(f"Fin du programme le nombre mystère était {nb_mystere}")
    