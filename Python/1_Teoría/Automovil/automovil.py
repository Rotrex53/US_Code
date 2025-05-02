'''# nombre: Cadena de caracteres con Marca y Modelo separados por un blanco (por ejemplo “Skoda Fabia”)
# fecha: Fecha de diseño
# electrico: Booleano que indica si el vehículo tiene opción eléctrica.
# colores: Conjunto de colores disponibles de tipo set[str]
# paises: Conjunto de países donde se vende de tipo set[str]
# matriculaciones: Lista de matrículas de los automóviles vendidos en orden de venta de tipo list[str'''

from datetime import datetime
from typing import NamedTuple


Automovil = NamedTuple('Automovil', [('marca',str),( 'fecha',datetime),( 'electrico',bool),( 'colores',set[str]),
('paises',set[str]),( 'matriculaciones',list[str])])



'''EXPRESIONES'''

#1. Inicialice una variable de tipo Automóvil con los datos que quiera
a1=Automovil("Skoda Fabia", datetime(2021,10,21).date(),False,{"Blanco","Rojo"},{"España","Francia"},["0605GTR","6653VTV","1937RWE"])
a2=Automovil("Skoda Fabia", datetime(2021,10,21).date(),False,{"Blanco","Rojo"},{"España","Francia"},["0605GTR","6653VTV","1937RWE"])
a3=Automovil("Skoda Fabia", datetime(2021,10,21).date(),False,{"Blanco","Rojo"},{"España","Francia"},["0605GTR","6653VTV","1937RWE"])

#2. El automóvil a1 se diseñó antes de 2023
a1.fecha.year<2023

#3. El automóvil a2 es eléctrico y está disponible en color Negro
a1.electrico and "Negro" in a1.colores

#4. La última matriculación del automóvil a3 es 5434MLP
a1.matriculaciones[-1] == "5434MLP"

#5. Ni a1 ni a2 son eléctricos pero a3 sí
a1.electrico==False
a1.electrico==False and a2.electrico==False and a3.electrico

#6. Del automóvil a2 se han vendido al menos 5 coches
len(a1.matriculaciones)>=5

#7. El automóvil a1 se vende en España pero no en Italia
"España" in a1.paises and not "Italia" in a1.paises

#8. El automóvil a1 se vende en más países que el a2 pero en menos que el a3
len(a3.paises)>len(a1.paises)>len(a2.paises)

#9. El automóvil a1 se vende en más países que el a2 o tiene más colores que el a3
len(a1.paises)>len(a2.paises) or len(a1.colores)>len(a3.colores)

#10. El automóvil a1 se vende en Francia o España pero no en ambos              [Esto es un "or" exclusivo == EXOR]    ![](automovil.p\9c6d0f14-0e91-f605-c42f-4df706e398ff.svg)
("España" in a1.paises or "Francia" in a1.paises) and not ("España" in a1.paises and "Francia" in a1.paises)

#11. La primera matriculación del automóvil a2 empieza por el mismo DÍGITO que la primera matriculación del automóvil a3
a1.matriculaciones[0][0]==a3.matriculaciones[0][0]

#Si quiero saber si un automovil es Skoda
"Skoda" in a1.marca

#Si quiero saber si un automovil es modelo Fabia
"Fabia" in a1.marca



'''FUNCIONES'''

#1. Dada una lista de tuplas de tipo Automovil devuelva el número total de vehículos matriculados de una marca dada.
def suma_matriculaciones(lista:list[Automovil], marca:str)->int:
    suma=0
    for vehiculo in lista:
        if marca in vehiculo.marca:
            suma+=len(vehiculo.matriculaciones)
    return suma

#2. Dada una lista de tuplas de tipo Automovil devuelva la marca y modelo del vehículo con más matriculaciones.     (no entra)
def mayor_matriculaciones(lista:list[Automovil])->str:     #Se puede resolver por diccionario o por una lista de tuplas
    lista_res=[]
    for a in lista:
        tupla=(len(a.matriculaciones), a.marca)
        lista_res.append(tupla)

    return max(lista_res)[0]

        #Lo mismo pero si se diera que hay marcas o/y modelos REPETIDOS
def mayor_matriculaciones2(lista:list[Automovil], marca:str)->int:
    conjunto_marca=set()
    for a in lista:
        conjunto_marca.add(a.marca)

    lista_res=list()
    for marca in conjunto_marca:
        valor=num_matriculaciones(lista, marca)
        tupla=(valor, marca)
        lista_res.append(tupla)
    
    return max(lista_res)[1]

def num_matriculaciones(lista:list[Automovil], marca:str)->int:
    suma=0
    for vehiculo in lista:
        if marca == vehiculo.marca:
            suma+=len(vehiculo.matriculaciones)

    return suma

#3. Dada una lista de tuplas de tipo Automovil devuelve el número total de matriculaciones.

def total_matriculaciones(lista:list[Automovil], marca:str)->int:
    return sum(len(v.matriculaciones) for v in lista)

#4. Dada una lista de tuplas de tipo Automovil devuelve un conjunto con los colores disponibles para
#   una marca dada. Defina previamente una función que devuelva el conjunto unión de dos pasados
#   como argumentos

def union_conjunto(conj1:set[str], conj2:set[str])->set[str]:
    conj_res=conj1
    for e in conj2:              #esto es un acumulador (unir conjuntos)
        conj_res.add(e)        

    return conj_res

def union_conjunto2(conj1:set[str], conj2:set[str])->set[str]:
    conj_res=conj1.union(conj2)        #lo aquivalente seria esto

    return conj_res

def colores_disponibles(lista:list[Automovil], marca:str)->set[str]:
    conj_res=set()
    for vehiculo in lista:
        if marca in vehiculo.marca:
            conj_res=union_conjunto(conj_res, vehiculo.colores)

    return conj_res

#5. Dada una lista de tuplas de tipo Automovil devuelve una lista ordenada de las fechas de diseño de
#   los vehículos que tienen opción eléctrica.
def lista_fechas_electricos(lista:list[Automovil])->list:
    lista_filtrada=[v.fecha for v in lista if v.electrico]
    lista_filtrada.sort()

    return lista_filtrada
