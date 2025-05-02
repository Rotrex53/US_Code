'''Dadas dos listas de números representando dos vectores de valores numéricos,
devuelve el producto escalar de ambos vectores. Por ejemplo si las listas son [2, 3, 1] y
[3, 4, 7] el resultado debe ser 2x3+3x4+1x7=25. Compruebe que ambas listas son de la
misma longitud, si no devuelva None.'''


#solución 1
def producto_escalar(lista1:list[int], lista2:list[int])->int | None:
    if len(lista1)==len(lista2):
        suma=0
        for i in range(len(lista1)):
            suma+=lista1[i]*lista2[i]
        
    else:
        suma=None

    return suma

#resultado=producto_escalar([1,2,3], [4,5,6])
#print(resultado)

#solución 2
def producto_escalar2(lista1:list[int], lista2:list[int])->int | None:
    if len(lista1)==len(lista2):
        suma=0
        for i,x in enumerate(lista1):
            suma+=x*lista2[i]
        
    else:
        suma=None

    return suma

#solución 3
def producto_escalar3(lista1:list[int], lista2:list[int])->int | None:
    if len(lista1)==len(lista2):
        suma=0
        for x,y in zip(lista1,lista2):
            suma+=x*y
        
    else:
        suma=None

    return suma
