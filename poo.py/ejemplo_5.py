from clasevectorcito import vector
import random

n= int(input("entre tamaño del primer vector: "))
vec1 = vector(n)
vec1.construyeVector(n//2,50)
m = int(input("entre tamaño del segundo  vector: "))
vec2 = vector(m)
vec2.construyeVector(m//2,100)

vec1.seleccion()
vec2.seleccion()
vec3= vector(m+n)
i =1 
j= 1
while i <= vec1.V[0] and j<= vec2.V[0]:
    if vec1.V[i] < vec2.V[j]:
        vec3.agregarDato(vec1.V[i])
        i = i+1
    else:
        vec3.agregarDato(vec2.V[j])
        j = j+1
while i<= vec1.V[0]:
    vec3.agregarDato(vec1.V[i])
    i= i+1
while j <= vec2.V[0]:
    vec3.agregarDato(vec2.V[j])
    j= j+1

vec1.imprimeVector("vector 1 de prueba")
vec2.imprimeVector("vector 2 de prueba")
vec3.imprimeVector("vector resultado  de la  intercalacion")
