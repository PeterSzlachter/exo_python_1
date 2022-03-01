def factoriel(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

##factoriel(4)
##factoriel(0)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

##print(factorial(4))

##def fib(n):
##    if n<=1:
##        return 1
##    elif n == 0:
##        return 0
##    return fib(n-1) + fib(n-2)


def fib(n):
    if n<=2:
        return 1
    current = 2
    old = 1
    res=0
    for i in range(3,n):
       res = current+old 
       print("old :",old) 
       print("current :",current)
       old = current
       current = res
    return res

##print("Résultat",fib(9))
