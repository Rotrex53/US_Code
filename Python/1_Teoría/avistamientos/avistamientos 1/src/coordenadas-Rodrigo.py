from avistamientos1 import *
import math

def distancia(c1:Coordenadas, c2:Coordenadas)-> float:
    dif_lat = c1.latitud - c2.latitud
    dif_long = c1.longitud - c2.longitud
    resultado_distancia = math.sqrt(dif_lat**2 + dif_long**2)
    return resultado_distancia