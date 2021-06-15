import random

v= [0,0,0,0,0,0,0,0]
n= len(v)
print("el tamaño del V es:", n)
for i in range (0,8):
    print (v[i], end=", ")

n =  int(input("\nEntre tamaño del vector: "))
vec = [0]*(n+1)
m = len(vec)
print("El tamaño del vector es: ",m)
for i in range(1,m//2 +1):
    vec[i] =random.randint(1,100)
vec[0] = m//2
for i in range (1, m):
    print(vec[i],end=", ")
print()
for i in range(0,m):
    print(vec[i],end=", ")

print("\n ahora  generemos numeros entre  0 y 9")
for i in range (1, m//2 + 1):
    vec[i] = random.randint(0,9)
for i in range (1,m):
    print(vec[i], end=", ")
print()
for i in range(0, m):
    print(vec[i],end=", ")