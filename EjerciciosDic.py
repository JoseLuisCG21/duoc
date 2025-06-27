Vehiculos ={
    1: {"Marca": "Audi",
        "Año": 2000,
        "Patente": "jk32",
        "Tipo": "Camioneta",}
        }

def valida_placa(patente):
    minusculas=False
    numeros=False
    for palabra in patente:
        if palabra.islower():
            minusculas=True
        if palabra.isdigit():
            numeros=True
        if minusculas and numeros and len(patente)==6:
            print("La placa cumple con lo requerido")
            return True
        else:
            print("Error al ingresar la placa, debe tener 4 letras minusculas y 2 numeros")
            return False

def ingresar_vehiculo(dict):
    marca=input("Ingrese la marca del vehiculo: ")
    año=int(input("Ingrese el año del vehiculo: "))
    tipo=('''
          Ingrese el tipo de vehiculo:
          1.- Sedan
          2.- Camioneta
          3.- moto
          ''')
    patente=input("Ingrese la patente del vehiculo: ")
    if valida_placa(patente):
        largo=list(dict.keys())[-1]
        dict[largo+1]={"Marca": marca,
                        "Año": año,
                        "Patente": patente,
                        "Tipo": tipo,}
    else:
        print("Los parametros de la placa no es correcta")
     
def mostrar_vehiculos(list):
    for keys, vehiculo in Vehiculos.items():
        print(keys, vehiculo)
     
     
while True:
    try:
        print('''
              1.- Ingresar vehiculo
              2.- Mostrar vehiculo
              3.- Actualizar vehiculo
              4.- Borrar vehiculo
              5.- Mostrar estadisticas
              6.- Salir 
              ''')
        op=int(input("Seleccione una opción: "))
        match op:
            case 1:
                ingresar_vehiculo(Vehiculos)
            case 2:
                mostrar_vehiculos(Vehiculos)
                
            case 6:
                print("Saliendo del sistema...")
                break
            case _:
                print("Ingrese una opción valida: ")
            
            
            
    except Exception as e:
        print("Error, a cometido un error", e)