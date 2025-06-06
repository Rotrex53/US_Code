import csv
import math 
import folium
from typing import NamedTuple



Coordenadas = NamedTuple('Coordenadas', [('latitud', float), ('longitud', float)])
Estacion = NamedTuple('Estacion', [('nombre', str), ("slots", int), ("free_slots", int), ("bikes", int), ("coordenadas", Coordenadas)])


def leer_estaciones(fichero: str) -> list[Estacion]:
    estaciones = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)

        for nombre, slots, free_slots, bikes, latitud, longitud in lector:
            slots = int(slots)
            free_slots = int(free_slots)
            bikes = int(bikes)
            coordenadas=Coordenadas(float(latitud), float(longitud))
            r=Estacion(nombre, slots, free_slots, bikes, coordenadas)
            estaciones.append(r)

    return estaciones


def estaciones_bicis_libres(estaciones, k=5):
    return sorted(estaciones, key=lambda x: x.bikes, reverse=True)[:k]