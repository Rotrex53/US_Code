'''Para definir una función tal que dado un número entero devuelva si un número es
primo, puede hacerse definiendo la función directamente o bien definir la función que
devuelva si un número es compuesto y después se niegue. '''
#recordar que primo es opuesto a compuesto

'''
esquema existe(coleccion de elementos, condicion)
    existe=Falso
    hacemos un recorrido de la coleccion
        si el elemento cumple la condicion
            existe=Verdad
            break
    devuelve existe
'''
def es_compuesto(n:int)->bool:
    existe=False
    for i in range(2,n):
        if es_compuesto(n,i):
            existe=True
            break
    return existe

def es_primo(n:int)->bool:
    return not es_compuesto(n)

'''
esquema paraTodo(coleccion, condicion)
    paraTodo=Verdad
    recorremos la coleccion:
        si el elemento cumple la condicion:
            paraTodo=Verdad
        sino:
            paraTodo=Falso
            break
    devuelve paraTodo


esquema paraTodo_mejor(coleccion, condicion)
    paraTodo=Verdad
    recorremos la coleccion:
        si el elemento NO cumple la condicion:
            paraTodo=Falso
            break
    devuelve paraTodo
'''

def es_primo(n:int)->bool:
    paraTodo=True
    for i in range(2,n):
        if es_compuesto(n,i):
            paraTodo=False
            break
    return paraTodo