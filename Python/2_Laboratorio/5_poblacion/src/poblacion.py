from typing import NamedTuple
import csv
import matplotlib.pyplot as plt

RegistroPoblacion = NamedTuple('RegistroPoblacion',[("pais",str),("codigo",str),("año",int),("censo",int)])


def lee_poblaciones(population_csv:str)->list[RegistroPoblacion]:
    with open(population_csv, encoding="utf-8") as f:
        lista_poblaciones=[]

        lector=csv.reader(f)

        for pais,codigo,año,censo in lector:
            año=int(año)
            censo=int(censo)

            r=RegistroPoblacion(pais,codigo,año,censo)

            lista_poblaciones.append(r)

        return lista_poblaciones
    

def calcula_paises(lista_paises:list[RegistroPoblacion])->list[RegistroPoblacion]:
    conjunto=set()

    for r in lista_paises:
        conjunto.add(r.pais)
    lista_paises_conjunto=list(conjunto)

    return lista_paises_conjunto


def filtra_por_pais(lista_registro:list[RegistroPoblacion], nombre_o_codigo:str)->list[RegistroPoblacion]:
    lista_filtrada=[]
    for registro in lista_registro:
        if registro.pais == nombre_o_codigo or registro.codigo == nombre_o_codigo:
            lista_filtrada.append(registro.año)
            lista_filtrada.append(registro.censo)

    return lista_filtrada

def filtra_por_paises_y_año(lista_registro:list[RegistroPoblacion], año:int, lista_varios_paises:set)->list:
    lista_filtrada=[]
    for registro in lista_registro:
        if registro.año == año and registro.pais in lista_varios_paises:
            lista_filtrada.append(registro.pais)
            lista_filtrada.append(registro.censo)

    return lista_filtrada


def muestra_evolucion_poblacion(lista_registro:list[RegistroPoblacion], nombre_o_codigo:str):
    lista_años=[]
    lista_habitantes=[]
    for registro in lista_registro:
        if registro.pais == nombre_o_codigo or registro.codigo == nombre_o_codigo:
            lista_años.append(registro.año)
            lista_habitantes.append(registro.censo)

    return lista_años, lista_habitantes


def muestra_comparativa_paises_año(lista_registro:list[RegistroPoblacion], año:int, lista_varios_paises:set)->list:
    lista_paises=[]
    lista_habitantes=[]
    for registro in lista_registro:
        if registro.pais in lista_varios_paises and registro.año == año:
            lista_paises.append(registro.pais)
            lista_habitantes.append(registro.censo)
    lista_paises.sort()
        
    return lista_paises, lista_habitantes