'''Implemente una función que reciba una tupla de dos enteros distintos y devuelva 1 
si el primer valor es mayor que el segundo y 2 en caso contrario. 
Reutilizando esa función implemente otra que reciba una lista de tuplas con los resultados 
de un partido de tenis a tres sets y debe devolver un 1 o un 2 según el ganador del partido 
sea el primer jugador o el segundo. Un partido lo gana el jugador que gane dos sets de los tres 
y un set se gana si tiene más juegos que el contrario. Por ejemplo si la lista es [(6,1),(4,6),(7,6)] 
gana el jugador 1 porque gana el primer set (6 juegos a 1) y el tercero (7-6). 
Si la lista es [(6,1),(4,6),(2,6)] gana el jugador 2 que gana el 2º y 3º set.'''


def gana_set(parcial:tuple[int,int])->int:
    ganador=1
    if parcial[1]>parcial[0]:
        ganador=2
    return ganador

def gana_partido(resultado:list[tuple[int,int]])->int:
    jug1,jug2=0
    for resultado_set in resultado:
        if gana_set(resultado_set)==1:
            jug1+=1
        else:
            jug2+=1
    if jug1>jug2:
        ganador=1
    else:
        ganador=2
    return ganador