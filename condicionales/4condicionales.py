
#ejemplo_uno
salario = float(input("ingrese salario actual"))
aumento = 0 
if salario < 1000000:
    aumento = salario * 0.1
nuevosalario = salario + aumento
print(f"salario actual={salario}", f"aumento ={aumento}", f"nuevo salario {nuevosalario}", sep= "; " )

#ejemplo 2 usando else
salario =float(input("ingrese el salario"))
if salario < 1000000:
    aumento=salario * 0.1
else:
    aumento=0
nuevosalario=salario+aumento
print(f"salario actual ={salario}", f"aumento ={aumento}", f"nuevo salario ={nuevosalario}", sep="; ")

#ejemplo 3 leer dos numeros enteros  e imprimirlos en orden ascendente, es necesario utilizar else
a = int(input("ingrese un  numero entero "))
b = int(input("ingrese otro numero entero "))
if a < b :
    print(a , b )
else:
    print(b , a)

#ejercicio_uno
#Determinar si un número entero entrado por pantalla es divisible por otro número entrado también por pantalla.
a = int(input("ingrese un  numero entero "))
b = int(input("ingrese otro numero entero "))
if a % b == 0:
    print(a,"es divisible por",b)
else:
    print(a, "no es divisible por" , b)
print("fin")

#Leer tres números enteros y determinar si la suma de dos de ellos da el tercero.
a = int(input("ingrese un  numero entero "))
b = int(input("ingrese otro numero entero "))
c = int(input("ingrese un tercer  numero entero "))
if a +b == c:
    print (c,"es la suma de ", a, "con ", b)
else:
    if a + c == b:
         print (b, "es la suma de", a,"con ", c)
    else:
        if b+c == a:
            print(a, "es la suma de", b,"con", c)
        else:
            print(a,b,"y",c, "no cumplen la condicion")
print("fin ")            


#determina si tres valores pueden formar un triangulo o no
a = int(input("ingrese el primer numero entero "))
b = int(input("ingrese el segundo numero entero "))
c = int(input("ingrese el tercer numero entero "))
if a+b>c:
    if a+c>b:
        if b+c>a:
            print(a, b,"y", c, "pueden  formar un triangulo")
        else:
            print(a, b, "y",c,"no pueden formar un triangulo")
print("fin del triangulo con tres if ")


if a+b>c and a+c>b and b+c>a:
    print(a,b,"y", c, "pueden formar un triangulo")
else:
    print(a,b,"y", c,"no pueden formar un triangulo")
print("fin del triangulo con un solo if ")


    
#Instrucciones de desición anidadas
nombre = input("entre el nombre: ")
genero=int(input("entre genero: "))
estatura=int(input("entre estatura: "))
peso=int(input("entre peso: "))
if estatura > 180:
    if peso > 70:
        if genero == 0:
            print("reina de belleza")
        else:
            print("cantautor")
    else:
        print("arbitro de futbol")
else:
    print("jugador de parques")
print("paciente clasificado")



#Ejercicios con la instrucción if-else anidadas 


a = int ( input("Entre un número entero:  "))
b = int ( input("Entre otro número entero: ")) 
c = int ( input("Entre un tercer número entero: ")) 

aa=a
bb=b
cc=c
print("version 1, la comparacion es compuesta solo con un menor(<), y sin else", end =": \n")

if a < b and b < c:
    print (" a", a, " b", b, " c",c)
if a < c and c < b:
    print (" a", a, " c", c, " b",b)
if b < a and a < c:
    print (" b", b, " a", a, " c",c)
if b < c and c < a:
    print (" b", b, " c", c, " a",a)
if c < a and a < b:
    print (" c", c, " a", a, " b",b)
if c < b and b < a:
    print (" c", c, " b", b, " a",a)
print("")

a=aa
b=bb
c=cc
print("version 1a, la comparacion es compuesta solo con un menor(<=), y sin else", end =": \n")

if a <= b and b <= c:
    print (" a", a, " b", b, " c",c)
if a <= c and c <= b:
    print (" a", a, " c", c, " b",b)
if b <= a and a <= c:
    print (" b", b, " a", a, " c",c)
if b <= c and c <= a:
    print (" b", b, " c", c, " a",a)
if c <= a and a <= b:
    print (" c", c, " a", a, " b",b)
if c <= b and b <= a:
    print (" c", c, " b", b, " a",a)
print("")

a=aa
b=bb
c=cc
print("version 2: la comparacion es compuesta con menor o igual (<=) usando  else", end=": \n" )
if a <= b and b <= c:
    print(" a", a, " b", b, " c",c)
