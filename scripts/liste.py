# liste : objet mutable
liste = []

liste.append("Element")
liste.extend([1, 2 ,3])
liste.remove(1)

print(liste)
print(liste[2])
print(liste[-1])
print(liste[-2])

l = ["User_1", #0 -5
     "User_2", #1 -4
     "User_3", #2 -3
     "User_4", #3 -2
     "User_5", #4 -1
     "User_6"] #5

# array [start:stop:step]

print(l[0:1])
print(l[2:4])
print(l[0:5:2])
print(l[::2])
print(l[1:-1])
print(l[::-1])

employes = ["Carlos","Max", "Martine", "Patrcik", "Alex","Max"]
print(employes.index("Martine"))
print(employes.count("Max"))
tri = sorted(employes)
# print(employes.sort())
print(employes)
print(tri)
print(employes.pop(-1))
print(employes)
employes.clear()
print(employes)

phrase = ["Je", "code", "en", "python"]
result = " ".join(phrase)
print(result)
result = result.split()
print(result)

print("code" in phrase)

liste_2 = ["Python", ["Java", "C++",["C"]], ["Ruby"]]
print(liste_2[1][2][0])
print(liste_2[0][1:3])

notes = [12,14,20,10,8]
print(any([x > 18 for x in notes]))

mytuple=("orange", "peche", "mangue", "banane")
# Affiche le deuxieme et troisieme (le "1" n est pas inclus)
print(mytuple[1:3])
# Affiche du 3e au dernier
print(mytuple[2:])
# Affiche du debut au troisieme
print(mytuple[:3])
# Affiche du deuxieme a l'avant dernier
print(mytuple[1:-1])