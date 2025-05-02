'''Dados dos números n y m defina una función que lea desde teclado n números
enteros y devuelva la suma de los múltiplos de m. '''

from ej10_multiplicidad import es_multiplo


def suma_n_multiplos(n:int, m:int)->int:
    suma=0
    for i in range(n):
        x=int(input("dame un numero entero: \n"))
        if es_multiplo(x, m):
            suma+=x
    return suma