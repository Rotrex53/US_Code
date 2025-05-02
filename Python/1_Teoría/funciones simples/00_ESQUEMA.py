#EXISTE
'''
esquema existe(coleccion de elementos, condicion )
existe=Falso
hacemos un recorrido de la coleccion
si el elemento cumple la condicion
existe=Verdad
break
devuelve existe
'''
from ej10_multiplicidad import multiplicidad

def es_compuesto(n:int)->bool:
    existe=False
    for i in range (2,n):
        if multiplicidad(n,i):
            existe=True
            break
    return existe

def es_primo(n:int)->bool:
    return not es_compuesto(n)


#PARA_TODO
'''
esquema paraTodoMejor(coleccion, condicion)
paraTodo=verdad
recorremos la coleccion:
si el elemento NO cumple la condicion
paraTodo=falso
break
devuelve paraTodo
'''

def es_primo(n:int)->bool:
    paraTodo=True
    for i in range (2,n):
        if multiplicidad(n,i):
            paraTodo=False
        break
    return paraTodo