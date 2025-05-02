from typing import NamedTuple
from math import sqrt

<<<<<<< HEAD
Coordenadas = NamedTuple("Coordenadas", ("latitud", float),("longitud", float))
=======
Coordenadas = NamedTuple("Coordenadas",(("latitud", float),("longitud", float)))
>>>>>>> beff0ad (centro sanitario)

def calcular_distancia(coord1: Coordenadas, coord2: Coordenadas) -> float:
    distancia_euclidea = sqrt((coord2.latitud - coord1.latitud)**2 + (coord2.longitud - coord1.longitud)**2)
    
    return distancia_euclidea


def calcular_media_coordenadas(coordenadas: list[Coordenadas])->Coordenadas:
    latitud_media = sum(coord.latitud for coord in coordenadas) / len(coordenadas)
    longitud_media = sum(coord.longitud for coord in coordenadas) / len(coordenadas)
    
    return Coordenadas(latitud_media, longitud_media)