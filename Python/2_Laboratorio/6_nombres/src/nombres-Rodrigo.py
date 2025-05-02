from typing import NamedTuple
from datetime import date
import csv
import matplotlib.pyplot as plt

'''reciclar para el 4 el 2, para el 5 y 6 el 3'''

FrecuenciaNombre = NamedTuple("FrecuenciaNombre", [("año",date),("nombre",str),("frecuencia",int),("genero",str)])


def leer_frecuencias_nombres(nombres_csv:str)->list[FrecuenciaNombre]:
    with open(nombres_csv, encoding="utf-8") as f:
        lista_nombres=[]
        lector=csv.reader(f)
        next(lector)
    
        for año,nombre,frecuencia,genero in lector:
            año=int(año)
            nombre=str(nombre)
            frecuencia=int(frecuencia)
            genero=str(genero)

            r=FrecuenciaNombre(año,nombre,frecuencia,genero)

            lista_nombres.append(r)

    return lista_nombres


def filtrar_por_genero(lista_fichero:list[FrecuenciaNombre], genero:str)->list[FrecuenciaNombre]:
    lista_por_genero=[]

    for registro in lista_fichero:
        if genero == registro.genero:
            tupla = (registro.año, registro.nombre, registro.frecuencia)
            lista_por_genero.append(tupla)
        if genero == None:
            for registro in lista_fichero:
                lista_por_genero.append(registro.nombre)
            return lista_por_genero
    return lista_por_genero


def calcular_nombres(lista_fichero: list[FrecuenciaNombre], genero: str) -> set[str]:
    conjunto_nombres = set()

    filtro = filtrar_por_genero(lista_fichero, genero)
    for tupla in filtro:
        if genero == None:
            for registro in lista_fichero:
                conjunto_nombres.add(registro.nombre)
            return conjunto_nombres
        else:
            año, nombre, frecuencia = tupla  # Descomponer la tupla explícitamente      or: _,nombre,_
            conjunto_nombres.add(nombre)     # Solo trabajamos con el nombre
        

    return conjunto_nombres

'''conjunto_nombres = set()

# Reutilizamos la función filtrar_por_genero para obtener las tuplas
filtro = filtrar_por_genero(lista_fichero, genero)

# Extraer los nombres de las tuplas (año, nombre, frecuencia)
for _, nombre, _ in filtro:
    conjunto_nombres.add(nombre)

return conjunto_nombres'''


def calcular_top_nombres_de_año(lista_fichero: list[FrecuenciaNombre], año:int, num_limite:int, genero:str)->list[str, int]:
    lista_top_nombres=[]
    for r in lista_fichero:
        if len(lista_top_nombres)<num_limite:
            if r.genero==genero and r.año==año:
                lista_top_nombres.append((r.nombre,r.frecuencia))
            if genero == None:
                for registro in lista_fichero:
                    lista_top_nombres.append(registro.nombre)
                return lista_top_nombres

    lista_top_nombres.sort(key=lambda x: x[1], reverse=True)

    return lista_top_nombres


def calcular_nombres_ambos_generos(lista_fichero: list[FrecuenciaNombre])->set[str]:
    conjunto_nombres = set()

    for registro in lista_fichero:
        conjunto_nombres.add(registro.nombre)

    return conjunto_nombres


def calcular_nombres_compuestos(lista_fichero: list[FrecuenciaNombre], genero:str)->set[str]:
    conjunto_nombres = set()

    for registro in lista_fichero:
        if genero == registro.genero and " " in registro.nombre:
            conjunto_nombres.add(registro.nombre)
        if genero == None:
            for registro in lista_fichero:
                conjunto_nombres.add(registro.nombre)
            return conjunto_nombres

    return conjunto_nombres


def calcular_frecuencia_media_nombre_años(lista_fichero: list[FrecuenciaNombre], nombre:str, año_inicial:int, año_final:int)->float:
    suma_frecuencias = 0
    contador = 0

    for registro in lista_fichero:
        if registro.nombre == nombre and año_inicial <= registro.año < año_final:
            suma_frecuencias += registro.frecuencia
            contador += 1

    if contador == 0:
        return 0

    return suma_frecuencias / contador


