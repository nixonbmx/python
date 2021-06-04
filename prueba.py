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
    