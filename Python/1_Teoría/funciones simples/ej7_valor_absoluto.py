'''Defina una función valor_absoluto tal que dado un número entero n devuelve su valor
sin signo.'''


import math

#n=int(input("valor: \n"))
def valor_absoluto(n:int)->int:
    if n>0:
        valor=n

    else:
        valor=-n
    return valor

    #Se invoca un Print para comprobar con un ejemplo si funciona
#print(valor_absoluto(n))