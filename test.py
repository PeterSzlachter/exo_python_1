# chaine = "Pierre, Julien, Anne, Marie, Lucien"
# chaine = chaine.split(", ")
# chaine.sort()
# chaine = ", ".join(chaine)
# print(chaine)

# Ne modifie pas les lignes suivantes
# import sys
# note = sys.argv[-1]
# commentaire = ""
# note = input("note :")
# # Change l'ordre des if / elif
# if note < 3 :
#     commentaire = "Sans commentaire..."
# elif note >= 3 and note < 6:
#     commentaire = "Tu n'as rien compris !"
# elif note >= 7 and note < 10 :
#     commentaire = "Il faut tout revoir..."
# elif note >= 11 and note < 14 :
#     commentaire = "Peut mieux faire."
# elif note >= 15 and note < 18 :
#     commentaire = "Bon travail !"
# elif note >= 18 and note < 20:
#     commentaire = "Excellent !!"
# elif note == 20:
#     commentaire = "C'est un sans faute !"


# # Ne modifie pas la ligne ci-dessous
# print(commentaire)

# for i in range(1,11):
#     print("Utilisateur ",i)

# mot = "Python"
# for l in mot[::-1]:
#     print(l)
# print(mot[::-1])

# mot = "Python"
# for lettre in reversed(mot):
#     print(lettre)

# continuer = "o"
# while continuer == "o":
#     print("On continue !")
#     continuer = input("Voulez-vous continuer ? o/n ")
# print("Fin du programme")

# print(n := len(a := [1,2,3,4]))

# prenom = input("Quel est votre prénom ?")
# ville_de_naissance = input("Quel est votre ville de naissance ?")
# age = input("Quel est votre age ?")

# print(prenom,ville_de_naissance,age)

# from random import randint

# number_to_find = randint(0, 100)
# remaining_attempts = 5

# print("*** Le jeu du nombre mystère ***")

# # Boucle principale
# while remaining_attempts > 0:
#     print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

#     # Saisie de l'utilisateur
#     user_choice = input("Devine le nombre : ")
#     if not user_choice.isdigit():
#         print("Veuillez entrer un nombre valide.")
#         continue
    
#     user_choice = int(user_choice)    

#     if number_to_find > user_choice:  # Plus grand
#         print(f"Le nombre mystère est plus grand que {user_choice}")
#     elif number_to_find < user_choice:  # Plus petit
#         print(f"Le nombre mystère est plus petit que {user_choice}")
#     else:  # Égal (succès)
#         break

#     remaining_attempts -= 1

# # Gagné ou perdu
# if remaining_attempts == 0:
#     print(f"Dommage ! Le nombre mystère était {number_to_find}")
# else:
#     print(f"Bravo ! Le nombre mystère était bien {number_to_find} !")
#     print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai")

# print("Fin du jeu.")

# import random

# ENEMY_HEALTH = 50
# PLAYER_HEALTH = 50
# NUMBER_OF_POTIONS = 3
# SKIP_TURN = False

# while True:
#     # Jeu du joueur
#     if SKIP_TURN:
#         print("Vous passez votre tour...")
#         SKIP_TURN = False
#     else:
#         user_choice = ""
#         while user_choice not in ["1", "2"]:
#             user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

#         if user_choice == "1":  # Attaque
#             your_attack = random.randint(5, 10)
#             ENEMY_HEALTH -= your_attack
#             print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi ⚔️")
            
#         elif user_choice == "2" and NUMBER_OF_POTIONS > 0:  # Potion
#             potion_health = random.randint(15, 50)
#             PLAYER_HEALTH += potion_health
#             NUMBER_OF_POTIONS -= 1
#             SKIP_TURN = True
#             print(f"Vous récupérez {potion_health} points de vie ❤️ ({NUMBER_OF_POTIONS} ? restantes)")
#         else:
#             print("Vous n'avez plus de potions...")
#             continue

    
#     if ENEMY_HEALTH <= 0:
#         print("Tu as gagné ?")
#         break

#     # Attaque de l'ennemi
#     enemy_attack = random.randint(5, 15)
#     PLAYER_HEALTH -= enemy_attack
#     print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")

#     if PLAYER_HEALTH <= 0:
#         print("Tu as perdu ?")
#         break

#     # Stats
#     print(f"Il vous reste {PLAYER_HEALTH} points de vie.")
#     print(f"Il reste {ENEMY_HEALTH} points de vie à l'ennemi.")
#     print("-" * 50)

# print("Fin du jeu.")

# a, b = 5, 10

# print(f"{b}")