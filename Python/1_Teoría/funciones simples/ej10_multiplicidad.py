'''Defina una función que dados dos números enteros devuelva si el primero es múltiplo
del segundo.'''


import math

def multiplicidad(num1:int, num2:int)->bool:
    if num1%num2==0:
        multiplicidad=True

    else:
        multiplicidad=False
    return multiplicidad

    #Se invoca un Print para comprobar con un ejemplo si funciona
#print(multiplicidad(3,6))