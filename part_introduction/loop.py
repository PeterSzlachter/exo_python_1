import time

element = "Bonjour tout le monde"
for e in element :
    print(e)

nombres = [0, 5, 8 ,7, 12]

for i in nombres:
    print(i)

count = 1
for e in range(10):
    print(count)
    count += 1

j = 0
while j < 10 :
    j += 1
    print("Ligne :",j)

# while True :
#     print("Sauvegarde en cours...")
#     time.sleep(30)

liste = ["1", "4", "25", "Paul", "3", "Peter"]
for element in liste:
    if element.isalpha():
        continue #break
    print(element)
    
nb = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
nb_positif = [i for i in nb if i > 0]
print(nb_positif)
for i in nb:
    if i > 0 :
        nb_positif.append(i)
print(nb_positif)
