'''Reusando la función anterior defina una función que devuelva si un número es par.'''


import math

def multiplicidad(num1:int, num2:int)->bool:
    if num1%num2==0:
        multiplicidad=True

    else:
        multiplicidad=False
    return multiplicidad

def paridad(n:int)->bool:
    return multiplicidad(n, 2)

    #Se invoca un Print para comprobar con un ejemplo si funciona
#print(paridad(5))