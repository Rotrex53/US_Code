from avistamientos2 import *

'''Implemente  una  función  que  lea  un  fichero  con  una  estructura  como  la  descrita  y 
devuelva una lista de tuplas, según el namedtuple que se proporciona. '''
def leer_avistamientos(fichero: str) -> list[Avistamiento]:
    with open(fichero, encoding="utf-8") as f:
        lista_avistamientos = []
        lector = csv.reader(f)
        next(lector)
        
        for fecha, ciudad, estado, forma, duracion, comentarios, latitud, longitud in lector:
            fechahora=datetime.datetime.strptime(fecha,"%m/%d/%Y %H:%M")
            duracion=float(duracion)
            coordenadas=Coordenadas(float(latitud), float(longitud))
            
            r=Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, coordenadas)
            lista_avistamientos.append(r)
    
    return lista_avistamientos


'''Implemente una función tal que dada una fecha devuelva el número de avistamientos que 
se han producido en esa fecha.'''
def contador_fecha(lista_avistamientos:list[Avistamiento], fecha:date)-> int:
    contador = 0
    for registro in lista_avistamientos:
        if registro.fechahora.date() == fecha:
            contador += 1
    return contador

def contador_fecha2(lista_avistamientos:list[Avistamiento], fecha:date)-> int:
    return sum(1 for avistamiento in lista_avistamientos if avistamiento.fechahora.date() == fecha)


'''Dado un estado implemente una función que devuelva la duración total de los 
avistamientos de ese estado. '''
def duracion_total(lista_avistamientos:list[Avistamiento], estado:str)-> float:
    suma = 0
    for avistamiento in lista_avistamientos:
        if avistamiento.estado.lower() == estado.lower():
            suma += avistamiento.duracion
    return suma

def duracion_total2(lista_avistamientos:list[Avistamiento], estado:str)-> float:
    return sum(avistamiento.duracion for avistamiento in lista_avistamientos if avistamiento.estado.lower() == estado.lower())


'''Implemente  una  función  tal  que  dado  un  conjunto  de  estados  devuelva  el  número  de 
formas distintas de los avistamientos observados en esos estados. '''
def numero_formas_distintas(lista_avistamientos:list[Avistamiento], estados:set[str])-> int:
    conj_formas = set()
    for avistamiento in lista_avistamientos:
        if avistamiento.estado in estados:
            conj_formas.add(avistamiento.forma)
    return len(conj_formas)

def numero_formas_distintas2(lista_avistamientos:list[Avistamiento], estados:set[str])-> int:
    return len({avistamiento.forma for avistamiento in lista_avistamientos if avistamiento.estado in estados})

'''Dada  una  forma  determinada,  devuelve  el  avistamiento  de  mayor  duración  de  entre 
todos los que tienen esa forma. '''
def avistamiento_mayor_duracion(lista_avistamientos:list[Avistamiento], forma:str)-> Avistamiento | None:
    lista_fil= [avistamiento for avistamiento in lista_avistamientos if avistamiento.forma == forma]
    return max(lista_fil, key=lambda x: x.duracion)

# Si se desea que la función anterior devuelva None en caso de no haber avistamientos con esa forma, se puede hacer de la siguiente manera:
def avistamiento_mayor_duracion2(lista_avistamientos:list[Avistamiento], forma:str)-> Avistamiento | None:
    lista_fil= [avistamiento for avistamiento in lista_avistamientos if avistamiento.forma == forma]
    if len(lista_fil) > 0:    
        maximo = max(lista_fil, key=lambda x: x.duracion)
    else:
        maximo = None
    
    return maximo


'''Implemente una función tal que dado un año y una palabra devuelva el avistamiento con 
el  comentario  más  largo  y  la  longitud  de  este  para  los  avistamientos  del  año  y  que 
contenga la palabra dados como argumentos. '''
def avistamiento_comentario_mas_largo(lista_avistamientos:list[Avistamiento], año:int, palabra:str)-> tuple[Avistamiento, int] | None:
    lista_fil= [avistamiento for avistamiento in lista_avistamientos if avistamiento.fechahora.date().year == año and palabra in avistamiento.comentarios]
    if len(lista_fil) > 0:
        maximo = max(lista_fil, key=lambda x: len(x.comentarios))
        maximo = (maximo, len(maximo.comentarios))
    else:
        maximo = None
    return maximo


'''Dado un estado, implemente una función que devuelva el punto medio (longitud y latitud 
media de los avistamientos de ese estado.'''
def punto_medio(lista_avistamientos:list[Avistamiento], estado:str)-> tuple[float, float] | None:
    sum_lat=0.
    sum_lon=0.
    contador=0
    for avistamiento in lista_avistamientos:
        if avistamiento.estado.lower() == estado.lower():
            sum_lat+=avistamiento.coordenadas.latitud
            sum_lon+=avistamiento.coordenadas.longitud
            contador+=1

    if contador > 0:
        punto_medio = (sum_lat/contador, sum_lon/contador)
    else:
        punto_medio = None
    
    return punto_medio


'''Usando  la  función  distancia  de  Coordenadas,  construya  una  función  que  tiene  como 
entrada unas coordenadas ubicacion y un radio r y devuelve los avistamientos que se han 
situado dentro de un radio r a ubicación. '''
def avistamientos_en_radio(lista_avistamientos:list[Avistamiento], ubicacion:Coordenadas, r:float)-> list[Avistamiento]:
    return [avistamiento for avistamiento in lista_avistamientos if distancia(avistamiento.coordenadas, ubicacion) < r]


'''Implemente  una  función  que  devuelva  una  lista  ordenada  por  fecha  (de  más  reciente  a 
más antigua) con los avistamientos entre  fecha_inicial  y fecha_final (ambas inclusive). Si 
fecha_inicial  es  None,  entonces  se  devolverán  todos  los  registros  hasta  la  fecha_final.  Si 
fecha_final es  None,  entonces  se  devolverán todos  los  registros  desde  la  fecha_inicial.  Si 
ambas fechas son None, se devuelve la lista de registros completa. '''
def filtra_entre_fechas(lista_avistamientos:list[Avistamiento], fecha_ini:date = None, fecha_fin:date = None)-> list[Avistamiento]:
    lista_filtrada = []
    if fecha_ini == None and fecha_fin == None:
        lista_filtrada = lista_avistamientos
    elif fecha_ini == None:
        lista_filtrada = [avistamiento for avistamiento in lista_avistamientos if avistamiento.fechahora.date() <= fecha_fin]
    elif fecha_fin == None:
       lista_filtrada = [avistamiento for avistamiento in lista_avistamientos if avistamiento.fechahora.date() >= fecha_ini]
    else:
        lista_filtrada = [avistamiento for avistamiento in lista_avistamientos if fecha_ini <= avistamiento.fechahora.date() <= fecha_fin]

    return sorted(lista_filtrada, key=lambda x: x.fechahora, reverse=True)

#Mejor solución
def filtra_entre_fechas2(lista_avistamientos:list[Avistamiento], fecha_ini:date = None, fecha_fin:date = None)-> list[Avistamiento]:
    lista_filtrada = []
    if fecha_ini == None:
        fecha_ini = datetime.datetime(1700,1,1).date()
    if fecha_fin == None:
        fecha_fin = datetime.datetime(2020,1,1).date()
    lista_filtrada = [avistamiento for avistamiento in lista_avistamientos if fecha_ini <= avistamiento.fechahora.date() <= fecha_fin]
    return sorted(lista_filtrada, key=lambda x: x.fechahora, reverse=True)