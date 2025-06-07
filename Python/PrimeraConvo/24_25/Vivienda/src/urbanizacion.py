from typing import NamedTuple 
from datetime import datetime,date 
import csv
from collections import defaultdict
 
Mejora = NamedTuple("Mejora",      
       [("denominacion", str),  
        ("coste", int),  
        ("fecha", date)]) 
 
Vivienda = NamedTuple("Vivienda",      
      [("propietario", str), 
       ("calle", str), 
       ("numero", int), 
       ("fecha_adquisicion", date), 
       ("metros",float), 
       ("precio",int),         
       ("mejoras", list[Mejora])])



def lee_viviendas(ruta: str) -> list[Vivienda]:
    with open(ruta, encoding="UTF-8") as f:
        lista = []
        lector=csv.reader(f, delimiter=";")
        next(lector)
        for propietario, calle, numero, fecha_adquisicion, metros, precio, mejoras in lector:
            numero=int(numero)
            fecha_adquisicion=datetime.strptime(fecha_adquisicion,"%d/%m/%Y").date()
            metros=float(metros)
            precio=int(precio)
            mejoras=parsea_mejoras(mejoras)
            r = Vivienda(propietario, calle, numero, fecha_adquisicion, metros, precio, mejoras)
            lista.append(r)
    return lista

def parsea_mejoras(mejoras_str:str) -> list[Mejora]:
    listaRes=[]
    if mejoras_str=="":
        return listaRes
    mejoras=mejoras_str.split("*")
    for mejora in mejoras:
        datos_mejora=mejora.split("-")
        denominacion=datos_mejora[0]
        coste=int(datos_mejora[1])
        fecha=datetime.strptime(datos_mejora[2], "%d/%m/%Y").date()
        listaRes.append(Mejora(denominacion, coste, fecha))
    return listaRes


def total_mejoras_por_calle(viviendas: list[Vivienda], par_impar: str) -> dict[str,int]:
    dicc=defaultdict(int)
    if par_impar.lower()=="par":
        filtradas=(vivienda for vivienda in viviendas if vivienda.numero%2==0)
    if par_impar.lower()=="impar":
        filtradas=(vivienda for vivienda in viviendas if vivienda.numero%2!=0)
    for vivienda in filtradas:
        dicc[vivienda.calle]+=len(vivienda.mejoras)
    return dicc


def vivienda_con_mejora_mas_rapida(viviendas: list[Vivienda]) -> tuple[str,str,int,int,str]:
    duracionAnterior = None
    tuplaRes =()
    for vivienda in viviendas:
        fecha_inicio = vivienda.fecha_adquisicion
        for mejora in vivienda.mejoras:
            fecha_fin = mejora.fecha
            duracionMejora = (fecha_fin - fecha_inicio).days
            if  duracionAnterior==None or duracionMejora<duracionAnterior:
                tuplaRes = (vivienda.propietario, vivienda.calle, vivienda.numero, duracionMejora, mejora.denominacion)
                duracionAnterior = duracionMejora
    return tuplaRes


def calle_mayor_diferencia_precios(viviendas: list[Vivienda]) -> str:
    calle = None
    difAnterior = None
    diccCalleTupla = defaultdict(list)

    for vivienda in viviendas:
        tupla = (vivienda.numero, vivienda.precio)
        diccCalleTupla[vivienda.calle].append(tupla)

    for calle_clave, lista_tuplas_valor in diccCalleTupla.items():
        pares_suma_precios=0
        impares_suma_precios=0
        for numero_vivienda, precio_vivienda in lista_tuplas_valor:
            if numero_vivienda%2==0:
                pares_suma_precios+=precio_vivienda
            if numero_vivienda%2!=0:
                impares_suma_precios+=precio_vivienda
        difActual=abs(pares_suma_precios-impares_suma_precios)
        if difAnterior==None or difActual>difAnterior:
            calle = calle_clave
            difAnterior=difActual

    return calle


def n_viviendas_top_valoradas_por_calle(viviendas: list[Vivienda],  
                fecha: date|None = None,  n: int = 3) -> dict[str,list[tuple[str,int,int]]]:
    diccRes = {}
    if fecha is not None:
        viviendas_filtradas = (vivienda for vivienda in viviendas if vivienda.fecha_adquisicion>=fecha)
    else:
        viviendas_filtradas = viviendas

    for vivienda in viviendas_filtradas:
        if vivienda.calle not in diccRes:
            diccRes[vivienda.calle]=[]
        tupla_valor = (nombre_propietario(vivienda.propietario), vivienda.numero, valor_vivienda(vivienda))
        diccRes[vivienda.calle].append(tupla_valor)

    for calle_clave, listaTuplas_valor in diccRes.items():
        lista_ordenada = sorted(listaTuplas_valor, key=lambda x:x[2], reverse=True)
        diccRes[calle_clave] = lista_ordenada[:n]

    return diccRes
#func aux
def nombre_propietario(nombre_completo: str) -> str:
    nombreYApellidos = nombre_completo.split(",")
    return nombreYApellidos[1].strip()
#func aux
def valor_vivienda(vivienda: Vivienda) -> int:
    precio_base = vivienda.precio
    precio_mejoras = 0
    for mejora in vivienda.mejoras:
        precio_mejoras+=mejora.coste
    return precio_base + precio_mejoras


def valor_metro_cuadrado_por_calle_y_año(viviendas: list[Vivienda]) -> list[tuple[int, list[tuple[str, float]]]]:
    resultado = []
    viviendas_por_año = defaultdict(list)

    for vivienda in viviendas:
        año = vivienda.fecha_adquisicion.year
        viviendas_por_año[año].append(vivienda)

    for año in sorted(viviendas_por_año.keys()):
        viviendas_ese_año = viviendas_por_año[año]
        viviendas_por_calle = defaultdict(list)

        for vivienda in viviendas_ese_año:
            viviendas_por_calle[vivienda.calle].append((vivienda.metros, vivienda.precio))

        lista_tuplas = []
        for calle, lista_metros_precios in viviendas_por_calle.items():
            precio_medio = precio_medio_metro_cuadrado(lista_metros_precios)
            lista_tuplas.append((calle, precio_medio))

        lista_tuplas.sort(key=lambda x: x[1], reverse=True)
        resultado.append((año, lista_tuplas))

    return resultado
# func aux
def precio_medio_metro_cuadrado(lista_valores: list[tuple[float, int]]) -> float:
    precio_acum = 0
    for metros, precio in lista_valores:
        precio_acum += precio/metros
    return precio_acum/len(lista_valores)

    