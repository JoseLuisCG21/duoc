
productos = []

listaProductos = []

while True:
    op=int(input('''Ingrese una opción:
        1.- Agregar productos a la lista
        2.- eliminar productos de la lista
        3.- mostrar productos de la lista de forma ordenada
        4.- salir del sistema'''))
    match op:
        case 1:
            nombreProducto = input("Ingrese producto: ")
            listaProductos.append(nombreProducto)
        case 2:
            cont = 1
            for i in listaProductos:
                print(f {cont}, -{i})
        case 3:
        case 4:
        case _:


