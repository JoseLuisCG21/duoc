# def cal_iva(n):
#     return n*0.19

# def cal_desc(precio, porc):
#     return precio*(porc/100)

# neto=1500

# print("El IVA es", cal_iva(neto))
# print("El precio total es", cal_iva(neto)*neto)

productos=[
    {"Nombre":"Lapiz", "Precio": 400},
    {"Nombre":"Goma", "Precio": 200},
    {"Nombre":"Estuche", "Precio": 1600}
    ]
for producto in productos:
    print("El precio del articulo ",producto["Nombre"], "es ", producto ["Precio"])
    
while True:
    print('''
          1.- Agregar articulo
          2.- Borrar articulo
          3.- Actualizar articulo
          4.- Mostrar listado de articulos
          5.- Salir
          ''')
    op=int(input("Seleccione una opcion" ))
    match op:
        case 1:
            nombre=input("Ingrese el nombre del articulo")
            precio=int(input("Ingrese el nombre del precio"))
            productos.insert(0,{"Nombre": nombre, "Precio": precio})
        case 2:
            for producto in enumerate(productos):
            productos.remove(0,{"Nombre": nombre, "Precio": precio})
        case 3:
            productos.sort()
        case 4:
            print()
        case 5:
            print()
        case _:
            print()