'''Dada una cadena de caracteres que representa un número entero devuelva la suma de las cifras. 
Por ejemplo si se le da “3256” devuelve 16, si se le da “555” devuelve 15.'''


def suma_cifras(cadena:str)->int:
    suma=0
    for caracter in cadena:
        suma += int(caracter) #el int convierte caracter (que es un str) a un int
    return suma
