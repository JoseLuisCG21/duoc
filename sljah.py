#ejercicio 2

entradas=20

try: 
    while True:
        op=int(input('''***** Cine Estrella *****
        Bienvenido al sistema de venta de entradas del Cine Estrella
        1. Ver entradas disponibles
        2. Comprar entradas
        3. Salir
        Selecciona una opción (1-3): '''))
        match op:
        case 1:
            print(f"Entradas disponibles: {entradas}")
        case 2:
            comprar=int(input("Ingrese la cantidad de entradas que quiera llevar: "))
            entradas=entradas-comprar
            if entradas>comprar:
            entradas=entradas-comprar
            print("Compra exitosa!")
            elif entradas<comprar:
            print("Error, su compra supera la cantidad disponible")
        case 3:
            print("Saliendo del sistema...")
            break
        case _:
            print("Error, solo ingresar opcion de 1 a 3")

except Exception:
    print("Error, solo debe ingresar numeros enteros")
 

# #ejercicio 1

# try:
#     cant=int(input("Ingrese la cantidad de empleados a ingresar: "))
#     while True:
#         empleado=input("Ingrese el nombre del empleado: ")
#         edad=int(input("Ingrese la edad del empleado (solo numeros enteros): "))
#         if edad<=10:
#             print("El empleado tiene mas de 10 años de antiguedad")
#         elif edad>10:
#             print("El empleado tiene menos de 10 años de antiguedad")
#             cant-=1
# except Exception:
#     print("Solo puede ingresar numero enteros en edad")
#     print("En el nombre del empleado solo puede poner texto")