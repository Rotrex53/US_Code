'''Repita los ejercicios anteriores pero dividiendo el problema en dos partes. Una función
que lea los números y los guarde en una lista y después invoque a los métodos sum,
len, min o max a partir de la lista creada.'''
from ej18_input_suma_multiplos import es_multiplo
from ej18_input_suma_multiplos import x

def lee_lista_numeros(n:int)->list[int]:
    lista=[] #tambien valido: lista=list()
    for i in range(n):
        x=int(input("dame un numero entero: \n"))
        lista.append(x)
    return lista

def maximo_n_valores2(n:int)->int:
    l=lee_lista_numeros(n)
    return max(1)

def suma_n_multiplos2(n:int, m:int)->int:
    l=lee_lista_numeros(n)
    lista_fil=[x for x in l if es_multiplo(x,m)] #Esto significa: la lista esta formada por aquellos x, tales que cumplen es_multiplo(x,m)
    return sum(lista_fil)

#las lineas: 24/29=18/20
'''
lista_fil=[]
for x in lista:
    if es_multiplo(x,m):
        lista_fil.append(x)
'''




'''
lista=[2,3,6,-1,5]
print(lista[2])
print(len(lista))
print(sum(lista))
print(min(lista))
print(max(lista))
print(lista)
print(lista[0:3])
print(lista[:3])
'''