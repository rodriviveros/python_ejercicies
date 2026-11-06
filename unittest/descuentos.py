def descuento_producto(precio, porcentaje):
    if precio > 100000:
        porcentaje=porcentaje+5
    return precio - (precio * porcentaje/100)

# print (descuento_producto(20000, 10))
# print(descuento_producto(200000,10))
# print(descuento_producto(100000,10))

# assert descuento_producto(20000, 10) == 18000
# assert descuento_producto(100000, 10) == 90000
