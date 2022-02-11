from math import sqrt

def dichotomie(tgt,a,b):
    diff = b-a
    mid = (b+a)/2
    
    while(diff > 0.001):
        print(mid)
        if mid >= tgt:
            b = mid
            mid = (b+a)/2
            diff = b-a
        else:
            a = mid
            mid = (b+a)/2
            diff = b-a
    print(tgt,"est comprise entre",a:.4f ,"et",b:.4f)

dichotomie(sqrt(2),1,50)


    
    
