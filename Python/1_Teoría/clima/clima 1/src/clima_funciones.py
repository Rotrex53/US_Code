from clima_lectura import *


'''Dadas dos fechas devuelve una lista con solo los registros entre esas dos fechas ambas 
incluidas.'''

def filtra_entre_fechas(lista:list[RegistroClima], fecha1:datetime, fecha2:datetime)->list[RegistroClima]:
    lista_fil=[]
    for r in lista:
        if fecha1 <= r.fecha <= fecha2:
            lista_fil.append(r)
    return lista_fil


'''Dadas dos cadenas de caracteres representando dos fechas con el formato “día/mes/año” 
devuelve una lista con los registros entre esas dos fechas ambas incluidas.'''

def filtra_entre_fechas_cadenas(lista:list[RegistroClima], fecha1:str, fecha2:str)->list[RegistroClima]:
    f1=datetime.strptime(fecha1, "%d/%m/%Y").date()
    f2=datetime.strptime(fecha2, "%d/%m/%Y").date()
    return filtra_entre_fechas(lista, f1, f2)


'''Devolver el día más frio.'''

def filtra_dia_mas_frio(lista:list[RegistroClima])->RegistroClima:
    dia_mas_frio=min(lista, key=lambda x: x.temp_min) #tambien x:x[3]
    return dia_mas_frio


'''Devolver el día con más lluvia.'''

def filtra_dia_mas_lluvioso(lista:list[RegistroClima])->RegistroClima:
    dia_mas_lluvioso=max(lista, key=lambda x: x.lluvia) #tambien x:x[3]
    return dia_mas_lluvioso


'''Dado un año devolver el día más frio de ese año y la temperatura mínima'''

#1ª opción: muy compacto, inconveniente que hace dos recorridos, lista_f y regmin
            #OJO: si estuviese vacía la lista deberiamos añadir una linea para comprobar que si esta vacía devolver None
def filtra_dia_mas_frio_año(lista:list[RegistroClima], año:int)->tuple[datetime, float]:
    lista_f=[r for r in lista if r.fecha.year==año]
    regmin=min(lista_f, key=lambda x:x.temp_min)
    return regmin.fecha, regmin.temp_min

#2ª opción: menos compacto, ventaja es solo 1 bucle
            #OJO: si al inicializar temp_min al primer elemento es mayor que cualquiera otra temperatura 
                # va a devolver vacio todo, por eso se podria incializar con un numero suficientemente 
                # grande como para que no sea una temp_min y a partir de ahi vaya filtrando-> temp_min=1000
def filtra_dia_mas_frio_año2(lista:list[RegistroClima], año:int)->tuple[datetime, float]:
    temp_min=lista[0].temp_min
    fecha_min=lista[0].fecha
    for r in lista:
        if r.fecha.year==año:
            if r.temp_min<temp_min:
                temp_min=r.temp_min
                fecha_min=r.fecha
    return fecha_min, temp_min


'''Dado un mes devolver el día con más lluvia de ese mes'''

def dia_mas_lluvia_mes(lista:list[RegistroClima], mes:int)->tuple[datetime, float]:
    lista_f=[r for r in lista if r.fecha.year==mes]
    regmax=min(lista_f, key=lambda x:x.lluvia)
    return regmax.fecha, regmax.lluvia


'''Hacer el 6 (dia_mas_lluvia_mes) reusando el 4 (filtra_dia_mas_lluvioso)'''

def dia_mas_lluvia_mes2(lista:list[RegistroClima], mes:int)->tuple[datetime, float]:
    lista_f=[r for r in lista if r.fecha.year==mes]
    regmax=filtra_dia_mas_lluvioso(lista_f)
    #para poder hacer esto bien filtra_dia_mas_lluvioso debe devolver el registro
    #completo, no solo la fecha, es decir, en return no prondria .fecha
    return regmax.fecha, regmax.lluvia


'''Dado un año obtener la lluvia acumulada de ese año'''

def lluvia_acumulada_año(lista:list[RegistroClima], año:int)->float:
    suma=0
    for t in lista:
        if t.fecha.year==año:
            suma+=t.lluvia
    return suma

def lluvia_acumulada_año2(lista:list[RegistroClima], año:int)->float:
    return sum(t.lluvia for t in lista if t.fecha.year==año)


'''Dada una lista de años devuelve la temperatura máxima media de esos años'''
#usamos la media, novedad: no es solo un año, recibe una lista de años
#1ª opción: con el for
def temp_media(lista:list[RegistroClima], lista_años:list[int])->float:
    suma=0
    contador=0
    for t in lista:
        if t.fecha.year in lista_años:
            suma+=t.temp_max
            contador+=1

    if contador>0:
        media=suma/contador
    else:
        media=None

    return media

def temp_media2(lista:list[RegistroClima], lista_años:list[int])->float:
    lista_f=[t.temp_max for t in lista if t.fecha.year in lista_años]
    suma=sum(lista_f)
    contador=len(lista_f)
    if contador>0:
        media=suma/contador
    else:
        media=None
    return media

#diccionarios
diccionario=dict()

codigo_postal={"Bami":41013, "Reina Mercedes":41012, "Bellavista":41014, "Heliopolis":41012}

vuelos={"Iberia": ["Madrid", "Barcelona", "Valencia"]}

#print(codigo_postal["Bami"])

for t in codigo_postal:
    print(t, codigo_postal[t])


lista=["ana", "julia", "pepe", "manuel"]
lista.sort()
print(lista)

'''
return lista.sort()
return sorted(lista)
lista.sort()
return lista

lista.sort(list_tuplas, key=lambda x:x.campo)
#no se puede hacer un sort para devolver un minimo/maximo
'''

#si quiero ordenar los elementos de lista por su tamaño:
lista=[[1,2,3],[2,5],[1],[1,6,5,5]]
lista.sort(key=lambda x:len(x))
print(lista)        #esta ordenando las listas por el numero de elementos que tienen cada una de ellas