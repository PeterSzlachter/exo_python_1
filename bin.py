def DecToBin(n) :
    liste = []
    while( n >= 1):
        liste.append(n%2)
        n //= 2
    liste.reverse()
    for i in range(len(liste)):
        liste[i] = str(liste[i])
    res = "".join(liste)
    return res
##
##print(DecToBin(20))

vingt = "10100"
##print(len(vingt))
##print(vingt[2])
##print(dir(str(vingt)))

def BinToDec(n):
    n = str(n)
    pw = len(n)-1
    print(n[pw])
    res = 0
    for i in n:
        print(i)
        res += int(i)*pow(2,pw)
        pw -= 1
    return res

print(BinToDec(10100))

def ipToBin(ip):
    res = ip.split('.')
    newList = []
    for i in res:
        i = int(i)
        newList.append(DecToBin(i))
    newList = ".".join(newList)
    return newList
    

print(ipToBin('192.168.10.25'))
        
        
    
