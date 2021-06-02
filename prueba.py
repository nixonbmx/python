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

        


