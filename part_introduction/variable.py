a = 5 #nom associé à un objet
b = 50
c = a
print(a+b)
print(5**5)
print(5*5*5*5*5)
print(id(a))
print(id(b))
print(id(c))

d,e = 10,90
d,e = e,d
print(d,e)

#sigleton et small integer cashing (entre -5 et 256)

print(id(True))
print("Toujours le même id sigleton -> tjr le même objet retourné",id(True))

f = 500

print(id(500))
print(id(50*10))
print(id(f))

print("Python est un langage dynamique et fortement typé")
print("""Dynamique : pas besoin de dire à Python quel est le type de la variable
On changer le type de la variable à tout moment.
ma_variable = 5
ma_variable = 'texte' """)
print("""Fortement typé : 
Impossible d'addition(opérations) sur 2 type différents
Pas besoin d'indiquer le type d'une variable
On peut changer le type d'une variable n'importe quand
Pour réaliser certaines opérations, on doit convertir les variables d'un type à un autre""")