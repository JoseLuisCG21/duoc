#Tienda de videojuegos
import time
total=0
CantProducto=0
cantPS=0
cantXbox=0
cantNintendo=0
des=0
totaldes=0

while True:
    op=int(input('''
                 Escoja el catalogo de VideoJuegos: 
                 
                 1.- PlayStation 5
                 2.- Xbox Series X/S
                 3.- Nintendo Swich 2
                 4.- Ver recibo 
                 5.- Pagar y finalizar compra
                 '''))
    match op:
        case 1:
            while True:
                op=int(input('''
                             Seleccione el juego a comprar:
                             
                             1.- Grand theft auto VI $90.000
                             2.- God Of War Ragnarok $45.000
                             3.- Stellar Blade $50.000
                             4.- Salir'''))
                match op:
                    case 1:
                        total+=90000
                        CantProducto+=1
                        cantPS+=1
                        print("Agrego al carrito de compras Grand Theft Auto IV $90.000")
                        print(f"El total que lleva es de {total}")
                    case 2:
                        total+=45000
                        CantProducto+=1
                        cantPS+=1
                        print("Agrego al carrito de compras God Of War Ragnarok $45.000")
                        print(f"El total que lleva es de {total}")
                    case 3:
                        total+=50000
                        CantProducto+=1
                        cantPS+=1
                        print("Agrego al carrito de compras Stellar Blade $50.000")
                        print(f"El total que lleva es de {total}")
                    case 4:
                        print("Saliendo del catalogo de PlayStation 5...")
                        time.sleep(2)
                        break
                    case _:
                        print("Error, ingrese una opcion valida")
        case 2:
            while True:
                op=int(input('''
                             Seleccione el juego a comprar:
                             
                             1.- Grand theft auto VI $90.000
                             2.- Forza Horizon 5 $43.000
                             3.- Halo infinite $37.000
                             4.- Salir'''))
                match op:
                    case 1:
                        total+=90000
                        CantProducto+=1
                        print("Agrego al carrito de compras Grand Theft Auto IV $90.000")
                        print(f"El total que lleva es de {total}")
                        cantXbox+=1
                    case 2:
                        total+=43000
                        CantProducto+=1
                        print("Agrego al carrito de compras Forza Horizon 5 $43.000")
                        print(f"El total que lleva es de {total}")
                        cantXbox+=1
                    case 3:
                        total+=50000
                        CantProducto+=1
                        print("Agrego al carrito de compras Halo infinite $37.000")
                        print(f"El total que lleva es de {total}")
                        cantXbox+=1
                    case 4:
                        print("Saliendo del catalogo de Xbox Series X/S...")
                        time.sleep(2)
                        break
                    case _:
                        print("Error, ingrese una opcion valida")
        case 3:
            while True:
                op=int(input('''
                             Seleccione el juego a comprar:
                             
                             1.- Mario Kart World $70.000
                             2.- Zelda Tears Of The Kingdom $60.000
                             3.- Xenoblade Chronicles 3 $60.000
                             4.- Salir'''))
                match op:
                    case 1:
                        total+=70000
                        CantProducto+=1
                        print("Agrego al carrito de compras Mario Kart World $70.000")
                        print(f"El total que lleva es de {total}")
                        cantNintendo+=1
                    case 2:
                        total+=60000
                        CantProducto+=1
                        print("Agrego al carrito de compras Zelda Tears Of The Kingdom $60.000")
                        print(f"El total que lleva es de {total}")
                        cantNintendo+=1
                    case 3:
                        total+=60000
                        CantProducto+=1
                        print("Agrego al carrito de compras Xenoblade Chronicles 3 $60.000")
                        print(f"El total que lleva es de {total}")
                        cantNintendo+=1
                    case 4:
                        print("Saliendo del catalogo de Nintendo Switch 2...")
                        time.sleep(2)
                        break
                    case _:
                        print("Error, ingrese una opcion valida")
        case 4:
            
            print(f''' 
                    ******************************
                    TOTAL PRODUCTOS: {CantProducto}
                    ******************************
                    Catalogo de PlayStation 5: {cantPS}
                    Catalogo de Xbox Series X/S: {cantXbox}
                    Catalogo de Nintendo Switch 2: {cantNintendo}
                    ******************************
                    Subtotal por pagar: {total}
                    Total a pagar con IVA: {total*1.19}
                     ''')
        case 5:
            des=int(input('''Tiene un cupon de descuento??: 
                          1.- Si
                          2.- No'''))
            if des==1:
                print("Su cupon es valido, y el descuento aplica un 10% de rebaja")
                total=total*0.1
            else:
                print("No se aplica ningun descuento.")
            fin=int(input(f''' 
                    ******************************
                    TOTAL PRODUCTOS: {CantProducto}
                    ******************************
                    Catalogo de PlayStation 5: {cantPS}
                    Catalogo de Xbox Series X/S: {cantXbox}
                    Catalogo de Nintendo Switch 2: {cantNintendo}
                    ******************************
                    Subtotal por pagar: {total}
                    Total a pagar con IVA: {total*1.19}
                    
                    Desea realizar la compra??:
                    1.- Finalizar la compra
                    2.- Seguir comprando'''))
        



























































