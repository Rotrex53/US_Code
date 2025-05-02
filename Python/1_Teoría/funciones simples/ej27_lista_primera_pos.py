'''Dado un número de una lista devuelva la primera posición en la que se encuentra. 
Por ejemplo, dada la lista [3, 5, 7, 8, 2, 8, 10] si se le da 8 debe devolver 3 
(su primera posición empezando en 0). Si el valor no estuviera devuelve None. 
Consulte si hay alguna función en Python que haga lo mismo y qué sucede si no está.'''


def posicion_lista(lista: list[int], x:int)->int| None:
    pos=None
    for i in range(len(lista)):
        if lista[i]==x:
            pos=i
        break
    return pos

def posicion_lista2(lista: list[int], x:int)->int| None:
    pos=None
    for i, elemento in enumerate(lista):
        if elemento==x:
            pos=i
        break
    return pos
