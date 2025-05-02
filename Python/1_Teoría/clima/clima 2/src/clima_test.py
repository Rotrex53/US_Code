from clima_lectura import *
from clima_diccionario import *

def test_diccionario_contador_por_año(lista_r):
    dicc=diccionario_contador_por_año(lista_r)
    print(f"el numero de registros por año es {dicc}")

def test_diccionario_contador_por_mes(lista_r):
    dicc=diccionario_contador_por_mes(lista_r, 1951)
    print(f"el numero de registros por mes es {dicc}")

def test_diccionario_contador_por_mes2(lista_r):
    dicc=diccionario_contador_por_mes2(lista_r, 1951)
    print(f"el numero de registros por mes es {dicc}")

def test_diccionario_contador_por_mes_counter(lista_r):
    dicc=diccionario_contador_por_mes_counter(lista_r, 1951)
    print(f"el numero de registros por mes es {dicc}")

def test_diccionario_lluvia_acumulada_por_mes(lista_r):
    dicc=diccionario_lluvia_acumulada_por_mes(lista_r, 1951)
    print(f"la lluvia acumulada por mes es {dicc}")

def test_diccionario_lluvia_acumulada_por_mes2(lista_r):
    dicc=diccionario_lluvia_acumulada_por_mes2(lista_r, 1951)
    print(f"la lluvia acumulada por mes es {dicc}")

def test_diccionario_lluvia_acumulada_por_mes3(lista_r):
    dicc=diccionario_lluvia_acumulada_por_mes3(lista_r, 1951)
    print(f"la lluvia acumulada por mes es {dicc}")

def test_diccionario_tempmax_media_por_mes(lista_r):
    dicc=diccionario_tempmax_media_por_mes(lista_r, 1951)
    print(f"la lluvia acumulada por mes es {dicc}")

def test_diccionario_tempmax_media_por_mes2(lista_r):
    dicc=diccionario_tempmax_media_por_mes2(lista_r, 1951)
    print(f"la lluvia acumulada por mes es {dicc}")

def test_mes_mayor_tempmax_media(lista_r):
    mes=diccionario_tempmax_media_por_mes(lista_r, 1951)
    print(f"el mes con mayor temperatura maxima media es {mes}")

def test_diccionario_dia_mas_frio_por_año(lista_r):
    dicc=diccionario_dia_mas_frio_por_año(lista_r)
    print(f"el dia mas frio por año es {dicc}")





if __name__=="__main__":
    lista_r=leer_clima("./Python/clima/clima 2/data/madrid.csv")
    #test_diccionario_contador_por_año(lista_r)
    #test_diccionario_contador_por_mes(lista_r)
    #test_diccionario_contador_por_mes2(lista_r)
    #test_diccionario_contador_por_mes_counter(lista_r)
    #test_diccionario_lluvia_acumulada_por_mes(lista_r)
    #test_diccionario_lluvia_acumulada_por_mes2(lista_r)
    #test_diccionario_lluvia_acumulada_por_mes3(lista_r)
    #test_diccionario_tempmax_media_por_mes(lista_r)
    #test_diccionario_tempmax_media_por_mes2(lista_r)
    #test_mes_mayor_tempmax_media(lista_r)
    test_diccionario_dia_mas_frio_por_año(lista_r)