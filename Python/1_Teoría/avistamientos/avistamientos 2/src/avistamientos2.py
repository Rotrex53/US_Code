from typing import NamedTuple
import csv
import datetime
from datetime import date
from coordenadas2 import distancia
from collections import defaultdict, Counter

Avistamiento = NamedTuple("Avistamiento",[("fechahora", datetime), ("ciudad", str), ("estado", str), ("forma", str), ("duracion", float), ("comentarios", str), ("coordenadas", "Coordenadas")])
Coordenadas = NamedTuple('Coordenadas', [('latitud', float), ('longitud', float)])

'''Implemente una función que devuelva el número de avistamientos por año. Hágalo con los 
tipos dict, Counter y defaultdict.'''
#dict
def contador_por_año(lista_avistamientos:list[Avistamiento])-> dict[int, int]:
    diccionario = {}
    for avistamiento in lista_avistamientos:
        año = avistamiento.fechahora.datetime().year
        if año in diccionario:
            diccionario[año] += 1
        else:
            diccionario[año] = 1
    return diccionario

#defaultdict        Es para evitar preguntar si la clave está en el diccionario
def contador_por_año_defaultdict(lista_avistamientos:list[Avistamiento])-> dict[int, int]:
    diccionario = defaultdict(int)
    for avistamiento in lista_avistamientos:
        año = avistamiento.fechahora.datetime().year
        diccionario[año] += 1
    return diccionario

#Counter
def contador_por_año_counter(lista_avistamientos:list[Avistamiento])-> dict[int, int]:
    return Counter(avistamiento.fechahora.datetime().year for avistamiento in lista_avistamientos)


'''Implemente una función que devuelva cuál es el año con más avistamientos'''
def año_con_mas_avistamientos(lista_avistamientos:list[Avistamiento])-> int:
    diccionario = contador_por_año(lista_avistamientos)
    diccionario.items()
    maximo = max(diccionario.items(), key=lambda x: x[1])       #diccionario.items() es una lista de tuplas, por lo que se puede usar un max() con una key
    return maximo[0]            #Cuando se pide un maximo no se utiliza un sorted() y devolver el ultimo elemento, sino usar el maximo

def año_con_mas_avistamientos_counter(lista_avistamientos:list[Avistamiento])-> int:
    diccionario = Counter(contador_por_año_counter(lista_avistamientos))
    maximo = diccionario.most_common(1)[0][0]       #esto seria -> diccionario.most_common(1)=[(2010, 10)] -> diccionario.most_common(1)[0]=(2010, 10) -> diccionario.most_common(1)[0][0]=2010
    return maximo[0]


'''Dada una forma, implemente una función que devuelva el año con más avistamientos de esa forma. '''
def año_con_mas_avistamientos_forma_counter(lista_avistamientos:list[Avistamiento], forma:str)-> int:
    diccionario = Counter(avistamiento.fechahora.datetime().year for avistamiento in lista_avistamientos if avistamiento.forma == forma)
    maximo = diccionario.most_common(1)[0][0]
    return maximo


'''Implemente una función que devuelva la hora en la que se producen más avistamientos.'''
def hora_con_mas_avistamientos(lista_avistamientos:list[Avistamiento])-> int:
    diccionario = Counter(avistamiento.fechahora.datetime().hour for avistamiento in lista_avistamientos)
    maximo = diccionario.most_common(1)[0][0]
    return maximo


'''Implemente una función que devuelva un diccionario que relaciona cada fecha como clave 
con el conjunto de los avistamientos de esa fecha. '''
#dict
def conjunto_avistamientos_por_fecha(lista_avistamientos:list[Avistamiento])-> dict[date, set[Avistamiento]]:
    diccionario = {}
    for avistamiento in lista_avistamientos:
        clave = avistamiento.fechahora.date()
        if clave in diccionario:
            diccionario[clave].add(avistamiento)
        else:
            diccionario[clave] = {avistamiento}
    return diccionario

