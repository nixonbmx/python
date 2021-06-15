from clasevectorcito import vector
import random

n=int(input("entre tamaño del vecto: "))

vec = vector(n)
vec.V[0] = n//2
for i in range(1, n//2 + 1):
    vec.V[i]= random.randint(1,100)
vec.imprimeVector("vector de prueba")
mayda = vec.mayor()
menda = vec.menor()
print("el mayor dato esta en la posicion ", mayda, "y es", vec.V[mayda])
print("el menor dato esta en la posicion ", menda, "y es", vec.V[menda])
vec.burbuja