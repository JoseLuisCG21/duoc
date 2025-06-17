# def cal_iva(n):
#     return n*0.19

# def cal_desc(precio, porc):
#     return precio*(porc/100)

# neto=1500

# print("El IVA es", cal_iva(neto))
# print("El precio total es", cal_iva(neto)*neto)

productos=[
    {"Nombre":"Lapiz", "precio":400},
    {"Nombre":"Goma", "Precio":200},
    {"Nombre":"Estuche", "Precio":1600}
    ]
for producto in productos:
    print("El precio del articulo ", producto["Nombre"], "es", producto["Precio"])