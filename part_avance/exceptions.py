#LBYL : Look Before You Leap / regarde avant de sauter
#EAFP : it's Easier to Ask for Forgiveness than Permission / il est plus facile de demander pardon que de demander la permission
dicti = {}

#LBYL
if "cle" in dicti:
    print(dicti["cle"])
    
liste = [2,7,"texte",4]
for i in liste:
    if not str(i).isdigit():
        liste.remove(i)
total = sum(liste)

#EAFP
try:
    print(dicti["cle"])
except:
    pass

liste = [2,7,"texte",4]
try:
    total = sum(liste)
except:
    total = 0
    
a = 5
# b = "truc"

try:
    print(a/b)
except ZeroDivisionError:
    print("Division par zero impossible")
except TypeError:
    print("Division par une valeur incorrect")
except NameError as e:
    print("Error :", e)
finally:
    print("Finalement")
    