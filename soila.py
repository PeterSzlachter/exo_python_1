#age = round(float(input("Quel est ton age ? ")))

while True:
    try:
        age = int(input("Quel est ton age ?"))
        break
    except ValueError:
        print("Faute de valeur")
nom = input("Quel est ton nom ?")



if age > 0 and age <= 25:
    print(nom+" ta formation est payée par l'Etat")
elif age <= 35:
    print(nom+" ta formation est payée par PUIC prologue numérique")
else:
    print(nom+" ta formation doit être financée par toi même")


