#Nuevos diccionarios y manipulación de datos

juegos = [
    1:{
        "Nombre" : "metroid dread",
        "Precio" : 50000,
        "Code" : "Mdd23",
    }
    2:{
        "Nombre" : "pikmin",
        "Precio" : 50000,
        "Code" : "Kgr195",
    }
]



def valida_pass(code):    
    Mayuscula=0
    Minuscula=0
    Numero=0

    for palabra in code:
        if palabra.isupper():
            Mayuscula=True
        if palabra.islower():
            Minuscula=True
        if palabra.isdigit():
            Número=True
    if (Mayuscula==2 and Minuscula==2 and Numero) and len(code)==4:
        print("El codigo esta bien escrito")
        return True
    else:
        print("El codigo esta bien escrito")
        return False
valida_pass(code)


for j, datos in juegos.items():
    print(j, datos)
while True:
    try:
        print('''
            1.- Agregar juego
            2.- Mostrar juegos
            3.- Actualizar juegos
            4.- Borrar juegos
            5.- Salir''')
        op=int(input("Seleccione una opción: "))
        match op:
            case 1:
                nombre=input("Ingrese el nombre del juego")
                precio=int(input("Ingrese el precio"))
                code=input("Ingrese el codigo")
                if valida_pass(code):
                    largo=len(juegos)
                    juegos=[largo+1]={
                        "nombre" : nombre,
                        "precio" : precio,
                        "code" : code
                    }
            case 2: 
                for j, datos in juegos.items():
                    print(j, datos)
            case 3: 

            case 4: 
            case 5: 
                print("Saliendo del sistema...")
                break
            case _: 
                print("Onpión invalida")
    except Exception:
        print("")