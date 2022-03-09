import random

def findNumber(k):
    count = 0
    choice = 0
    print(k)

    while ( k != choice):
        try:
            choice = int(input("Trouver le nombre mystère : "))
            if k > choice :
                print("C'est plus !")
            elif k < choice:
                print("C'est moins !")
            count += 1
        except ValueError as e:
            print('Mauvais input')
            print(e)
            
    print("Bravo vous avez trouvé le nombre mystère en",count,"essai(s)")


findNumber(random.randint(1,100))

