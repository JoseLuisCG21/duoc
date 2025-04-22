#uso del for

# # num=int(input("ingrese un num"))

# num=int(input("ingrese un numero"))

# for i in range(10):
#     print(num,i+1 , (i+1)*num)


cant=int(input("ingrese el numero de notas"))
suma=0
for i in range(cant):
    print("ingrese primera nota", i+1)
    nota=input(float(input()))
    suma=suma+nota
prom=suma/cant
print("el promedio es", round(prom))