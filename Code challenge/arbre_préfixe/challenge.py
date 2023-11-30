#  Étapes
# 1. Créez la logique de base en définissant la fonction add() pour ajouter un mot
# 2. Ajouter une valeur de type booléenne pour marquer la dernière lettre de la clé (chaîne représentant les mots intégrés à la trie)
# 3. Chaque nœud interne ou feuille doit ainsi contenir la lettre courante et la valeur citée au point n°2 (True si c'est un mot, False si c'est un prédicat)
# 4. Créez la fonction contains() pour vérifier la présence d'une clé dans l'arbre préfixe
# 5. Développez l'affichage complet

# Mots à intégrer
# [à, arbre, art, artiste, chape, chapeau, créatif, création, œuf, zèbre]

# liste_mots = ["à", "arbre", "art", "artiste", "chape", "chapeau", "créatif", "création", "œuf", "zèbre"]

# liste_mots.sort()

# print(liste_mots)

# def countBits(num: int):
#     counter = [0]
#     for i in range(1, num+1):
#         print(i >> 1, i % 2, "+", counter[i >> 1])
#         counter.append(counter[i >> 1] + i % 2)
#         print(counter)
#     return counter

# print(countBits(10))

# for x in range(10,0,-1):
#     print(x)

# cost = [1,100,1,1,1,100,1,1,100,1,0]
# cost = [10,15,20]
# print(cost)
# # print(cost[len(cost)::-1])

# for i in range(len(cost)-3,-1,-1):
#     # print(i)
#     print(f"iter : {i} on cherche {cost[i+1]} et {cost[i+2]}")
#     cost[i]+=min(cost[i+1],cost[i+2])

# print(cost)

# def fibonacci(n):
#     if n <= 0:
#         return "Veuillez saisir un entier positif pour générer la suite de Fibonacci."
#     elif n == 1:
#         return 0  # Le premier terme de la suite est 0
#     elif n == 2:
#         return 1  # Le deuxième terme de la suite est 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Nombre de termes de la suite à afficher
# n = 10

# print(f"Les {n} premiers termes de la suite de Fibonacci sont :")
# for i in range(1, n + 1):
#     print(fibonacci(i), end=" ")

# def inverser_nombre(nombre):
#     nombre_inverse = 0
#     while nombre > 0:
#         reste = nombre % 10  # Obtenir le dernier chiffre du nombre
#         nombre_inverse = nombre_inverse * 10 + reste  # Ajouter le chiffre au nombre inversé
#         nombre = nombre // 10  # Supprimer le dernier chiffre du nombre
#     return nombre_inverse

# # Exemple avec le nombre 10
# nombre = 123
# nombre_inverse = inverser_nombre(nombre)
# print(f"Le nombre {nombre} inversé est : {nombre_inverse}")

star = "*"
n = 10
for i in range(1,n):
    if i < n/2:
        print(star)
        star += "*"
    else:
        star = star[:n-i]
        print(star)
    