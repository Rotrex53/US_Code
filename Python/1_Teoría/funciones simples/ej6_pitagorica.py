'''Tres números forman una terna pitagórica si la suma al cuadrado de dos de ellos da el
tercero al cuadrado. Implemente una función tal que dados tres valores numéricos
enteros devuelva cierto si los tres valores forman una terna pitagórica.'''


import math

def terna_pitagorica(a:float, b:float, c:float)->bool:
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        terna=True
    else:
        terna=False
    return terna

    #Se invoca un Print para comprobar con un ejemplo si funciona
#print(terna_pitagorica(5,4,3))
