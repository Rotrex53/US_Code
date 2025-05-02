from sevici import *
from typing import NamedTuple
import csv
import math 
import folium


Coordenadas = NamedTuple('Coordenadas', [('latitud', float), ('longitud', float)])

def funcion_coordenadas(coordenada1: Coordenadas, coordenada2: Coordenadas) -> float:
    return math.sqrt((coordenada1.latitud - coordenada2.latitud)**2 + (coordenada1.longitud - coordenada2.longitud)**2)