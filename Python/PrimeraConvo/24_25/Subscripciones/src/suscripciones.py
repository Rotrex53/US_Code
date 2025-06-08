from typing import NamedTuple, Counter
from datetime import date, datetime
from collections import defaultdict
import csv
 
Suscripcion = NamedTuple("Suscripcion", 
                         [("nombre", str), 
                          ("dni", str), 
                          ("fecha_inicio", date), 
                          ("fecha_fin", date | None), # Será None si la suscripción sigue activa 
                          ("tipo_plan", str), 
                          ("num_perfiles", int), 
                          ("precio_mensual", float), 
                          ("addons", list[str]) 
                         ])


def lee_suscripciones(ruta_fichero: str) -> list[Suscripcion]:
    with open(ruta_fichero, encoding="UTF-8") as f:
        lista = []
        lector = csv.reader(f)
        next(lector)
        for nombre, dni, fecha_inicio, fecha_fin, tipo_plan, num_perfiles, precio_mensual, addons in lector:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            fecha_fin = parsea_fecha(fecha_fin)
            num_perfiles = int(num_perfiles)
            precio_mensual = float(precio_mensual)
            addons = parsea_addons(addons)
            lista.append(Suscripcion(nombre, dni, fecha_inicio, fecha_fin, tipo_plan, num_perfiles, precio_mensual, addons))
    return lista

def parsea_fecha(fecha_str: str) -> date | None:
    if fecha_str=="":
        return None
    else:
        return datetime.strptime(fecha_str, "%Y-%m-%d").date()

def parsea_addons(lista_addons_str: str)->list[str]:
    lista = []
    addons = lista_addons_str.split(",")
    for addon in addons:
        lista.append(addon)
    return lista


def suscripciones_mas_rentables(suscripciones: list[Suscripcion], 
                    n: int = 3, 
                    tipos_plan: set[str]|None = None) -> list[tuple[str, float]]:
    listaRes=[]
    for suscripcion in suscripciones:
        if tipos_plan==None or suscripcion.tipo_plan in tipos_plan:
            listaRes.append((suscripcion.dni, importe_total(suscripcion)))
    listaOrdenada = sorted(listaRes, key=lambda x:x[1], reverse=True)
    return listaOrdenada[:n]
    
def total_dias(suscripcion: Suscripcion) -> int:
    fecha_fin = suscripcion.fecha_fin
    fecha_inicio = suscripcion.fecha_inicio
    if fecha_fin!=None:
        return (fecha_fin - fecha_inicio).days
    else:
        return (date.today() - fecha_inicio).days
    
def importe_total(suscripcion: Suscripcion) -> float:
    precio_diario = suscripcion.precio_mensual/30.0
    return precio_diario*total_dias(suscripcion)


def plan_mas_perfiles(suscripciones: list[Suscripcion],  
                        fecha_ini: date|None = None,  
                        fecha_fin: date|None = None) -> tuple[str, int]:
    diccAux = defaultdict(int)
    for suscripcion in suscripciones:
        if (fecha_ini is None or suscripcion.fecha_inicio >= fecha_ini) \
            and (fecha_fin is None or suscripcion.fecha_inicio <= fecha_fin):
            diccAux[suscripcion.tipo_plan] += suscripcion.num_perfiles

    return max(diccAux.items(), key=lambda x:x[1])

def media_dias_por_plan(suscripciones: list[Suscripcion]) -> dict[str, float]:
    diccAux = defaultdict(list[Suscripcion])
    diccRes = defaultdict(float)
    for suscripcion in suscripciones:
        if suscripcion.fecha_fin!=None:
            diccAux[suscripcion.tipo_plan].append(suscripcion)
    
    for tipo, lista_suscripciones_filtradas in diccAux.items():
        duracion_media = sum(total_dias(sus) for sus in lista_suscripciones_filtradas)/len(lista_suscripciones_filtradas)
        diccRes[tipo]=duracion_media
    
    return diccRes

def addon_mas_popular_por_año(suscripciones: list[Suscripcion]) -> dict[int,str]:
    addons_por_año = defaultdict(Counter)
    diccRes = defaultdict(str)
    for sus in suscripciones:
        addons_por_año[sus.fecha_inicio.year].update(sus.addons)

    for año, lista_addons in addons_por_año.items():
            addon_mas_aparecido = lista_addons.most_common(1)[0][0]
            diccRes[año]=addon_mas_aparecido

    return diccRes


def evolucion_años(suscripciones: list[Suscripcion]) -> list[tuple[int, int]]:
# Contamos num suscripciones por año
    sus_por_año = num_suscripciones_por_año(suscripciones)
# Calculamos incremento o decremento por año
    años = sorted(sus_por_año.keys())
    evolucion = []
    for año1, año2 in zip(años, años[1:]):
        evolucion.append((año2, sus_por_año[año2] - sus_por_año[año1]))
    return evolucion

def num_suscripciones_por_año(suscripciones: list[Suscripcion]) -> dict[int, int]:
    res = defaultdict(int)  
    for s in suscripciones:
        ano_ini = s.fecha_inicio.year
        if s.fecha_fin != None:
            ano_fin = s.fecha_fin.year
            res[ano_fin] -= 1
        res[ano_ini] += 1
    return res