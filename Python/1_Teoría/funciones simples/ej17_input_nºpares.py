'''Dado un número n defina una función que lea desde teclado n números enteros y
devuelva cuántos de ellos son pares. '''

from ej11_paricidad import es_par


def lee_n_numeros_pares(n:int)->int:
    for i in range(n):
        x=int(input("dame un número entero: \n"))
        if es_par(x):
            contador+=1
    return contador

#print(lee_n_numeros_pares(5))