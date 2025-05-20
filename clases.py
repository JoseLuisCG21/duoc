# #Uso y explicacion del match
# import random

# def suma():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(f"El resultado de la suma es: {n1+n2}")
#     suma()
# def resta():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(f"El resultado de la resta es: {n1-n2}")
#     resta()
# def multiplicacion():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(f"El resultado de la multiplicacion es: {n1*n2}")
#     multiplicacion()
# def division():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(f"El resultado de la division es: {n1/n2}")
#     division()


# def calcu():
#     while True:
#         op=int(input(''' Ingrese una opcion
#                 1.- suma
#                 2.- resta
#                 3.- multiplicacion
#                 4.- division
#                 5.- salir'''))

#         match op:
#             case 1:
#                 print("suma")
#                 suma()
#             case 2:
#                 print("resta")
#                 resta()
#             case 3:
#                 print("multiplicacion")
#                 multiplicacion()
#             case 4:
#                 print("division")
#                 division()
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("opcion invalida")

# calcu()

# #Perros
# import random
# while True:
#     try:
#         perros=int(input("Ingrese la cantidad de perros: "))
#         cuota=int(input("ingrese la cantidad minima de cuota por conejos: "))
#         cumplen=0
#         conejos=random.randint(0,10)
#         print("Los perros fueron a cazar!!")

#         for p in range(perros):
#             if cuota>=conejos:
#                 print(f"El perro {p+1} trajo {conejos} conejos")
#                 cumplen+=1
#             else:
#                 print(f"El perro {p+1} trajo {conejos} conejos. se queda sin filete")
            
#         print(f"El total de perros que cumplen con la cuota fue: {cumplen}")
#         print(f"El total de perros que no cumplen con la cuota fue: {perros-cumplen}")

#     except Exception:
#         print("Solo debes poner numeros enteros")







rojos=int(input("Ingrese la cantidad de rojos"))
taller=int(input("Cuantas veces asistio a talleres??"))
decimas=0.3













































































































































