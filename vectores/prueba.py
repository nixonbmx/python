def sumavector(V, n):
    s=0
    for i in range(1,n):
        s = s + V[i]
    return s

def mayorDato(V,n):
    mayor = 0
    for i in range(n):
        if V[i] >V[mayor]:
            mayor = i
    return mayor

nomMpio = ["", "medellin","bello", "envigado","sabaneta","itagui","rionegro","la ceja"]
n= 8
acmpio = [0] * n
mpio = int(input("entre el codigo del municipio"))
while mpio !=0:
    np = int(input("entre el numero de personas"))
    acmpio[mpio] = acmpio[mpio] + np
    mpio = int(input("entre el codigo del municipio"))
for i in range (1,n):
    print (i, nomMpio[i],acmpio[i])
th = sumavector(acmpio, n)
print ("total de habitantes ", th)
i = mayorDato(acmpio, n)
print("el mayor  numero  de habitaciones esta  en el municipio ", end=" ")
print(nomMpio[i], "con", acmpio[i], "habitantes")







