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

from random import randint

number_to_find = randint(0, 100)
remaining_attempts = 5

print("*** Le jeu du nombre mystère ***")

# Boucle principale
while remaining_attempts > 0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    # Saisie de l'utilisateur
    user_choice = input("Devine le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    
    user_choice = int(user_choice)    

    if number_to_find > user_choice:  # Plus grand
        print(f"Le nombre mystère est plus grand que {user_choice}")
    elif number_to_find < user_choice:  # Plus petit
        print(f"Le nombre mystère est plus petit que {user_choice}")
    else:  # Égal (succès)
        break

    remaining_attempts -= 1

# Gagné ou perdu
if remaining_attempts == 0:
    print(f"Dommage ! Le nombre mystère était {number_to_find}")
else:
    print(f"Bravo ! Le nombre mystère était bien {number_to_find} !")
    print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai")

print("Fin du jeu.")