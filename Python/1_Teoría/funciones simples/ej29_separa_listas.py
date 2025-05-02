'''Define una función que haga el proceso inverso al del ejercicio anterior.'''


def separa_listas(lista:list[tuple[int,int]])->tuple[list[int],list[int]]:
    lista1=lista2=list()
    for tupla in lista:
        lista1.append(tupla[0])
        lista2.append(tupla[1])
    return (lista1, lista2)

def separa_listas2(lista:list[tuple[int,int]])->tuple[list[int],list[int]]:
    lista1=lista2=list()
    for x,y in lista:
        lista1.append(x)
        lista2.append(y)
    return (lista1, lista2)

def separa_listas3(lista:list[tuple[int,int]])->tuple[list[int],list[int]]:
    return ([x for x,_ in lista], [y for _,y in lista])