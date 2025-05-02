'''Defina una función tal que dado el radio de un círculo devuelva su área y su longitud.'''


import math

def area_longitud_circulo(radio:float)->tuple[float, float]:
    area=math.pi*radio**2
    longitud=math.pi*2*radio
    return area, longitud

valor_area, valor_longitud= area_longitud_circulo(1) #Se marca 1 para asignarlo al radio y hacer una cuenta en base al radio=1

print(valor_area)
print(valor_longitud)