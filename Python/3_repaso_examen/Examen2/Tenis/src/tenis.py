from typing import NamedTuple
from collections import Counter
import datetime
import csv

'''1.  lee_partidos_tenis: lee un fichero de entrada en formato CSV codificado en UTF-8 y devuelve una lista de 
tuplas de tipo PartidoTenis conteniendo todos los datos almacenados en el fichero. Le puede ser de ayuda 
la función datetime.strptime(cadena, '%d/%m/%Y')  para el parseo de fechas. Para implementar esta 
función defina la siguiente función auxiliar: 
    a. parsea_set: Toma una cadena con el resultado de un set y devuelve una tupla de tipo Set que 
    representa ese  set. La cadena de entrada se espera que  tenga los juegos del set del primer 
    jugador, seguido de un guión y los juegos del set del segundo jugador, es decir, int-int. '''

ruta='C:/Users/rodri/OneDrive/Desktop/US_proyects/Python/3_repaso_examen/Examen2/Tenis/data/tenis.csv'
Parcial = NamedTuple('Parcial', (('juegos_j1',int), ('juegos_j2',int)))
PartidoTenis = NamedTuple('PartidoTenis', (('fecha', datetime.date),('jugador1', str),('jugador2',str),('superficie',str),('resultado', list[Parcial]), ('errores_nf1', int),('errores_nf2',int)))


def parsea_set(str_set:str)->Parcial:
    juegos=str_set.split("-")
    juegos_j1=int(juegos[0])
    juegos_j2=int(juegos[1])
    return Parcial(juegos_j1, juegos_j2)


def leer_archivo(archivo:str)->list[PartidoTenis]:
    registro=[]
    with open(archivo, encoding="utf-8") as a:
        lector=csv.reader(a, delimiter=";")
        
        for fecha, jugador1, jugador2, superficie, parcial1, parcial2, parcial3, errores_nf1, errores_nf2 in lector:
            fecha=datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            resultado=[parsea_set(parcial1), parsea_set(parcial2), parsea_set(parcial3)]
            errores_nf1=int(errores_nf1)
            errores_nf2=int(errores_nf2)

            tupla=PartidoTenis(fecha, jugador1, jugador2, superficie, resultado, errores_nf1, errores_nf2)
            registro.append(tupla)
    return registro


''' tenista_mas_victorias: recibe una lista de tuplas de tipo PartidoTenis, y dos fechas, ambas de tipo date, y 
con valor por defecto None.  Devuelve el nombre  del tenista que ha tenido más victorias en los partidos 
jugados entre las fechas (ambas inclusive). Si la primera fecha es None, la función  devuelve el tenista con 
más victorias hasta esa fecha (inclusive). Si la segunda fecha es  None,  la función devuelve el tenista con 
más victorias  desde  esa  fecha  (inclusive).  Finalmente,  si  las  dos  fechas  son  None,  la  función  devuelve  el 
tenista con más victorias de toda la lista, independientemente de la fecha. Para implementar esta función 
defina la siguiente función auxiliar: 
    a. ganador:  recibe  una  tupla de  tipo PartidoTenis y  devuelve  el  nombre  del  jugador  que  ganó 
    ese partido.'''
def ganador(archivo:PartidoTenis)->str:
    jugador_ganador=None
    resultado=archivo.resultado
    if resultado[0].juegos_j1 > resultado[0].juegos_j2 and resultado[1].juegos_j1 > resultado[1].juegos_j2:
        jugador_ganador=archivo.jugador1
    elif resultado[0].juegos_j1 < resultado[0].juegos_j2 and resultado[1].juegos_j1 < resultado[1].juegos_j2:
        jugador_ganador=archivo.jugador2
    elif resultado[2].juegos_j1 > resultado[2].juegos_j2:
        jugador_ganador=archivo.jugador1
    elif resultado[2].juegos_j1 > resultado[2].juegos_j2:
        jugador_ganador=archivo.jugador2

    return jugador_ganador
        

'''def tenista_mas_victorias(archivo:list[PartidoTenis], fecha1:datetime.date=None, fecha2:datetime.date=None)->str:
    lista_fechas=[]
    dicc_cont1=dict()
    dicc_cont2=dict()

    for r in archivo:
        if fecha1 != None and fecha2 != None:
            if fecha1 <= r.fecha <= fecha2:
                lista_fechas.append(r.fecha)
        elif fecha1 == None:
            if r.fecha <= fecha1:
                lista_fechas.append(r.fecha)
        elif fecha2 == None:
            if r.fecha >= fecha2:
                lista_fechas.append(r.fecha)
        elif fecha1 == None and fecha2 == None:
            lista_fechas.append(r.fecha)

    for r in lista_fechas:
        if r.jugador1==ganador(r)'''
def fecha_en_rango2(fecha, fecha1=None, fecha2=None):
    if fecha1==None:
        fecha1=datetime.min
    if fecha2==None:
        fecha2=datetime.max
    return fecha1 <= fecha <=fecha2


def tenista_mas_victorias0(lista_partidos:list[PartidoTenis],fecha1:datetime.date=None,fecha2:datetime.date=None)->tuple[str,int]:
    lista_fechas=[p for p in lista_partidos if fecha_en_rango2(p.fecha, fecha1,fecha2)]
    dicc_cont1=Counter(p.jugador1 for p in lista_fechas if p.jugador1==ganador(p))
    dicc_cont2=Counter(p.jugador2 for p in lista_fechas if p.jugador2==ganador(p))
    dicc_cont=dicc_cont1+dicc_cont2
    return dicc_cont.most_common(1)[0]