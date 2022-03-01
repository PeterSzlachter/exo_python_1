from math import *
from random import *

def distance(xa,ya,xb,yb):
    return sqrt(pow(xb-xa,2)+pow(yb-ya,2))

x = randint(0,100)
y = randint(0,100)
print(x,y)
print("Trouver le point générer par la machine ! Bonne chance ! :")
diff = 16
count = 0

while diff >= 15 :
    a = int(input("Coordonée x du point : "))
    b = int(input("Coordonée y du point : "))
    count += 1
    diff = distance(x,y,a,b)
    if diff >= 15 :
        print("cherche mon cochon")
    
print("tu as trouvé le point bg en ",count,"essai(s)", diff, "distance")



