##Lista
# Lista = [1,2,3,4,5,6]

# print(Lista[-2])

# for numero in Lista:
#     print(numero)
    
# dic = {"nombre": "Jose Luis",
#        "Numero": 819273,
#        "Pololeando": True,
#        "Direccion": "Los laureles"
# }

# print(dic)

# dic["edad"]=21

# print(dic)

# dic["empleado"]=False

# print(dic)

# corredores = ["zlatan", "Bombasi", "Lando"]
# tiempos = [10.9, 11.1, 12.5]

# while True:
#     try:
#         print('''
#             1.- Registrar corredor y tiempo
#             2.- Ver listado de corredores
#             3.- Ver estadisticas (tiempo menor, mayor, ordenados por mas rapido)
#             4.- Salir
#             ''')
        
#         op=int(input("Seleccione una opción: "))
#         match op:
#             case 1:
#                 corre=input("Ingrese el nombre del corredor: ")
#                 corredores.append(corre)
#                 tie=float(input("Registre su mejor tiempo: "))
#                 tiempos.append(tie)
#             case 2:
#                 for i in range(len(corredores)):
#                     print(f"Corredor: {corredores[i]}, tiempo {tiempos[i]}")
#             case 3:
#                 print(f"El tiempo mas rapido es: {min(tiempos)}")
#                 print(f"El tiempo mas lento es: {min(tiempos)}")
#                 print(f"Ordenados del mas rapido al mas lento")
#                 tiempos.sort()
#                 print(tiempos)
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opcion invalida")
        
#     except Exception as e:
#         print("Error:" , e)
        






# productos = {
#     "Lapiz" : 100,
#     "Goma" : 100,
#     "Estuche" : 500,
#     "Plumon" : 1000
# }

# while True:
#     try:
#         print('''
#               1.- Agregar articulo y precio
#               2.- Ver listado
#               3.- Borrar articulo
#               4.- Actualizar precio
#               5.- Salir
#               ''')
#         op=int(input("Seleccione una opción: "))
#         match op:
#             case 1:
#                 art=input("Ingrese el nombre del articulo: ")
#                 precio=int(input("Ingrese el precio del articulo: "))
#                 productos[art]=precio
#             case 2:
#                 for key, value in productos.items():
#                     print(key, "$",value)
#             case 3:
#                 borrar=input("Cual es el articulo que desea borrar??: ")
#                 del productos[borrar]
#                 print(f"El articulo {borrar} fue borrado")
#             case 4:
#                 for key, value in productos.items():
#                     print(key, "$",value)
#                     act=input("Cual articulo cuyo precio desea actualizar??: ")
#                     if act in productos:
#                         precio=int(input("Ingrese el precio nuevo: "))
#                         productos[act]=precio
#                     else:
#                         print("El articulo no existe")
#             case 5:
#                 print("Saliendo del sistema...")
#                 break
#             case _:
#                 print("Ingrese una opción valida")
#     except Exception as e:
#         print("Error: ", e)


















#Perros de casa

perros = {
    1:{"Nombre": "Droopy",
      "Raza": "Dog Hount",
      "Codigo": "Dp06"},
    2:{"Nombre": "Spike",
      "Raza": "Bulterrier",
      "Codigo": "Dbil77"},  
}

def mostrar_perros(lista):
    for key, perro in perros.items():
        print(key, perro)
    
def valida_pass(clave):    
    Mayuscula=False
    Minuscula=False
    Numero=False

    for palabra in clave:
        if palabra.isupper():
            Mayuscula=True
        if palabra.islower():
            Minuscula=True
        if palabra.isdigit():
            Numero=True
    if Mayuscula and Minuscula and Numero and len(clave)==6:
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False

def ingrese_perro(dict):
    nombre=input("Ingrese un nombre: ")
    raza=input("Ingrese la raza: ")
    codigo=input("Ingrese su codigo: ")
    if valida_pass(codigo): 
        largo=list(dict.keys())[-1]
        dict[largo+1]={"Nombre": nombre,
                        "Raza": raza,
                        "Codigo": codigo}
    else:
        print("El parametro de la clave no es correcto")
        
def act_perros(dict):
    mostrar_perros(dict)
    act=int(input("Seleccione el perro a actualizar: "))
    print('''
          1.- Nombre
          2.- Raza
          3.- Codigo
          4.- Salir
          ''')
    dato=int(input("¿Que dato va a actualizar?: "))
    while True:
        match dato:
            case 1:
                n=input("Ingrese el nuevo nombre: ")      
                dict[act]["Nombre"]=n
            case 2:
                n=input("Ingrese la raza nueva: ")
                dict[act]["Raza"]=n
            case 3:
                n=input("Ingrese el codigo nuevo: ")
                if valida_pass(n):
                    dict[act]["Codigo"]=n
                else: 
                    print("El parametro de la clave no es correcto")
            case 4:
                break
            case _:
                print("Ingrese una opción valida: ")        

def borrar_perros(dict):
    mostrar_perros(dict)
    borrar=int(input("Seleccione el perro a borrar: "))
    del dict[borrar]
    
while True:
    try:
        print('''
              1.- Registrar un perro
              2.- Mostrar perros
              3.- Actualizar perro
              4.- borrar perro
              5.- Salir
              ''')
        op=int(input("Seleccione una opción: "))
        match op:
            case 1:
                ingrese_perro(perros)
            case 2:
                mostrar_perros(perros)
            case 3:
                act_perros(perros)
            case 4:
                borrar_perros(perros)
            case 5:
                print("Saliendo del sistema...")
            case _:
                print("Seleccione una opción valida")
    except Exception as error:
        print("Error, a cometido un error", error)

























