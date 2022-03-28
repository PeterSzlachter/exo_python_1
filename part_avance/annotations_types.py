a: int = 5

def add (a: int = 0 ,b: int = 0) -> int: #si pas de typage add(a=0,b=0)
    return a + b

add(3  , 4)

def ajouter_List() -> list[int]: 
    return [1]

print(ajouter_List())
print(type(ajouter_List()))