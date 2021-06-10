n= int(input("entre valor  de n "))
r= int(input("entre valor  de r "))

fn = 1
for i in range (1,n +1):
    fn = fn * i

fr = 1
for i in range (1,r +1):
    fr = fr *i

fnr = 1
for i in range (1, n-r+1):
    fnr=fnr *i

nc = fn//fr//fnr
print("n=",n,"r=",r,"factorial de n= ", fn, "factorial  de r=",fr,"factorial de n-r=",fnr,"numero de combinaciones=",nc)

################################################

import misfunciones as mf

"""def factorial(n):
    f= 1
    for i in range(1,n+1):
        f= f*i
    return f
    """
n= int(input("entre valor  de n "))
r= int(input("entre valor de r  "))

fn=mf.factorial(n)
fr=mf.factorial(r)
fnr=mf.factorial(n-r)

nc= fn//fr//fnr
print("n=",n,"r=",r,"factorial de n=", fn,"factorial de r=", fr,"factorial  de n -r= ",fnr,"numero de combinaciones =", nc)
 
 ###############################################

 
import misfunciones as mf
a=int(input("entre valor de a"))
b=int(input("entre valor de b"))

if mf.esPrimo(a):
    print(a,"es primo")
else:
    print(a,"no es primo")

if mf.esPrimo(b):
    print(b,"es primo")
else:
    print(b,"no es primo")

mcd=mf.mcd(a,b)
print("el maximo comun divisor  de ", a, "y",b,"es", mcd)

mcm=mf.mcm(a,b)
print("el minimo comun multiplo de", a,"y", b,"es", mcm)

da=mf.comienzaCon(a)
print("el primer digito de ", a, "es", da)

db=mf.comienzaCon(b)
print("el primer digito de", b, "es", db)


########################################################


