from random import randint

player_one = { "HP" : 50, "potion" : 3 }
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
        print(f"Vous avez infligé {attack['player']} points de dégats 🔪")
        if hp_ennemi <= 0:
            print("Tu as gagné ! 🥳 ")
            break
        print(f"Il reste {hp_ennemi} points de vie à l'ennemi ")

    elif user_choice == "2":
        if player_one["potion"] > 0 :
            player_one["potion"] -= 1
            player_one["HP"] += heal
            print(f"Vous récupérez {heal} points de vie")
            print("Vous passez votre tour..")
        else :
            print("Vous n'avez plus de potion")
            continue


    player_one["HP"] -= attack["ennemi"]
    print(f"L'ennemi vous a infligé {attack['ennemi']} points de dégats 🩸")
    if player_one["HP"] <= 0 :
        print("Tu as perdu ! 😓")
        break
    print(f"Il vous reste {player_one['HP']} points de vie.")
    print("_"*30)

print("Fin du jeu")


    
