age = int(input("quel age avez vous\n"))

print(type(age))

if age >= 18:
    print("Vous êtes majeur")
elif age < 18:
    print("Vous êtes mineur")
else:
    print("Mauvaise saisie")


result =  "Vous êtes majeur" if age >= 18 else "Vous êtes mineur"

print(result)

print("Fin de script")