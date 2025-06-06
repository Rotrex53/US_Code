from typing import NamedTuple 
from datetime import datetime
from collections import defaultdict
import csv
 
Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)]) 
 
CarreraFP=NamedTuple("CarreraFP",[ 
        ("fecha_hora",datetime),  
        ("circuito",str),                     
        ("pais",str),  
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado 
        ("tiempo",float),  
        ("podio", list[Piloto])])

def lee_carreras(filename: str) -> list[CarreraFP]:
    lista = []
    with open(filename, encoding="UTF-8") as f:
        lector = csv.reader(f)
        next(lector)
        for fecha_hora, circuito, pais, seco, tiempo, primero_nombre, primero_escuderia, segundo_nombre, segundo_escuderia, tercer_nombre, tercer_escuderia in lector:
            fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
            seco = parseaSeco(seco)
            podio = [Piloto(primero_nombre, primero_escuderia),
                    Piloto(segundo_nombre, segundo_escuderia),
                    Piloto(tercer_nombre, tercer_escuderia)]
            tiempo = float(tiempo)
            r = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio)
            lista.append(r)
    return lista

def parseaSeco(seco: str) -> bool:
    if seco=="Seco":
        return True
    if seco=="Mojado":
        return False
   

def maximo_dias_sin_ganar(carreras: list[CarreraFP], nombre_piloto: str) -> int:
    listaTiempos = []
    carreras_ganadas = 0
    fecha_inicio = None
    for carrera in carreras:
        if nombre_piloto == carrera.podio[0].nombre:
            carreras_ganadas+=1
            if fecha_inicio!=None:
                tiempo = (carrera.fecha_hora - fecha_inicio).days
                listaTiempos.append(tiempo)
            fecha_inicio = carrera.fecha_hora
    if carreras_ganadas>=2:
        return max(listaTiempos)
    else:
        return None
    
def piloto_mas_podios_por_circuito(carreras: list[CarreraFP]) -> dict[str,str]:
    lista = []
    diccAux=defaultdict(list)
    dicc=defaultdict(str)
    for carrera in carreras:
        diccAux[carrera.circuito].append(carrera.podio)
    
    for circuito, lista_podios in diccAux.items():
        diccAux2=defaultdict(int)
        for podio in lista_podios:
            for piloto in podio:
                if piloto.nombre in lista:
                    diccAux2[piloto.nombre]+=1
                else:
                    lista.append(piloto.nombre)
        dicc[circuito]=max(diccAux2, key=diccAux2.get)

    return dicc

def escuderias_con_solo_un_piloto(carreras: list[CarreraFP]) -> list[str]:
    listaRes = []
    diccAux = {}
    for carrera in carreras:
        for piloto in carrera.podio:
            if piloto.escuderia not in diccAux:
                diccAux[piloto.escuderia]=[]
            diccAux[piloto.escuderia].append(piloto.nombre)
    
    for escuderia, lista_pilotos in diccAux.items():
        if len(set(lista_pilotos))==1:
            listaRes.append(escuderia)
    
    return listaRes

def piloto_racha_mas_larga_victorias_consecutivas(carreras: list[CarreraFP], año: int|None = None) -> tuple[str, int]:
    tuplaRes = ()
    diccAux = defaultdict(list)
    ganadorAnterior=None
    rachaActual = 0
    for carrera in carreras:
        if carrera.fecha_hora.year==año or año==None:
            ganador = carrera.podio[0].nombre
            if ganadorAnterior==None:
                rachaActual = 1
                ganadorAnterior = ganador
            elif ganadorAnterior != None:
                if ganadorAnterior == ganador:
                    rachaActual+=1
                else:
                    diccAux[ganadorAnterior].append(rachaActual)
                    rachaActual = 1
                    ganadorAnterior = ganador
    for persona, lista_rachas in diccAux.items():
        diccAux[persona]=max(lista_rachas)

    tuplaRes = max(diccAux.items(), key=lambda x:x[1])
    return tuplaRes

def ultimos_ganadores_por_circuito(carreras:list[CarreraFP], n: int, estado: str) -> dict[str, list[str]]:
    diccRes = defaultdict(str)
    diccAux = defaultdict(list)
    if estado == "Seco":
        estado_bool = True
    if estado == "Mojado":
        estado_bool = False

    for carrera in carreras:
        if carrera.seco == estado_bool:
            diccAux[carrera.circuito].append((carrera.podio[0].nombre, carrera.fecha_hora.date()))

    for circuito, tupla in diccAux.items():
        tupla_ordenada = sorted(tupla, key=lambda x:x[1], reverse=True)
        diccRes[circuito]=[nombre for nombre,_ in tupla_ordenada[:n]]

    return diccRes