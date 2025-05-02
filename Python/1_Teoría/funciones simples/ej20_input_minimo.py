'''Dados dos números n y m defina una función que lea desde teclado n números
enteros y devuelva el mínimo. Ídem para el máximo.'''


def minimo_n_valores(n:int)->int:
    minimo=int(input("dame numero entero: \n"))
    for i in range (n-1):
        x=int(input("dame numero entero: \n"))
        if x<minimo:
            minimo=x
    return minimo

def maximo_n_valores(n:int)->int:
    maximo=int(input("dame numero entero: \n"))
    for i in range (n-1):
        x=int(input("dame numero entero: \n"))
        if x<maximo:
            maximo=x
    return maximo