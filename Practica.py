# email = input("Ingrese su email: ")
# if "@" in email:
#     print("La variable tiene formato email")
# else:
#     print("La variable NO tiene formato email")

# while True:
#     try:
#         pin = int(input("Ingrese su PIN: "))
#         break
#     except Exception:
#         print("Error, Ingrese numeros enteros")
        
        
        
# clave = input("Ingrese su clave: ")

# if len(clave)>=5:
#     print("La clave tiene el largo correcto")
# else:
#     print("La clave debe tener al menos 5 caracteres")

# if len(clave)>=5 and len(clave)<=12:
#     print("La clave tiene el largo correcto")
# else:
#     print("La clave debe tener minimo 5 y maximo 12 caracteres")



tieneMayus = False
tieneMinus = False
tieneNumero = False

# #Se hace un recorrido en cada letra de la clave
# for letra in clave:
#     #verifico si la letra es mayuscula
#     if letra.isupper():
#         tieneMayus = True
#     #verifico que la letra es minuscula
#     if letra.islower():
#         tieneMayus = True
#     #Verifico si tengo un numero
#     if letra.isdigit():
#         tieneNumero = True

# if tieneMayus:
#     print("Tiene por lo menos una mayuscula")
# else: 
#     print(" NO tiene por lo menos una mayuscula")
# if tieneMinus:
#     print("Tiene por lo menos una minuscula")
# else: 
#     print(" NO tiene por lo menos una minuscula")

# if tieneMayus and tieneMinus and tieneNumero:
#     print("La clave esta bien")
# else:
#     print("Debe intentar nuevamente")



# Repaso de listas y diccionarios
clave="jKu46"
perros = [
        1:{"Nombre" : "Droopy",
            "Raza" : "Dog hount",
            "Codigo" : "Dphh06"}
    ]
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
            Número=True
    if (Mayuscula and Minuscula and Numero) and len(clave)==6:
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False
valida_pass(clave)

def ingresa_perro(dict):
    nombre = input("Ingrese un Nombre: ")
    raza = input("Ingrese su raza: ")
    codigo = input("Ingrese su codigo: ")
    if valida_pass(codigo):
        largo = list(dict.keys())[-1]
        dict[largo+1] = {"Nombre" : nombre,
                            "Raza" : raza ,
                            "Codigo" : codigo}

def mostrar_perros(dict):
    for key, perro in dict.items():
                print(key, perro)

def act_perros(dict):
    mostrar_perros(perros)
    act = int(input("Seleccione el perro que va a actualizar: "))
    while True:
        print('''
            1.- Nombre
            2.- Raza
            3.- Codigo
            4.- Salir
            ''')
        dato = int(input("¿Que dato va a actualizar?: "))
        match dato:
            case 1:
                n = input("Ingrese el nuevo nombre: ")
                perros[act]["nombre"] = n
            case 2:
                n = input("Ingrese la nueva raza: ")
                perros[act]["raza"] = n
            case 3:
                n = input("Ingrese el nuevo codigo: ")
                if valida_pass(n):
                    perros[act][]
                    
                perros[act]["codigo"] = n
            case 4:
                print("Saliendo...")
                break
            case _:
                perros[act]

def borrar_perros(dict):
        borrar = int(input("Seleccione el perro a borrar: "))
        del perros[borrar]

while True:
    try:
        print('''
              1.- Registrar un perro
              2.- Mostrar perros
              3.- Actualizar perro
              4.- Borrar perro
              5.- Salir
              ''')
        
    op=int(input("Seleccione una opción: "))
    match op:
        case 1:
            ingresa_perro(dict)
        case 2:
            mostrar_perros(perros)
        case 3:
            act_perros(perros)
        case 4:
            borrar_perros(dict)
            
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Opción invalida")
            
    except Exception:
    print("El error es: ")
        
        
        

    