#defaultdict
def conjunto_avistamientos_por_fecha_defaultdict(lista_avistamientos:list[Avistamiento])-> dict[date, list[Avistamiento]]:
    diccionario = defaultdict(set)
    for avistamiento in lista_avistamientos:
        clave = avistamiento.fechahora.date()
        diccionario[clave].add(avistamiento)
    return diccionario

        #cual es la fecha con mayor numero de formas distintas de avistamiento
def fecha_con_mas_formas_distintas(lista_avistamientos:list[Avistamiento])-> date:
    diccionario = conjunto_avistamientos_por_fecha(lista_avistamientos)
    dicc_formas={}
    for avistamientos in diccionario:
        formas={r.forma for r in diccionario[avistamientos]}
        dicc_formas[avistamientos]=formas

    return max(dicc_formas, key=lambda x: len(x[1]))[0]


'''Implemente  una  función  que  devuelva  un  diccionario  con  los  meses  como  claves  y  los 
valores son el conjunto de formas distintas de avistamientos ese mes.'''
def formas_distintas_por_mes(lista_avistamientos:list[Avistamiento])-> dict[int, set[str]]:
    diccionario = {}
    for avistamiento in lista_avistamientos:
        clave = avistamiento.fechahora.datetime().month
        if clave in diccionario:
            diccionario[clave].add(avistamiento.forma)
        else:
            diccionario[clave] = {avistamiento.forma}
    return diccionario


'''Implemente una función que devuelva un diccionario en el que las claves son las formas de 
los avistamientos, y los valores el porcentaje de avistamientos con dicha forma.'''
#tipos de diccionario:
#   contador
#   sumador
#   organizador a lista
#   organizador a conjunto
#   media
#   porcentaje (parecido a media)

#todos tienen la variante de máximo

def porcentaje_formas(lista_avistamientos:list[Avistamiento])-> dict[str, float]:
    dicc_cont = Counter(avistamiento.forma for avistamiento in lista_avistamientos)
    total_avistamientos = len(lista_avistamientos)
    dicc_porc={}
    for forma in dicc_cont:
        dicc_porc[forma]=dicc_cont[forma]/total_avistamientos*100
    return dicc_porc


'''Para averiguar la zona de mayor número de avistamientos, vamos a reducir las coordenadas 
de  longitud  y  latitud  a  su  parte  entera.  Implemente  de  forma  auxiliar  una  función  que 
devuelva un diccionario donde las claves sean la parte entera de la longitud y latitud y los 
valores un contador.'''
def contador_coordenadas_enteras(lista_avistamientos:list[Avistamiento])-> dict[tuple[int, int], int]:
    dicc_cont = Counter((int(avistamiento.coordenadas.latitud), int(avistamiento.coordenadas.longitud)) for avistamiento in lista_avistamientos)
    return dicc_cont
#si nos piden la zona con mayor numero de avistamientos
#return Counter((int(avistamiento.coordenadas.latitud), int(avistamiento.coordenadas.longitud)) for avistamiento in lista_avistamientos).most_common(1)[0][0]


'''Implemente una función tal que dado un año que por defecto toma el valor None, devuelve 
la media de días transcurridos entre dos avistamientos consecutivos del año especificado. 
Si en la llamada no se especifica año, entonces se calculará para todos los años. '''
#lo primero seria ordenar los avistamientos por fecha
#luego calcular la diferencia de dias entre dos avistamientos consecutivos segun el año

#       dada una lista de valores calcula la media de los incrementos entre dos valores consecutivos
#       ejemplo:[2,5,3,7,8,6,5] -> [3,2,-4,1,-2,-1] -> 3+2-4+1-2-1= -1
def lista_diferencias(lista:list[int])-> float:
    lista_dif=[]
    for i in range(len(lista)-1):
        diferencia = lista[i+1]-lista[i]
        lista_dif.append(diferencia)
    
    return sum(lista_dif)/len(lista_dif)

def lista_diferencias2(lista:list[int])-> float:
    lista_dif=[]
    for i,j in zip(lista, lista[1:]):
        lista_dif.append(j-i)
    return sum((lista_dif)/len(lista_dif))

#       fecha1 - fecha2 = duration -> se indica como (fecha1 - fecha2).days (funcion especial de Python que mide intervalos de tiempo entre dos fechas)

