import csv
import math 
import folium
from typing import NamedTuple
from coordenadas import *



Estacion = NamedTuple('Estacion', [('nombre', str), ("slots", int), ("empty_slots", int), ("bikes", int), ("coordenadas", Coordenadas)])
Coordenadas = NamedTuple('Coordenadas', [('latitud', float), ('longitud', float)])


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


def estaciones_bicis_libres(fichero: list[Estacion], k=5):
    lista_estaciones = [registro.bikes for registro in fichero]
    return sorted(lista_estaciones, key=lambda x: x, reverse=True)


def calcula_distancia(coord1:Coordenadas, coord2:Coordenadas)->float:
    calculo_realizado=funcion_coordenadas(coordenada1=coord1, coordenada2=coord2)
    return calculo_realizado


def estaciones_cercanas(fichero:list[Estacion], distancia, k)->list[list[float,str,int]]:
    lista_de_tuplas = []
    for registro in fichero:
        lista_de_tuplas.append([registro.coordenadas, registro.nombre, registro.bikes])

    return sorted(lista_de_tuplas, key=lambda x: x[0], reverse=False)[:k]

'''         PROPUESTA DE SOLUCIÓN
def estaciones_cercanas(fichero: list[Estacion], distancia: float, k: int, coord_referencia: Coordenadas) -> list[list[float, str, int]]:
    lista_de_tuplas = []
    for registro in fichero:
        dist = calcula_distancia(coord_referencia, registro.coordenadas)
        lista_de_tuplas.append([dist, registro.nombre, registro.bikes])

    lista_de_tuplas = sorted(lista_de_tuplas, key=lambda x: abs(x[0] - distancia))
    return lista_de_tuplas[:k]
'''