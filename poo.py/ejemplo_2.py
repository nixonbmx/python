from clasevectorcito  import vector
import random

n= int(input("Entre el tamaño del vector: "))
vec1 = vector(n)
vec1.V[0] = n//2
for i in range(1, n//2 +1):
    vec1.V[i] = random.randint(1,100)
vec1.imprimeVector("vector de prueba uno ")
vacio =vec1.esVacio()
lleno =vec1.esLleno()
print("esta vacio ?", vacio)
print("esta lleno ?", lleno)
vec1.agregarDato(39)
vec1.imprimeVector("vector de prueba uno con dato agregado")
s = vec1.sumarDatos()
print("la suma de los datos es: ", s)
vec1.intercambiar(1,vec1.V[0])
vec1.imprimeVector("vector de prueba uno con datos intercambiados")