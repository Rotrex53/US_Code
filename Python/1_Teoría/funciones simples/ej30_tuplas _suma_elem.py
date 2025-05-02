'''Dada una lista de tuplas de 3 elementos, implemente una función que devuelva cierto 
si se cumple que para todas las tuplas el primer elemento es mayor que la suma del segundo y tercero. 
Por ejemplo, para [(7,2,3),(11,4,5),(4,1,1),(8,2,3)] debe devolver cierto porque 7 es mayor que 2+3,11>4+5, 
4>1+1 y 8>2+3. Por el contrario [(5,2,3),(11,4,5),(4,1,1),(8,2,3)] devuelve falso porque 5 no es mayor que 2+3.'''


def para_todo_suma(lista:list[tuple[int,int,int]])-> bool:
    paraTodo=True
    for tupla in lista:
        if tupla[0]<=tupla[1]+tupla[2]:
            paraTodo=False
    return paraTodo

def para_todo_suma2(lista:list[tuple[int,int,int]])-> bool:
    paraTodo=True
    for x,y,z in lista:
        if x<=y+z:
            paraTodo=False
        break
    return paraTodo