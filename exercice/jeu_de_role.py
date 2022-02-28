# 2 joueurs (vous et un ennemi) 50 points de vie, 3 potions qui rend de la vie
# afficher les dégats infligés par l'ennemi et le joueur à chaque tour
# prise ne charge des mauvaises input
# L'ennemi ne dispose d'aucune potion.
# Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
# Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
# L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
# Lorsque vous utilisez une potion, vous passez le prochain tour.

from random import randint

player_one = { "HP" : 50, "potion" : 3}
hp_ennemi = 50
MENU = "Souhaitez-vous attaque (1) ou utiliser une potion (2) ?"

while player_one["HP"] > 0 and hp_ennemi > 0 :
    attack = {"ennemi" : randint(5,15), "player" : randint(5,10)}
    heal = randint(15,50)
    user_choice = input(MENU)
    while not (user_choice == "1" or user_choice == "2"):
        print("Mauvaise input")
        user_choice = input(MENU)
        
    if user_choice == "1" :
        hp_ennemi -= attack["player"]
        print(f"Vous avez infligé {attack['player']} points de dégats")
        if hp_ennemi <= 0:
            print("Tu as gagné ! 🥳 ")
            break
        print(f"Il reste {hp_ennemi} points de vie à l'ennemi")

    elif user_choice == "2" and player_one["potion"] > 0:
        player_one["potion"] -= 1
        player_one["HP"] += heal
        print(f"Vous récupérez {heal} points de vie")
        print("Vous passez votre tour..")
    elif player_one["potion"] == 0 and user_choice == "2" :
        print("Vous n'avez plus de potion")
        continue


    player_one["HP"] -= attack["ennemi"]
    print(f"L'ennemi vous a infligé {attack['ennemi']} points de dégats")
    if player_one["HP"] <= 0 :
        print("Tu as perdu ! 😓")
        break
    print(f"Il vous reste {player_one['HP']} points de vie.")
    print("_"*30)

print("Fin du jeu")


    
