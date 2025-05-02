from clima_lectura import *
from collections import Counter, defaultdict



'''1. Devuelve un diccionario que a cada año le haga 
corresponder un contador con el número de registros de ese año.'''
def diccionario_contador_por_año(lista:list[RegistroClima])->dict[int,int]:
    dicc={} # dicc=dict()
    for r in lista:
        clave=r.fecha.year
        if clave in dicc:
            dicc[clave]+=1
        else:
            dicc[clave]=1
    return dicc


'''2.   Devuelve un diccionario tal que dado un año 
asigna a cada mes del año el número de registros de ese mes.'''
def diccionario_contador_por_mes(lista:list[RegistroClima], año:int)->dict[int, int]:
    dicc=dict()
    for r in lista:
        if r.fecha.year==año:
            clave=r.fecha.month
            if clave in dicc:
                dicc[clave]+=1
            else:
                dicc[clave]=1
    return dicc

def diccionario_contador_por_mes2(lista:list[RegistroClima], año:int)->dict[int, int]:
    dicc=dict()
    lista_fil=[r for r in lista if r.fecha.year==año]
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc:
            dicc[clave]+=1
        else:
            dicc[clave]=1
    return dicc


'''3.  Repita el ejercicio 2 usando el tipo Counter.'''
def diccionario_contador_por_mes_counter(lista:list[RegistroClima], año:int)->dict[int, int]:
    return Counter(r.fecha.month for r in lista if r.fecha.year==año)


'''4.  Devuelva un diccionario tal que dado un año devuelva 
para cada mes la lluvia acumulada en ese mes.'''
def diccionario_lluvia_acumulada_por_mes(lista:list[RegistroClima], año:int)->dict[int, float]:
    dicc=dict()
    for r in lista:
        if r.fecha.year==año:
            clave=r.fecha.month
            if clave in dicc:
                dicc[clave]+=r.lluvia
            else:
                dicc[clave]=r.lluvia
    return dicc

def diccionario_lluvia_acumulada_por_mes2(lista:list[RegistroClima], año:int)->dict[int, float]:
    dicc=dict()
    lista_fil=[r for r in lista if r.fecha.year==año]
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc:
            dicc[clave]+=r.lluvia
        else:
            dicc[clave]=r.lluvia
    return dicc


'''5.  Repita el ejercicio 5 usando el tipo defaultdict.'''
def diccionario_lluvia_acumulada_por_mes3(lista:list[RegistroClima], año:int)->dict[int, float]:
    dicc=defaultdict(float)
    lista_fil=[r for r in lista if r.fecha.year==año]
    for r in lista_fil:
        clave=r.fecha.month
        dicc[clave]+=r.lluvia 
    return dicc


'''6.   Dado un año devuelva un diccionario tal que asocie a
 cada mes de ese año la temperatura máxima media de ese mes.'''
def diccionario_tempmax_media_por_mes(lista:list[RegistroClima], año:int)->dict[int, float]:
    lista_fil=[r for r in lista if r.fecha.year==año]
    dicc_contador=Counter(r.fecha.month for r in lista_fil)
    dicc_suma=dict()
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc_suma:
            dicc_suma[clave]+=r.temp_max
        else:
            dicc_suma[clave]=r.temp_max
    dicc_media={}
    for mes in dicc_suma:
        dicc_media[clave]=dicc_suma[clave]/dicc_contador[clave]
    return dicc_media

def diccionario_tempmax_media_por_mes2(lista:list[RegistroClima], año:int)->dict[int, float]:
    lista_fil=[r for r in lista if r.fecha.year==año]
    dicc_contador=dict()
    dicc_suma=dict()
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc_suma:
            dicc_suma[clave]+=r.temp_max
            dicc_contador[clave]+=1
        else:
            dicc_suma[clave]=r.temp_max
            dicc_contador[clave]=1
    dicc_media={}
    for mes in dicc_suma:
        dicc_media[clave]=dicc_suma[clave]/dicc_contador[clave]
    return dicc_media


'''7.   Usando el ejercicio 6 y dado un año devuelva cuál 
es el mes de ese año con la temperatura máxima media mayor.'''
def mes_mayor_tempmax_media(lista:list[RegistroClima], año:int)->int:
    dicc_temp_media=diccionario_tempmax_media_por_mes(lista, año)
    return max(dicc_temp_media.items(), key=lambda x:x[1])[0]


