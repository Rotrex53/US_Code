from typing import NamedTuple
import csv
from coordenadas import *


CentroSanitario = NamedTuple("CentroSanitario", (("nombre", str),("localidad", str),("coordenadas", Coordenadas),
                                                ("estado", str),("num_camas", int),("acceso_discapacitado", bool),("tiene_uci", bool)))

'''leer_centros: recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de tipo 
CentroSanitario(str, str, Coordenadas(float, float), str, int, bool, bool) conteniendo todos los datos almacenados en el fichero.'''
def leer_centros(archivo:str)->list[CentroSanitario]:
    with open(archivo, encoding="utf-8") as f:
        lectura=[]
        lector=csv.reader(f, delimiter=";")
        next(lector)

        for nombre, localidad, latitud, longitud, estado, num_camas, acceso_discapacitado, tiene_uci in lector:
            coordenadas=Coordenadas(float(latitud), float(longitud))
            num_camas = int(num_camas)
            if acceso_discapacitado == "true":
                acceso_discapacitado = True
            if acceso_discapacitado == "false":
                acceso_discapacitado = False
            if tiene_uci == "true":
                tiene_uci = True
            if tiene_uci == "false":
                tiene_uci = False

            r=CentroSanitario(nombre, localidad, coordenadas, estado, num_camas, acceso_discapacitado, tiene_uci)
            lectura.append(r)

    return lectura

'''calcular_total_camas_centros_accesibles: recibe una lista de tuplas de tipo CentroSanitario y 
produce como salida un entero correspondiente al número total de camas de los centros sanitarios accesibles para discapacitados.'''
def calcular_total_camas_centros_accesibles(lista_r:list[CentroSanitario])->int:
    suma=0
    for r in lista_r:
        if r.acceso_discapacitado==True:
            suma+=r.num_camas

    return suma

