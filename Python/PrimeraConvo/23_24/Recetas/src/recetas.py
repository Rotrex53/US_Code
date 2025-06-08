from typing import NamedTuple, Optional, List, Set, Tuple, Dict
from datetime import date, datetime
import csv
from collections import defaultdict

Receta = NamedTuple("Receta",  
                    [("nombre", str), 
                     ("tipo", str), 
                     ("dificultad", str), 
                     ("ingredientes", Optional[List[str]]), 
                     ("tiempo_preparacion", int), 
                     ("calorias", int), 
                     ("fecha_creacion", date), 
                     ("precio_estimado", float) 
                    ])


def leer_recetas(fichero:str) -> List[Receta]:
    recetas = list()
    with open(fichero, encoding="UTF-8") as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, tipo, dificultad, ingredientes, tiempo_preparacion, calorias, fecha_creacion, precio_estimado in lector:
            ingredientes = parseaIngredientes(ingredientes)
            tiempo_preparacion = int(tiempo_preparacion)
            calorias = int(calorias)
            fecha_creacion = datetime.strptime(fecha_creacion, '%Y-%m-%d').date()
            precio_estimado = float(precio_estimado)
            r = Receta(nombre, tipo, dificultad, ingredientes, tiempo_preparacion, calorias, fecha_creacion, precio_estimado)
            recetas.append(r)
    return recetas

def parseaIngredientes(ingredientes_str: Optional[str]) -> List[str] | None:
    res=None
    if ingredientes_str:
        res = [ingrediente.strip() for ingrediente in ingredientes_str.split(",")]

    return res


def receta_mas_barata(recetas: List[Receta], 
                        tipos: Set[str],  
                        n: Optional[int] = None) -> Receta:
    res = list()
    for receta in recetas:
        if receta.tipo in tipos:
            if n!=None:
                res.append(receta)
                sorted(res, key=lambda x:x.calorias)[:n]
            else:
                res.append(receta)
                sorted(res, key=lambda x:x.calorias)

    return min(res, key=lambda x:x.precio_estimado)


def obten_ingredientes(recetas: List[Receta],  
                          mes1: Optional[int] = None, 
                          mes2: Optional[int] = None) -> Set[str]:
    res=set()
    for receta in recetas:
        if receta.ingredientes!=None:
            if(mes1==None or receta.fecha_creacion.month>=mes1) and (mes2==None or receta.fecha_creacion.month<mes2):
                res=res.union(receta.ingredientes)
    return res


def recetas_con_precio_menor_promedio(recetas: List[Receta], n: int) -> List[Tuple[str, int]]:
    precio_promedio = sum(receta.precio_estimado for receta in recetas)/len(recetas)

    lista = []
    for receta in recetas:
        if receta.precio_estimado<precio_promedio:
            lista.append((receta.nombre, receta.calorias))
    return sorted(lista, key=lambda x:x[1])[:n]


def receta_mas_ingredientes(recetas: List[Receta],  
                           ingredientes: Optional[Set[str]] = None) -> Tuple[str, List[str]]:
    tupla = ()
    comp = []
    for receta in recetas:
        if receta.ingredientes!=None and len(receta.ingredientes)>len(comp):
            if ingredientes==None:
                tupla=(receta.nombre, receta.ingredientes)
        
            if ingredientes!=None and any(ingredientes in receta.ingredientes):
                tupla=(receta.nombre, receta.ingredientes)

            comp = receta.ingredientes

    return tupla

def ingredientes_mas_comunes_por_tipo(recetas: List[Receta]) -> Dict[str, List[str]]:
    dicc=defaultdict(list)
    contador=defaultdict(int)
    res={}
    for receta in recetas:
        if receta.ingredientes!=None:
            dicc[receta.tipo]+=receta.ingredientes
    
    for tipo, ingredientes in dicc.items():
        for ingrediente in ingredientes:
            contador[ingrediente]+=1
 
        top3 = sorted(contador.items(), key=lambda x:x[1], reverse=True)[:3]
        res[tipo] = [nombre for nombre,_ in top3]
    return res

def mes_con_precio_medio_mas_alto(recetas: List[Receta], n: int) -> int:
    listAux = []
    dicc = defaultdict(list)
    for receta in recetas:
        dicc[receta.fecha_creacion.month].append(receta.precio_estimado)
    
    for mes, lista_precios in dicc.items():
        if len(lista_precios)>=n:
            suma=0
            for precio in lista_precios:
                suma+=precio
            precio_promedio = suma/len(lista_precios)
            listAux.append((mes, precio_promedio))
    
    return max(listAux, key=lambda x:x[1])[0]
