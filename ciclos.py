
#PRIMER EJEMPLO
# construir un programa que lea un numero entero  n>0 y que calcule y muestre la suma de todos los enteros desde 1 hasta n:
numero= int(input("ingrese un numero"))
suma= 0 
i= 1
while i <= numero:
    suma = suma +i
    i = i +1

print(numero,suma)
#la variable controladora del ciclo  es la variable i 


#SEGUNDO EJEMPLO
#elaborar un programa para calcular y mostrar  el factorial de un entero  entrado por teclado 
factorial  = 1
i = 1
while i <= numero:
    factorial = factorial * i
    i= i + 1
print("el factorial  de", numero, "es", factorial)



#TERCER EJEMPLO
#determinar  el nuevo salario  de una persona en una lista de empleados
nombre = input("entre nombre ")
while nombre != "":
    salario = int(input(f"{nombre}entre salario"))  
    aumento = 0.
    if salario <1000:
        aumento = salario  *0.1
    nuevosalario = salario + aumento
    print("nombre",nombre,"\tsalario",salario,"\taumento\t", aumento, "\tnuevosalario\t ", nuevosalario)
    nombre =input ("entre nombre")
print("termine")


"""Elaborar un programa para determinar el nuevo salario de una
persona, contando a cuántas se les hizo el cálculo, cuántas
tuvieron un aumento mayor que cero, el total de salarios
anteriores, el total de aumentos, el total de nuevos salarios, el
promedio salarial antes y después del aumento y el promedio
de aumentos"""
tsa= 0.
tau=0.
tns=0.
contador=0
contAu=0
nombre = input("entre nombre")
while nombre != "":
    salario = int(input(f"{nombre} entre salario"))
    tsa = tsa + salario
    contador = contador + 1
    aumento= 0.
    if salario< 1000:
        aumento = salario *0.1
        tau= tau+ aumento
        contAu = contAu +1
    nuevosalario=salario + aumento
    tns= tns +nuevosalario
    print("nombre", nombre, "\tsalario",salario, "\taumento\t", aumento, "\t nuevo salario\t", nuevosalario)
    nombre = input("entre nombre")
psa = tsa /contador
pau = tau /contador
pns = tns /contador
print("total empleados ", contador, "\ttotal con aumento > cero ", contAu)
print("total salarios anteriores\t ", tsa, "\tpromedio\t", psa)
print("total aumentos               \t", tau, "\tpromedio\t", pau)
print("total nuevos salarios         \t", tns,  "\tpromedio\t",pns)

#determina si un numero x es primo  o no 
x = int (input("entre un numero  entero "))
i = 2
while i <x**(.5) and x % i !=0:
    i = i + 1
if i > x**(.5):
    print(x, "es primo")
else:
    print(x, "no es primo, es divisible  por ", i )


n = input("muestra los primos  desde  3 hasta 33")
#muestra  los primos  desde  3  hasta 101
x= 3
while x<= 33:
    i= 2
    while i <= x**(.5) and  x % i !=0:
        i = i +1
    if i > x**(.5):
        print(x,"es primo ")
    x= x+2

import math
x = int(input("entre numero entero "))
i = 2
while i <= math.sqrt(x) and x % i !=0:
    i=i+1
if i > math.sqrt(x):
    print(x, "es primo")
else:
    print(x," no es primo")


n= int(input("entre numero entero"))
i= 1
while i <=10:
    r=n *i
    print(n, "*", i, "=",r)
    i= i+1
print("ternime\n")

n= int(input("entre un numero entero"))
x =1
while x <=n:
    i=1
    while i<=10:
        r=x*i
        print(x,"*",i, "=", r)
        i=i+1
    x=x+1
    print(" ")



    #
    
a = input("entre un número ")
b = input("entre otro número ")
c = int(input("entre un tercer número "))
d = int(input("entre un cuarto número "))
if  b > a:
    print(c+d, end=",")
    print(a+b)
else:
    if a == b:          
        print(a, d)
    else:
        print(a, b, c, d, sep ="")

 #ejemplo: la suma  de los  enteros desde  1 hasta n 
n = int(input("entre un numero entero"))
suma= 0
for i in range(1, n+1, 1):
    suma=suma+i
print("la suma de los  enteros desde 1 hasta n  con parametros 1, n+1, 1 es:", n, "es,", suma)


suma= 0
for i  in range (1, n, 1    ):
    suma= suma +i 
print("la suma  de los enteros desde 1 hasta n con parametros 1, n,1 es ", n, "es",  suma)


suma= 0
for i in range (n+1):
    suma = suma +i
print("la suma de los enteros desde 1 hasta n con el solo parametro n+1 es: ", n, "es", suma)

#el factorial de un entero n

factorial = 1
for i in range ( 1, n+1, 1):
    factorial = factorial *i
print("el factorial  de n  con parametros 1, n+1, 1 es: ", n , "es", factorial)

factorial= 1
for i in range( 1,n, 1):
    factorial= factorial*i
print("el factorial de n con parametros 1, n , 1 es: ", n," es", factorial)

factorial= 1 
for i  in range(n+1):
    factorial= factorial*i
print("el factorial de ", n , "es", factorial)



x=int(input("entre un numero entero"))
if x%2== 0 :
    print (x, "no es primo , es numero par ")
    exit(0)
i=2 
for i in range (3,int (x**(.5))+1, 2):
    if x % i==0:
        print(x, "no es numero primo, es divisible  por", 1)
        break
if x %i !=0:
    print(x, "es primo ")
    


n= int(input("entre numero entero "))

for  i in range (1, n+1):
    for j in range (1, i+1):
        print(i,end="")
    print("")
print("")

for i in range (1, n+1):
    for j in range (1,i+1):
        print(j,end="")
    print("")
print("")

for i in range(n,0,-1):
    for j in range (1,i+1):
        print(i, end="")
    print("")
print("")

for i in range(n,0, -1):
    for j in range(i,0,-1):
        print(j,end="")
    print("")
    

