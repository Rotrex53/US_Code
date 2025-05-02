'''Dados dos números enteros n y m devuelva la suma de los números entre n y m
ambos inclusive. Tenga presente que n puede ser menor que m, igual o mayor. Por
ejemplo si la función se invoca suma_entre(5,7) devuelve 18 y si se invoca
suma_entre(8,5) devuelve 26.'''


def suma_entre_dos(n:int, m:int)->int:
    suma=0
    if n <=m:
        for i in range(n, m+1):
            suma+=1
    else:
        for i in range(m, n+1):
            suma+=1
    return suma

#print(suma_entre_dos(8,345))