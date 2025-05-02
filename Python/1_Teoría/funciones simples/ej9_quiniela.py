'''. Defina una función tal que dado el resultado de un partido devuelva el signo de la
quiniela.'''


import math

def resultado_quiniela(gol_loc:int, gol_vis:int)->str:
    if gol_loc>gol_vis:
        resultado_quiniela="1"
    elif gol_loc<gol_vis:
        resultado_quiniela="2"
    else:
        resultado_quiniela="x"
    return resultado_quiniela

    #Se invoca un Print para comprobar con un ejemplo si funciona
#print(resultado_quiniela(2,3))