def media_dias_transcurridos(lista_avistamientos:list[Avistamiento], año:int = None)-> float:
    #primera solucion
    if año == None:
        lista_fil=lista_avistamientos
    else:
        lista_fil=[avistamiento for avistamiento in lista_avistamientos if avistamiento.fechahora.datetime().year == año]
    
    #segunda solucion
    if año != None:
        lista_fil=[avistamiento for avistamiento in lista_avistamientos if avistamiento.fechahora.datetime().year == año]
    
    #tercera solucion
    lista_fil=[avistamiento for avistamiento in lista_avistamientos if año == None or avistamiento.fechahora.datetime().year == año]

    lista_dif=[]
    lista_fil.sort(key=lambda x: x.fechahora)       #esto es para ordenar la lista por fecha cuando nos pidan valores consecutivos (sobretodo)
    for i in range(len(lista_fil)):
        dif_fechas=(lista_fil[i+1].fechahora.date()-lista_fil[i].fechahora.date() ).days       #esto es posible ya que en Python se puedem restar dos fechas ya que existe el tipo duration
        lista_dif.append(dif_fechas)
    #si nos dijeran que si no hay Avistamientos en ese Año deuvuelva None:
    if len(lista_dif) == 0:
        return None

    return sum((lista_dif)/len(lista_dif))


'''Implemente una función que devuelva un diccionario en el que las claves son los estados y 
los valores la longitud media de los comentarios de cada estado.'''
def dicc_media_comentarios(lista_avistamientos:list[Avistamiento])-> dict[str, float]:
    dicc_cont = dict()
    dicc_suma = dict()
    for r in lista_avistamientos:
        if r.estado in dicc_cont:
            dicc_cont[r.estado] += 1
            dicc_suma[r.estado] += len(r.comentarios)
        else:
            dicc_cont[r.estado] = 1
            dicc_suma[r.estado] = len(r.comentarios)
    dicc=dict()
    for estado in dicc_cont:
        dicc[estado]=dicc_suma[estado]/dicc_cont[estado]
    
    return dicc


'''Implementa una función que devuelva un diccionario donde las claves sean los estados, y 
los valores sean una lista con las n mayores duraciones de los avistamientos de cada estado, 
ordenadas de mayor a menor. El valor de n por defecto será 3. '''
#OJO, esquema de diccionario "a doble vuelta" que VA A ENTRAR
def dicc_mayores_duraciones_por_estados(lista_avistamientos:list[Avistamiento], n:int = 3)-> dict[str, list[float]]:
    dicc=defaultdict(list)
    for r in lista_avistamientos:
        dicc[r.estado].append(r.duracion)
    for estado in dicc:
        dicc[estado]=sorted(dicc[estado], reverse=True)[:n]
    
    return dicc


'''Implemente una función tal que devuelva una lista de tuplas (mes, número de apariciones 
en ese mes) para todos los meses. '''
def contador_por_mes(lista_avistamientos:list[Avistamiento])-> list[tuple[int, int]]:
    dicc_cont=Counter(avistamiento.fechahora.datetime().month for avistamiento in lista_avistamientos)
    return [(mes, dicc_cont[mes]) for mes in range(1, 13)]


'''Implemente una función tal que dado n devuelva una lista de n tuplas con el nombre y el 
número de avistamientos de los estados con mayor número de avistamientos, ordenados 
de mayor a menor. El número n será 5 por defecto. '''
def lista_mayor_avistamientos(lista_avistamientos:list[Avistamiento], n:int = 5)-> list[tuple[str, int]]:
    dicc=defaultdict(int)
    for r in lista_avistamientos:
        dicc[r.estado]+=1
    return sorted(dicc.items(), key=lambda x: x[1], reverse=True)[:n]

def lista_mayor_avistamientos_Counter(lista_avistamientos:list[Avistamiento], n:int = 5)-> list[tuple[str, int]]:
    dicc=Counter(r.estado for r in lista_avistamientos)
    return dicc.most_common(n)              #la funcion most_common() se utiliza cuando nos dicen que 
                                            #queremos los n elementos mas comunes