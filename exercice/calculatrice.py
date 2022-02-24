print("Additionner deux nombres de votre choix :")
nombre_1 = input("Choisir un premier nombre : ")
nombre_2 = input("Choisir un deuxième nombre : ")

while not (nombre_1.isdigit() and nombre_2.isdigit()) :
    print("Veuillez entrer deux nombres valides")
    nombre_1 = input("Choisir un premier nombre : ")
    nombre_2 = input("Choisir un deuxième nombre : ")

print(f"Le résultat de l'addition de {nombre_1} avec {nombre_2} est égal à {int(nombre_1) + int(nombre_2)}")