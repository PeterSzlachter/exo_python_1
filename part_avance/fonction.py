def retourne_cinq():
    return 5

print(retourne_cinq())

def display(message="Valeur par défaut"):
    print(locals())
    print(message)
    
def addition(a,b):
    return print(a+b)

display("salut")
display()
addition(b=10,a=100)

b = 100 #espace global

def local_space():
    print(b)
    a = 5 #espace local
    print(a)
    
local_space()

print(globals())