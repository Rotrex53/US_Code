import datetime
import math
from typing import NamedTuple
import csv


lista1=[]
lista2=[]
fichero="./archivo.csv"
RegistroClima = NamedTuple("RegistroClima", [("fecha", datetime),
                        ("lluvia", float), ("temp_max", float), ("temp_min",float)])
lector=csv.reader(fichero)
fecha_cadena="2024/10/21"
letras="abcde"


def es_multiplo(n:int, m:int)->bool:
    if n%m==0:
        valor=True
    else:
        valor=False
    return valor

def es_par(n:int)->bool:
    return es_multiplo(n,2)

def funcion_principal():
    hola="hola"