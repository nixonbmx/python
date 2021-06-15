from clasevectorcito import vector
import random
n= int(input("entre tamaño del vector: "))
vec = vector(n)
vec.V[0]= n//2
for i in range(1, n//2 +1):
    vec.V[i] = random.randint(1,100)
vec.imprimeVector("vector de prueba")
vec.agregarDato(13)
vec.imprimeVector("vector  con dato agregado")
vec.seleccion()
vec.imprimeVector("vector ordenado ascendentemente")
i = vec.buscarDondeInsertar(39)
vec.insertar(39,i)
vec.imprimeVector("vector con dato 39 insertado")
vec.insertar(44)
vec.imprimeVector("vector con dato 44 insertado")