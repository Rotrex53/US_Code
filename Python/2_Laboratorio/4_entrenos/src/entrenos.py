from typing import NamedTuple
import datetime
from datetime import datetime
import csv


Entreno = NamedTuple("Entreno" ,[("tipo", str),("fechahora", datetime),("ubicacion", str),("duracion", int),
            ("calorias", int),("distancia", float),("frecuencia", int),("compartido", bool)])

def leer_entreno(entrenos_csv:str)->list[Entreno]:

    lista_entrenos=[]

    with open(entrenos_csv, encoding="utf-8") as f:
    
        lector=csv.reader(f)
        next(lector) #solo si el fichero tiene una primera línea distinta

        for tipo,fechahora_cadena,ubicacion,duracion,calorias,distancia,frecuencia,compartido in lector:
        #for tupla in lector        (esto seria si queremos los datos empaquetados)

            #convertir las cadenas de caracteres en datos con su tipo
            fechahora=datetime.strptime(fechahora_cadena,"%d/%m/%Y %H:%M")    

            #si la lectura se hubiera hecho sin desempaquetar aquí pondriamos:
            #fecha=datetime.strptime(tupla[0],"%Y-%m-%d").date()
            tipo=str(tipo)
            ubicacion=str(ubicacion)
            duracion=int(duracion)
            calorias=int(calorias)
            distancia=float(distancia)
            frecuencia=int(frecuencia)
            if compartido=="S":
                compartido=True
            elif compartido=="N":
                compartido=False

            r=Entreno(tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido)

            lista_entrenos.append(r)

    return lista_entrenos


def tipos_entreno(tupla_tipos_entrenos:list[Entreno])->list[Entreno]:

    conjunto=set()

    for r in tupla_tipos_entrenos:
        conjunto.add(r.tipo)
    lista_tipos_entrenos_conjunto=list(conjunto)

    return lista_tipos_entrenos_conjunto


def entrenos_duracion_superior(lista_duraciones_entrenos:list[Entreno], d:int)->list:
    conjunto=set()

    for registro in lista_duraciones_entrenos:
        if registro.duracion > d:
            conjunto.add(registro.tipo)

    lista_duraciones_superior_conjunto=list(conjunto)

    return lista_duraciones_superior_conjunto


def suma_calorias(lista_calorias:list[Entreno], f_inicio:int, f_fin:int)->int:
    calorias_filtradas=[]
    f_inicio = datetime.strptime(f_inicio, "%d/%m/%Y %H:%M")
    f_fin = datetime.strptime(f_fin, "%d/%m/%Y %H:%M")

    for registro in lista_calorias:
        fecha_registro=registro.fechahora
        if f_inicio < fecha_registro < f_fin:
            calorias=registro.calorias
            calorias=int(calorias)
            calorias_filtradas.append(calorias)
    
    return sum(calorias_filtradas)

from datetime import date
Venta = NamedTuple('Venta',[('fecha', date), ('concesionario', str), ('modelos', str),
                    ('precio', float), ('unidades', int), ('financiado', bool)])
def unidades_vendidas(lista_ventas:list[Venta],conj_modelos:set[str], fecha_inicial:date|None, fecha_final:date|None)->int:
    conj_modelos=set()
    lista_fil=[unidades.modelos for unidades in lista_ventas]
    return sum(unidades.unidades for unidades in lista_ventas if unidades.modelos in conj_modelos)

from collections import defaultdict
def dicc_ganancias_por_año(lista_ventas:list[Venta],n:int)->dict[int,list[tuple[str,float]]]:
    dict=defaultdict(int,list[tuple[str,float]])
    for r in lista_ventas:
        ganancia_bruta=r.unidades*r.precio
        tupla=(r.modelos, ganancia_bruta)
        dict[r.fecha.year].append(tupla)
        sorted(dict.items(), key=lambda x:x[1], reverse=True)

    return dict[:n]
    resultado = {}
    for año, ventas in dict.items():
        ventas_ordenadas = sorted(ventas, key=lambda x: x[1], reverse=True)[:n]
        resultado[año] = ventas_ordenadas

    return resultado

def max_unidades(lista_ventas:list[Venta])->int:
    dict=defaultdict(int)
    for r in lista_ventas:
        clave=r.fecha.day
        dict[clave]+=r.unidades
    return max(dict[clave], key=lambda x:x[1])[1]

def fechas_de_mas_ventas(lista_ventas:list[Venta])->list[date]:
    lista_fecha_max_unidades=[]
    tope_de_ventas=max_unidades(lista_ventas)
    dict=defaultdict(int)
    for r in lista_ventas:
        clave=r.fecha.year
        dict[clave]+=r.unidades
        if dict[clave]==tope_de_ventas:
            lista_fecha_max_unidades.append(dict[clave][1])
    return lista_fecha_max_unidades

def beneficio(lista_ventas:list[Venta])->float:
    for r in lista_ventas:
        ganancia_bruta=r.unidades*r.precio
        if r.financiado==True:
            return ganancia_bruta*0.05
        else:
            return ganancia_bruta*0.01

def concesionario_mas_beneficio_modelo(lista_ventas:list[Venta],modelo:str|None)->str:
    for r in lista_ventas:
        if modelo != None:
            if r.modelos == modelo:
                lista_beneficios=[beneficio(lista_ventas)]
        if modelo == None:
            lista_beneficios=[beneficio(lista_ventas)]
    return max(lista_beneficios)