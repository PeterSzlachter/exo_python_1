from function import factoriel

factoriel(4)


def euroMillion():
    n1=50
    k1=5
    n2=12
    k2=2
    p1 = (factoriel(n1)/(factoriel(k1)*factoriel(n1-k1)))
    p2 = (factoriel(n2)/(factoriel(k2)*factoriel(n2-k2)))
    return print(p1*p2)

euroMillion()
