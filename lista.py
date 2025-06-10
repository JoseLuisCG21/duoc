# #       -6 -5-4-3 -2 -1
# lista = [3,6,9,12,15,18]
# #        0 1 2  3  4  5

# print(lista)
# # print(lista.index(12))
# lista.append(64)

# print(lista)


# Numeros

#       -6 -5-4-3 -2 -1
numeros = [3,6,9,12,15,18]
#        0 1 2  3  4  5

# for numero in numeros:
#     print(f"Nota: {numero*3}")

# num=int(input("Ingrese un numero: "))

# numeros.append(num)
# print(numeros)


nombres = []
apellidos = []
cont=0
while True:
    print('''
            1.- Ingresar Nombres
            2.- Mostrar Nombres y Apellidos
            3.- Buscar Nombre
            4.- Salir
            ''')
    
    op=int(input("Seleccione una opcion: "))
    match op:
        case 1:
            nom=input("Ingrese un nombre: ")
            nombres.append(nom)
            ape=input("Ingrese un apellido: ")
            nombres.append(ape)
            print(nombres)
        case 2:
            cont=0
            for n in nombres:
                print(cont+1, ".-". nombres[cont], apellidos[cont])
                cont+=1
            for i in range(len(nombres)):
                print(i+1,".-", nombres[i], apellidos[i])
        case 3:
            busca=input("Ingrese el nombre a buscar: ")
            if busca in nombres:
                print(f"El nombre {busca} existe en la lista")
            else:
                print(f"El nombre {busca} no existe en la lista")
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opcion invalida")

