'''Dado un año devuelva un diccionario que haga corresponder a cada mes de ese año una 
lista con los RegistrosClima de ese mes.'''
#Esquema basico diccionario organizador(en este caso por mes)         Tambien se puede dar el caso con conjuntos
def diccionario_registros_por_mes(lista:list[RegistroClima], año:int)->dict[int, list[RegistroClima]]:
    dicc=dict()
    lista_fil=[r for r in lista if r.fecha.year==año]
    for r in lista_fil:
        clave=r.fecha.month
        if clave in dicc:
            dicc[clave].append(r)
        else:
            dicc[clave]=[r]
    return dicc


#Copilot
def diccionario_registros_por_mes(lista:list[RegistroClima], año:int)->dict[int, list[RegistroClima]]:
    dicc=dict()
    for r in lista:
        if r.fecha.year==año:
            clave=r.fecha.month
            if clave in dicc:
                dicc[clave].append(r)
            else:
                dicc[clave]=[r]
    return dicc


'''Dado un año, devuelva un diccionario en el que a cada mes de ese año le haga 
corresponder el día con más lluvia.'''
def diccionario_max_lluvia_por_mes(lista:list[RegistroClima], año:int)->dict[int, datetime]:
    dicc_organizador=diccionario_registros_por_mes(lista, año)
    dicc=dict()
    for mes in dicc_organizador:
        dicc[mes]=max(dicc_organizador[mes], key=lambda x:x.lluvia).fecha
    return dicc
#Copilot
def diccionario_dia_max_lluvia_por_mes_copilot(lista:list[RegistroClima], año:int)->dict[int, list]:
    dicc=dict()
    for r in lista:
        if r.fecha.year==año:
            clave=r.fecha.month
            if clave in dicc:
                if r.lluvia>dicc[clave]:
                    dicc[clave]=r.lluvia
            else:
                dicc[clave]=r.lluvia
    return dicc


'''Devuelve un diccionario en el que las claves sean los años y los valores el día más frio 
de cada año.'''
def diccionario_dia_mas_frio_por_año(lista:list[RegistroClima])->dict[int, datetime]:
    dicc_organizador=dict()
    for r in lista:
        clave=r.fecha.year
        if clave in dicc_organizador:
            dicc_organizador[clave].append(r)
        else:
            dicc_organizador[clave]=[r]
    dicc=dict()
    for año in dicc_organizador:
        dicc[año]=min(dicc_organizador[año], key=lambda x:x.temp_min).fecha
    return dicc
#Copilot
def diccionario_dia_mas_frio_por_año_copilot(lista:list[RegistroClima], año:int)->dict[int, datetime]:
    dicc=dict()
    for r in lista:
        clave=r.fecha.year
        if clave in dicc:
            if r.temp_min<dicc[clave].temp_min:
                dicc[clave]=r
        else:
            dicc[clave]=r
    return dicc

'''Devuelve un diccionario en el que las claves sean los años y los valores el día más frio 
de cada año y su temperatura.'''
def diccionario_dia_mas_frio_por_año_temperatura(lista:list[RegistroClima])->dict[int, tuple[datetime, float]]:
    dicc_organizador=dict()
    for r in lista:
        clave=r.fecha.year
        if clave in dicc_organizador:
            dicc_organizador[clave].append(r)
        else:
            dicc_organizador[clave]=[r]
    dicc=dict()
    for año in dicc_organizador:
        reg_min=min(dicc_organizador[año], key=lambda x:x.temp_min)
        dicc[año]=(reg_min.fecha, reg_min.temp_min)
    return dicc
#Copilot
def diccionario_dia_mas_frio_por_año_temperatura_copilot(lista:list[RegistroClima])->dict[int, tuple[datetime, float]]:
    dicc_organizador=dict()
    for r in lista:
        clave=r.fecha.year
        if clave in dicc_organizador:
            dicc_organizador[clave].append(r)
        else:
            dicc_organizador[clave]=[r]
    dicc=dict()
    for año in dicc_organizador:
        r=min(dicc_organizador[año], key=lambda x:x.temp_min)
        dicc[año]=(r.fecha, r.temp_min)
    return dicc