def calcular_nombre_mas_frecuente_año_genero(lista_fichero: list[FrecuenciaNombre], año:int, genero:str)->str:
    nombre_mas_frecuente = ""
    frecuencia_mas_alta = 0

    for registro in lista_fichero:
        if registro.año == año and registro.genero == genero and registro.frecuencia > frecuencia_mas_alta:
            nombre_mas_frecuente = registro.nombre
            frecuencia_mas_alta = registro.frecuencia

    return nombre_mas_frecuente


def calcular_año_mas_frecuencia_nombre(lista_fichero: list[FrecuenciaNombre], nombre:str)->int:
    año_mas_frecuencia=0
    mayor_frecuencia=0

    for registro in lista_fichero:
        if registro.nombre == nombre:
            if registro.frecuencia > mayor_frecuencia:
                mayor_frecuencia = registro.frecuencia
                año_mas_frecuencia = registro.año

    return año_mas_frecuencia

def calcular_nombres_mas_frecuentes(lista_fichero:list[FrecuenciaNombre], genero:str, decada:int, n:int)->list[str]:
    lista_nombres=[]
    numero_nombres=0
    for registro in lista_fichero:
        if registro.genero == genero and decada <= registro.año <= decada+10:
            lista_nombres.append(registro.nombre)
    
    lista_nombres.sort(key=registro.frecuencia)
    
    for n in range(n+1):
        numero_nombres+=1

    return lista_nombres, numero_nombres


def calcular_año_frecuencia_por_nombre(lista_fichero:list[FrecuenciaNombre], genero:str)->dict[str,tuple[int,int]]:
    diccionario=dict()
    for r in lista_fichero:
        clave=r.nombre
        tupla=(r.año, r.frecuencia)
        if r.genero == genero:
            if clave in diccionario:
                diccionario[clave].append(tupla)
            else:
                diccionario[clave]=[tupla]
    return diccionario


def calcular_nombre_mas_frecuente_por_año(lista_fichero:list[FrecuenciaNombre], genero:str)->list[tuple[int,str,int]]:
    diccionario=dict()
    lista_nombres=[]
    for r in lista_fichero:
        clave=r.año
        tupla=(r.nombre, r.frecuencia)
        if r.genero == genero:
            if clave in diccionario:
                diccionario[clave].append(tupla)
            else:
                diccionario[clave]=[tupla]
    sorted(diccionario.items(), key=lambda x: x[0], reverse=True)

    for año, valores in diccionario.items():
        valores=(año, max(valores, key=lambda x: x[1]))
        lista_nombres.append(valores)
    
    return lista_nombres


def calcular_frecuencia_por_año(lista_fichero:list[FrecuenciaNombre], nombre:str)->list[tuple[int,int]]:
    frecuencia_por_año = {}

    for registro in lista_fichero:
        if registro.nombre == nombre:
            if registro.año in frecuencia_por_año:
                frecuencia_por_año[registro.año] += registro.frecuencia
            else:
                frecuencia_por_año[registro.año] = registro.frecuencia

    lista_frecuencia_por_año = sorted(frecuencia_por_año.items())

    return lista_frecuencia_por_año


def mostrar_evolucion_por_año(lista_fichero:list[FrecuenciaNombre], nombre:str)->plt:
    frecuencias_por_año = calcular_frecuencia_por_año(lista_fichero, nombre)
    años = [año for año, _ in frecuencias_por_año]
    frecuencias = [frecuencia for _, frecuencia in frecuencias_por_año]

    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()


def calcular_frecuencias_por_nombre(lista_fichero:list[FrecuenciaNombre])->dict[str,int]:
    diccionario=dict()
    for r in lista_fichero:
        clave=r.nombre
        if clave in diccionario:
            diccionario[clave]+=r.frecuencia
        else:
            diccionario[clave]=r.frecuencia

    return diccionario


def mostrar_frecuencias_nombres(lista_fichero:list[FrecuenciaNombre], limite:int)->plt:
    frecuencias_por_nombre = calcular_frecuencias_por_nombre(lista_fichero)
    nombres_limitados = sorted(frecuencias_por_nombre.items(), key=lambda x:x[1], reverse=True)[:limite]
    nombres = [nombres for nombres,_ in nombres_limitados]
    frecuencias = [frecuencias for _,frecuencias in nombres_limitados]

    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(limite))
    plt.show()  