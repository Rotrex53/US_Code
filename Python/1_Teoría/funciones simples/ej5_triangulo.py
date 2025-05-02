'''Tres segmentos de longitudes a, b y c pueden constituir un triángulo si la suma de dos
cualesquiera de ellos es mayor que el tercero (debe cumplirse para todas las parejas).
Por ejemplo, 7, 4 y 5 sí pueden constituir un triángulo porque 4+5>7, 7+5>4 y 7+4>5,
pero 10, 3 y 4 no, ya que 4+3<10. Implemente una función que devuelva cierto si tres
longitudes pueden formar un triángulo.'''


import math

#a=input("v1: \n")
#b=input("v2: \n")
#c=input("v3: \n")
def forman_triangulo(a:float, b:float, c:float)->bool:
    if a+b>c and b+c>a and a+c>b:
        triangulo=True
    else:
        triangulo=False
    return triangulo

    #Se invoca un Print para comprobar con un ejemplo si funciona
#print(forman_triangulo(a,b,c))