else:   
    if a <= c and c <= b:
        print(" a", a, " c", c, " b",b)
    else:
        if b <= a and a <= c:
            print(" b", b, " a", a, " c",c)
        else:
            if b <= c and c <= a:
                print(" b", b, " c", c, " a",a)
            else:
                if c <= a and a <= b:
                    print(" c", c, " a", a, " b",b)
                else:
                    print(" c", c, " b", b, " a",a)
print("")


a=aa
b=bb
c=cc

print("version 3: con if anidados", end=": \n" )
if a < b:
    if b < c:
        print (" a", a, " b", b, " c",c)
    else:
        if a < c:
            print (" a", a, " c", c, " b",b)
        else:
            print (" c", c, " a", a, " b",b)
else:
    if a < c:
        print (" b", b, " a", a, " c",c)
    else:
        if b < c:
            print (" b", b, " c", c, " a",a)
        else:
            print (" c", c, " b", b, " a",a)


#proceso de seleccion multiple
#ejemplo 1
ingenieros = medicos = abogados = otros = 0
nombre = input("teclee su nombre")
profesion = int(input(f"{nombre} entre profesion: "))
if profesion == 1:
    ingenieros = ingenieros+1
elif profesion == 2:
    medicos = medicos +1
elif profesion == 3:
    abogados = abogados +1
else:
    otros=otros +1
print("ingenieros: ", ingenieros, "\nmedicos: ", medicos, "\nabogados: ",abogados, "\notros: ", otros)
#ejemplo 2
nombre = input("entre nombre: ")
estadocivil = int(input(f"{nombre} teclee su estado civil: "))
if estadocivil == 1:
    print(nombre, "soltero")
elif estadocivil ==2:
    print(nombre, "casado")
elif estadocivil ==3:
    print(nombre, "separado")
elif estadocivil==4:
    print(nombre, "viudo")
else:
    print("estado civi invalido ")


#ejercicio1
nombre = input("entre su nombre : ")
origen = int(input(f"{nombre} entre ciudad origen"))
destino = int(input(f"{nombre} entre ciudad destino "))
edad = int(input(f"{nombre} entre su edad "))

if origen == 5 or destino == 5:
    costotiquete = 980000
else: 
    if origen== 1:
        if destino == 2:
            costotiquete = 200000
            if edad < 60:
                costotiquete = 210000
        elif destino == 3:
            costotiquete = 250000 - .1 * edad *1000
        elif destino == 4:
            costotiquete = 300000 + edad *1000
    elif origen == 2:
        if destino ==1:
            if edad > 80:
                costotiquete =0
            else:
                costotiquete = 200000
        elif destino ==3:
            costotiquete= 200000
            if edad < 60:
                diferencia = 60 - edad
                if diferencia > 20:
                    sobrecosto = 20000
                else:
                    sobrecosto= diferencia *1000
                costotiquete = 200000 + sobrecosto
        elif destino == 4:
            costotiquete = 400000
            if edad > 60:
                costotiquete = 400000 + .05 * edad * 10000
    elif origen == 3:
        if destino  == 1:
            costotiquete = 350000
        elif destino == 2:
            costotiquete = 280000
            if edad > 60:
                costotiquete = 300000
        elif destino ==4:
            costotiquete = 190000
            if edad > 60:
                costotiquete = 200000
    elif origen == 4:
        if destino == 1:
            costotiquete = 500000
            if edad < 10:
                costotiquete = 250000
        elif destino == 2:
            costotiquete = 210000
            if edad < 30:
                costotiquete = 240000
        elif destino == 3:
            costotiquete = 350000
            if edad > 60:
                costotiquete = 350000 + (edad -60 ) * 10000
print (nombre, " el costo  de su tiquete  es:", costotiquete)

#ejercicio 3
nombre = input("entre su nombre ")
estadoCivil = int(input(f"{nombre} entre su estado civil "))
edad = int(input(f"{nombre} entre su edad "))
salario = int(input(f"{nombre} entre su salario "))
if   estadoCivil == 1:
    desc = "Soltero"
    if edad < 30:
        pau = 0.10
    else:
        pau = 0.12

elif estadoCivil == 2:
    desc = "Casado"
    if edad < 25:
        pau = 0.12
    else:
        pau = 0.15

elif   estadoCivil == 3:
    desc = "Separado"
    if edad < 20:
        pau = 0.08
    else:
        pau = 0.10

elif    estadoCivil == 4:
    desc = "Viudo"
    if edad < 30:
        pau = 0.15
    else:
        pau = 0.12

elif    estadoCivil == 5:
    desc = "Unión libre"
    if salario < 1000:
        pau = 0.20
    else:
        pau = 0.12

else:
    desc = "Estado civil inválido"
    pau = 0.0

aumento = salario * pau
nuevoSalario = salario + aumento
print(nombre, desc, "edad", edad, "salario", salario,"Porcentaje  de aumento", pau, "Aumento", end=": ")
print(aumento, "Nuevo salario", nuevoSalario)  
