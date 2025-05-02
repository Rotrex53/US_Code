from typing import NamedTuple 
from datetime import date 
import csv
import datetime
from collections import Counter

Medallas = NamedTuple('Medallas', [('oro', int), ( 'plata', int),  ('bronce', int)]) 
Registro = NamedTuple('Registro', [ ('ciudad_olimpica', str),  ('fecha_inicio', date),  ('pais', str),  
                                    ('deporte', str), ('num_participantes', int),  ('genero', str),  
                                    ('medallas', Medallas),   ('sede', bool)])


def leer_registro(archivo: str) -> list[Registro]:
    with open(archivo, encoding="utf-8") as f:
        lista_registros = []
        lector = csv.reader(f)
        next(lector)
        
        for ciudad_olimpica, fecha_inicio, pais, deporte, num_participantes, genero, oro, plata, bronce, sede in lector:
            fecha_inicio = parsea_fecha(fecha_inicio)
            num_participantes = int(num_participantes.strip())
            medallas = parsea_medallas(f"{oro}-{plata}-{bronce}")
            sede = parsea_sede(sede)
            
            r = Registro(ciudad_olimpica.strip(), fecha_inicio, pais.strip(), deporte.strip(), 
                         num_participantes, genero, medallas, sede)
            lista_registros.append(r)
            #el .strip() es para eliminar los espacios en blanco al inicio y al final de la cadena
    return lista_registros

def parsea_medallas(medallas: str) -> Medallas:
    cadenas = medallas.split("-")
    oro, plata, bronce = int(cadenas[0]), int(cadenas[1]), int(cadenas[2])
    
    return Medallas(oro, plata, bronce)

def parsea_fecha(fecha: str) -> date:
    return datetime.datetime.strptime(fecha, "%Y-%m-%d").date()

def parsea_sede(sede: str) -> bool:
    if sede == "SI":
        return True
    elif sede == "NO":
        return False
    


def deportes_ambos_generos_en_anio(registros: list[Registro], anio: int) -> set[str]:
    deportes = set()
    deportes_hombres = set()
    deportes_mujeres = set()
    
    for r in registros:
        if r.fecha_inicio.year == anio:
            if r.genero == "HOMBRE":
                deportes_hombres.add(r.deporte)
            elif r.genero == "MUJER":
                deportes_mujeres.add(r.deporte) 
    deportes = deportes_hombres.intersection(deportes_mujeres)          #Intersección de conjuntos

    return deportes


def deportes_mas_frecuentes(registros: list[Registro], n: int, genero: str) -> list[tuple[str, int]]:
    deportes_contador = Counter()
    
    for r in registros:
        if r.genero == genero:
            deportes_contador[r.deporte] += 1
    deportes_mas_comunes = deportes_contador.most_common(n)
    
    return deportes_mas_comunes

def deportes_mas_frecuentes2(registros: list[Registro], n: int, genero: str) -> list[tuple[str, int]]:
    deportes_contador = {}

    for r in registros:
        if r.genero == genero:
            if r.deporte in deportes_contador:
                deportes_contador[r.deporte] += 1
            else:
                deportes_contador[r.deporte] = 1

    deportes_ordenados = sorted(deportes_contador.items(), key=lambda x: x[1], reverse=True)[:n]
    #Sera MUY penalizado si hacemos un sorted() para despues hacer un max(), directamente se hace max()
    return deportes_ordenados


def deporte_con_mas_paises_distintos_con_oro(registros: list[Registro], genero: str = None) -> str:
    paises_por_deporte = {}

    for r in registros:
        if genero is None or r.genero == genero:    #"genero == None" o "genero is None" ambas formas son elegantes para el profesor
            if r.medallas.oro > 0:
                if r.deporte in paises_por_deporte:
                    paises_por_deporte[r.deporte].add(r.pais)
                else:
                    paises_por_deporte[r.deporte] = set()

    deporte_max_paises = max(paises_por_deporte.items(), key=lambda deporte: len(paises_por_deporte[deporte]))
    
    return deporte_max_paises


def deportes_mas_participantes_de_genero_por_juego(registros: list[Registro], pais: str, genero: str) -> dict[str, list[tuple[str, int]]]:
    juegos = {}

    for r in registros:
        if r.pais == pais and r.genero == genero:
            identificador_juego = f"{r.ciudad_olimpica}{str(r.fecha_inicio.year)[-2:]}"
            if identificador_juego not in juegos:
                juegos[identificador_juego] = []
            juegos[identificador_juego].append((r.deporte, r.num_participantes))

    for juego in juegos:
        juegos[juego] = sorted(juegos[juego], key=lambda x: x[1], reverse=True)[:3]

    return juegos

def deportes_por_juegos(registros: list[Registro], pais: str, genero: str) -> dict[str, list[tuple[str, int]]]:
    juegos = {}

    for r in registros:
        if r.pais == pais and r.genero == genero:
            identificador_juego = f"{r.ciudad_olimpica}{str(r.fecha_inicio.year)[-2:]}"

            if identificador_juego not in juegos:
                juegos[identificador_juego] = []

            juegos[identificador_juego].append((r.deporte, r.num_participantes))

    return juegos

def deportes_mas_participantes_de_genero_por_juego2(registros: list[Registro], pais: str, genero: str) -> dict[str, list[tuple[str, int]]]:
    dict_aux = deportes_por_juegos(registros, pais, genero)
    dicc_final = {}

    for juego in dict_aux:
        dicc_final[juego] = sorted(dict_aux[juego], key=lambda x: x[1], reverse=True)[:3]

    return dicc_final


def deporte_con_todos_los_paises(registros: list[Registro]) -> bool:
    paises = set(r.pais for r in registros)
    deportes_por_pais = {}

    for r in registros:
        if r.deporte not in deportes_por_pais:
            deportes_por_pais[r.deporte] = set()
        deportes_por_pais[r.deporte].add(r.pais)

    for deporte, paises_participantes in deportes_por_pais.items():
        if paises_participantes == paises:
            return True

    return False


def anyo_con_mayor_incremento_participantes_de_pais(registros: list[Registro], pais: str) -> tuple[int, int]:
    participantes_por_anio = {}

    for r in registros:
        if r.pais == pais:
            anio = r.fecha_inicio.year
            if anio not in participantes_por_anio:
                participantes_por_anio[anio] = 0
            participantes_por_anio[anio] += r.num_participantes

    anios_ordenados = sorted(participantes_por_anio.keys())
    max_incremento = 0
    anio_max_incremento = None

    for i in range(1, len(anios_ordenados)):
        incremento = participantes_por_anio[anios_ordenados[i]] - participantes_por_anio[anios_ordenados[i - 1]]
        if incremento > max_incremento:
            max_incremento = incremento
            anio_max_incremento = anios_ordenados[i]

    return (max_incremento, anio_max_incremento)