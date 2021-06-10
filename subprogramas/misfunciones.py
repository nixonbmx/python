import math

def factorial(n):
    f = 1
    for i in range (1,n +1):
        f = f * i
    return f

def esPrimo(n):
    if n%2==0:
        return False
    i= 3
    while i<= math.sqrt(i):
        if n%i==0:
            return False
        i=i+2
    return True

def comienzaCon(x):
    pd=x
    while pd>9:
        pd=pd//10
    return pd

def mcd(x,y):
    res= x%y
    while res!=0:
        x=y
        y=res
        res=x%y
    return y

def mcm (x,y):
    return x*y//mcd(x,y)

