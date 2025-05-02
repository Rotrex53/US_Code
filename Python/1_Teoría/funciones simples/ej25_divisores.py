'''Dado un número entero positivo devuelve una lista con sus divisores excepto el 1. 
Por ejemplo, si se le da 12, devuelve [2, 3, 4, 6].'''
from ej22_primos import es_compuesto

def divisores(num:int)->list[int]:
    lista=[]
    for i in range(2,num):
        if es_compuesto(num,i):
            lista.append(i)
    return lista

print(divisores(24))