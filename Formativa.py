
total=0
totaldes=0
codigo="soyotaku"
pik=0
ota=0
pul=0
ang=0

def Pikachu():
    global total
    total+=4500
    print("Lleva un Pikachu Roll $4.500")
    print(f"Su compra total es de {total}")
    
def Otaku():
    global total
    total+=5000
    print("Lleva un Otaku Roll $5.000")
    print(f"Su compra total es de {total}")

def Pulpo():
    global total
    total+=5200
    print("Lleva un Pulpo venenoso Roll $5.200")
    print(f"Su compra total es de {total}")
    
def Anguila():
    global total
    total+=4800
    print("Lleva una Aguila electrica Roll $4800")
    print(f"Su compra total es de {total}")
    


while True:
    op=int(input('''Seleccione una opcion: 
            1.- Pikachu Roll $4500
            2.- Otaku Roll $5000
            3.- Pulpo Venenoso Roll $5200
            4.- Anguila Eléctrica Roll $4800
            5.- Completar pedido
                 '''))
    match op:
        case 1:
            Pikachu()
            pik+=1
        case 2:
            Otaku()
            ota+=1
        case 3:
            Pulpo()
            pul+=1
        case 4:
            Anguila()
            ang+=1
        case 5:
            break
des=int(input('''Tiene un cupon de descuento??:
               1.- Si
               2.- No'''))
if des==1:
    codigo=str(input("Ingrese el codigo de descuento: "))
    if codigo=="soyotaku":
        print("Su codigo de descuento es valido, el descuento es del 10%.")
        totaldes+=total
        des=totaldes*0.1
        totaldes=totaldes-des
        
    else:
        print("El codigo es invalido")


print(f''' 
******************************
TOTAL PRODUCTOS: {(pik+ota+pul+ang)}
******************************
Pikachu Roll : {pik}
Otaku Roll : {ota}
Pulpo Venenoso Roll: {pul}
Anguila Eléctrica Roll: {ang}
******************************
Subtotal por pagar: {total}
Descuento por código: {des}
TOTAL: {totaldes} ''')


