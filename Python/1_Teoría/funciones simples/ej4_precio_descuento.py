'''Defina una función tal que dado un precio y un descuento devuelva el nuevo precio.'''


import math

def precio_descuento(precio:float, descuento:float)->float:
    variacion=precio*descuento/100
    nuevo_precio=precio-variacion
    return nuevo_precio

#Se invoca un Print para comprobar con un ejemplo si funciona
print(precio_descuento(120,15))