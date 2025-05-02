'''Tenemos dos listas pareadas (del mismo tamaño) y queremos definir una función que devuelva una lista
 formada por las tuplas de los elementos de las dos listas. Por ejemplo, si tenemos [3, 4, 7] y [2, -1, 4]
   devolvemos [(3, 2), (4,-1), (7,4)].'''


#tupla1=("Juan", 2, 5.4)
#tupla2=("Ana", 4, 5.6)
#print(tupla1[0])

#tupla1=("Pepe", tupla1[1], tupla2[2])
#print(tupla1) 

def una_listas(lista1:list[int], lista2:list[int])->list[tuple[int,int]]:
    lista=[]
    for i in range(len(lista1)):
        tupla=(lista1[i], lista2[i])
        lista.append(tupla)
        lista.append((lista1[i], lista2[i]))
    return lista

def una_listas2(lista1:list[int], lista2:list[int])->list[tuple[int,int]]:
    lista=[]
    for x,y in zip(lista1, lista2):
        lista.append((x,y))
    return lista