from nombres import *

def test_leer_frecuencias_nombres(lista_r):
    print(f"la primera linea es: {lista_r[0]}")
    print(f"la última linea es: {lista_r[-1]}")
    print(f"se han leído {len(lista_r)} líneas")

def test_filtrar_por_genero(lista_r):
    genero_elegido=None
    lista_f=filtrar_por_genero(lista_fichero=lista_r,genero=genero_elegido)
    print(f"El registro según el genero es: {lista_f}")

def test_calcular_nombres(lista_r):
    genero_elegido="Hombre"
    lista_f=calcular_nombres(lista_fichero=lista_r,genero=genero_elegido)
    print(f"el conjunto segun el genero {genero_elegido} es {lista_f}")

def test_calcular_top_nombres_de_año(lista_r):
    año_elegido = 2020
    num_limite_elegido = 5
    genero_elegido = "Hombre"
    top_nombres = calcular_top_nombres_de_año(lista_fichero=lista_r, año=año_elegido, num_limite=num_limite_elegido, genero=genero_elegido)
    print(f"Los top {num_limite_elegido} nombres del año {año_elegido} para el género {genero_elegido} son: {top_nombres}")

def test_calcular_nombres_ambos_generos(lista_r):
    nombres_ambos_generos = calcular_nombres_ambos_generos(lista_fichero=lista_r)
    print(f"El conjunto de nombres de ambos géneros es: {nombres_ambos_generos}")

def test_calcular_nombres_compuestos(lista_r):
    genero_elegido = None
    nombres_compuestos = calcular_nombres_compuestos(lista_fichero=lista_r, genero=genero_elegido)
    print(f"El conjunto de nombres compuestos para el género {genero_elegido} es: {nombres_compuestos}")

def test_calcular_frecuencia_media_nombre_años(lista_r):
    nombre_elegido = "JAVIER"
    año_inicial = 2000
    año_final = 2017
    frecuencia_media = calcular_frecuencia_media_nombre_años(lista_fichero=lista_r, nombre=nombre_elegido, año_inicial=año_inicial, año_final=año_final)
    print(f"La frecuencia media del nombre {nombre_elegido} entre los años {año_inicial} y {año_final} es: {frecuencia_media}")

def test_calcular_año_mas_frecuencia_nombre(lista_r):
    nombre_elegido= "RODRIGO"
    año_mas_frecuente=calcular_año_mas_frecuencia_nombre(lista_fichero=lista_r, nombre=nombre_elegido)
    print(f"Para el nombre {nombre_elegido} el año con mayor frecuencia es {año_mas_frecuente}")

def test_calcular_nombres_mas_frecuentes(lista_r):
    genero_elegido="Hombre"
    n_elegido=5
    decada_elegida=2005
    lista_nombres_filtrados, numero_nombres_por_n=calcular_nombres_mas_frecuentes(lista_fichero=lista_r, genero=genero_elegido, decada=decada_elegida, n=n_elegido)
    print(f"El top {numero_nombres_por_n} de nombres más frecuentes según el genero {genero_elegido} en la decada de {decada_elegida} es {lista_nombres_filtrados}")

def test_calcular_año_frecuencia_por_nombre(lista_r):
    genero_elegido="Hombre"
    diccionario_final=calcular_año_frecuencia_por_nombre(lista_fichero=lista_r, genero=genero_elegido)
    print(f"El diccionario según el género {genero_elegido} es: {diccionario_final}")

def test_calcular_nombre_mas_frecuente_por_año(lista_r):
    genero_elegido="Hombre"
    diccionario_final=calcular_nombre_mas_frecuente_por_año(lista_fichero=lista_r, genero=genero_elegido)
    print(f"El diccionario según el género {genero_elegido} es: {diccionario_final}")

def test_calcular_frecuencia_por_año(lista_r):
    nombre_elegido="RODRIGO"
    lista_tuplas=calcular_frecuencia_por_año(lista_fichero=lista_r, nombre=nombre_elegido)
    print(f"La lista de tuplas (año, frecuencia) para el nombre {nombre_elegido} es: {lista_tuplas}")

def test_mostrar_evolucion_por_año(lista_r):
    nombre_elegido="RODRIGO"
    evolucion = mostrar_evolucion_por_año(lista_fichero=lista_r, nombre=nombre_elegido)
    print(f"La evolución de la frecuencia del nombre {nombre_elegido} es: {evolucion}")

def test_calcular_frecuencias_por_nombre(lista_r):
    resultado = calcular_frecuencias_por_nombre(lista_fichero=lista_r)
    print(f"La frecuencia de cada nombre es {resultado}")

def test_mostrar_frecuencias_nombres(lista_r):
    limite_elegido=10
    resultado = mostrar_frecuencias_nombres(lista_fichero=lista_r, limite=limite_elegido)
    print(f"El diagrama de barras por frecuencia descendente de los {limite_elegido} nombres es: {resultado}")




def funcion_principal():
    lista_r=leer_frecuencias_nombres("C:/Users/rodri/OneDrive/Desktop/US_proyects/Python/2_Laboratorio/6_nombres/data/frecuencias_nombres.csv")
    #test_leer_frecuencias_nombres(lista_r)
    #test_filtrar_por_genero(lista_r)
    #test_calcular_nombres(lista_r)
    #test_calcular_top_nombres_de_año(lista_r)
    #test_calcular_nombres_ambos_generos(lista_r)
    #test_calcular_nombres_compuestos(lista_r)
    #test_calcular_frecuencia_media_nombre_años(lista_r)
    #test_calcular_año_mas_frecuencia_nombre(lista_r)
    #test_calcular_nombres_mas_frecuentes(lista_r)
    #test_calcular_año_frecuencia_por_nombre(lista_r)
    #test_calcular_nombre_mas_frecuente_por_año(lista_r)
    #test_calcular_frecuencia_por_año(lista_r)
    #test_mostrar_evolucion_por_año(lista_r)
    #test_calcular_frecuencias_por_nombre(lista_r)
    test_mostrar_frecuencias_nombres(lista_r)



if __name__=="__main__":
    funcion_principal()