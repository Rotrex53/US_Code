'''Una cadena de caracteres es un palíndromo si tiene los mismos caracteres y 
en el mismo orden mirados de izquierda a derecha que de derecha a izquierda. 
Construya una función tal que dada una cadena de caracteres devuelva si es palíndromo o no. 
Pista: compare el primer carácter con el último, el segundo con el penúltimo, etc. 
Si alguna de estas comparaciones es falsa entonces la palabra no es palíndroma. 
Por ejemplo, son palíndromos “RADAR” o “RECONOCER”.'''
#palíndromo=se lee igual de izquierda a derecha que de derecha a izquierda


def es_palindromo(cadena:str)->bool: #solo hemos visto 2 exquemas que devuelvan bool, en este caso es un paraTodo
    palindromo=True
    for i in range(cadena):             #i es un iterable, una lista que se crea y se consume, empieza en 0
        if cadena[i]!=cadena[-i-1]:           #cadena[0]=primer caracter VS cadena[-1]=último caracter, etc...
            palindromo=False
    return palindromo


#segunda opcion
def voltear(cadena:str)->str:
    voltea=""
    for x in cadena:
        voltea=x+voltea
    return voltea
#print(voltear("AVION"))


def es_palindromo2(cadena:str)->bool:
    cadena_alreves=voltear(cadena)
    palindromo=True
    for i in range(len(cadena)):
        if cadena[i]!=cadena_alreves[i]:
            palindromo=False
    return palindromo

#print(es_palindromo2("RADAR"))

def es_palindromo3(cadena:str)->bool:
    cadena_alreves=voltear(cadena)
    return cadena==cadena_alreves

def es_palindromo4(cadena:str)->bool:
    return cadena==cadena[::-1]