import math

def suma_n_primeros_num(n:int)->int:
    suma=0
    for i in range(1, n+1):
        print(i, suma)
        suma=suma+i
    return suma

#Se invoca un Print para comprobar con un ejemplo si funciona
print(suma_n_primeros_num(4))