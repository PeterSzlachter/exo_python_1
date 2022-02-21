liste = [5,1,3,4,8]
liste = sorted(liste) #fonction sorted
print(liste)
liste = [5,1,3,4,8]
print(liste)
liste.sort() #return None Method sort
print(liste)

#Muable : listes, dictionary, sets
#Immuable : string, nombres

texte = "Le seigeur des anneaux" #String => immuable
texte.title()
print(texte)
titre = texte.title()
print(titre)
test = [i*2 for i in range(0,5)]

print(len(texte))
print(len([1,2,3]))
print(round(2.2))
print(round(2.7))
print(max(liste))
print(min(liste))
print(max("abc"))
print(min("abc"))
print(sum(liste))
print(test)