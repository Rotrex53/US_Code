from avistamientos2 import *
from avistamientos2 import Coordenadas
from export_avist1 import *

def test_leer_avistamientos(lista_r):
    print(f"se han leido un total de {len(lista_r)} avistamientos")
    print(f"se han leido {len(lista_r)} avistamientos")
    print("Los primeros 3 avistamientos son:")
    for a in lista_r[:3]:
        print("\t", a)
    print("============================================\n")
    print("Los últimos 3 avistamientos son:")
    for a in lista_r[-3:]:
        print("\t", a)
    print("============================================\n")

def test_contador_fecha(lista_r):
    fecha1 = datetime.datetime(2010, 1, 1).date()
    contador1=contador_fecha(lista_r, fecha1)
    print(f"El número de avistamientos en la fecha {fecha1} es {contador_fecha(lista_r, fecha1)}")
    print(f"El número de avistamientos en la fecha {fecha1} es {contador1}")
    fecha2 = datetime.datetime(2010, 1, 1).date()
    contador=contador_fecha2(lista_r, fecha2)
    print(f"El número de avistamientos en la fecha {fecha2} es {contador_fecha2(lista_r, fecha2)}")
    print(f"El número de avistamientos en la fecha {fecha2} es {contador}")

def test_duracion_total(lista_r):
    estado = "ca"
    duracion=duracion_total(lista_r, estado)
    print(f"La duración total de los avistamientos en el estado {estado} es {duracion}")
    duracion2=duracion_total2(lista_r, estado)
    print(f"La duración total de los avistamientos en el estado {estado} es {duracion2}")

def test_numero_formas_distintas(lista_r):
    estados = {"ca", "tx"}
    formas_filtradas = numero_formas_distintas(lista_r, estados)
    print(f"El número de formas distintas de los avistamientos en los estados {estados} son {formas_filtradas}")
    estados2 = {"ca", "tx", "fl"}
    formas_filtradas2 = numero_formas_distintas2(lista_r, estados2)
    print(f"El número de formas distintas de los avistamientos en los estados {estados2} son {formas_filtradas2}")

def test_avistamiento_mayor_duracion(lista_r):
    forma = "light"
    avistamiento=avistamiento_mayor_duracion(lista_r, forma)
    print(f"El avistamiento de mayor duración con forma {forma} es {avistamiento}")

    forma2 = "luz" #no existe, por tanto, debería devolver None
    avistamiento2=avistamiento_mayor_duracion2(lista_r, forma2)
    print(f"El avistamiento de mayor duración con forma {forma2} es {avistamiento2}")

def test_avistamiento_comentario_mas_largo(lista_r):
    año_elegido = 2010
    palabra_elegida = "bright"
    comentario = avistamiento_comentario_mas_largo(lista_avistamientos=lista_r, año=año_elegido, palabra=palabra_elegida)
    print(f"El comentario más largo es: {comentario}")

def test_punto_medio(lista_r):
    estado = "ca"
    punto_medio_resultado = punto_medio(lista_r, estado)
    print(f"El punto medio de los avistamientos en el estado {estado} es {punto_medio_resultado}")

def test_avistamientos_en_radio(lista_r):
    coordenadas = Coordenadas(37.7749, -122.4194)
    radio = 100
    avistamientos_en_radio_resultado = avistamientos_en_radio(lista_r, coordenadas, radio)
    print(f"Los avistamientos en un radio de {radio} km de las coordenadas {coordenadas} son {avistamientos_en_radio_resultado}")

def test_filtra_entre_fechas(lista_r):
    fecha1 = datetime.datetime(2010, 1, 1).date()
    fecha2 = datetime.datetime(2010, 1, 2).date()
    filtrados = filtra_entre_fechas(lista_r, fecha1, fecha2)
    print(f"Los avistamientos entre las fechas {fecha1} y {fecha2} son:")
    for a in filtrados:
        print("\t", a)

def test_contador_por_año(lista_r):
    contador = contador_por_año(lista_r)
    print(f"El número de avistamientos por año es:")
    for año, cantidad in contador.items():
        print(f"\t{año}: {cantidad}")

def test_contador_por_año_defaultdict(lista_r):
    contador = contador_por_año_defaultdict(lista_r)
    print(f"El número de avistamientos por año es:")
    for año, cantidad in contador.items():
        print(f"\t{año}: {cantidad}")

def test_contador_por_año_counter(lista_r):
    contador = contador_por_año_counter(lista_r)
    print(f"El número de avistamientos por año es:")
    for año, cantidad in contador.items():
        print(f"\t{año}: {cantidad}")

def test_año_con_mas_avistamientos(lista_r):
    año = año_con_mas_avistamientos(lista_r)
    print(f"El año con más avistamientos es {año}")

def test_año_con_mas_avistamientos_counter(lista_r):
    año = año_con_mas_avistamientos_counter(lista_r)
    print(f"El año con más avistamientos es {año}")

def test_año_con_mas_avistamientos_forma_counter(lista_r):
    año = año_con_mas_avistamientos_forma_counter(lista_r)
    print(f"El año con más avistamientos es {año}")




if __name__ == "__main__":
    lista_r = leer_avistamientos("C:/Users/rodri/OneDrive/Desktop/US_proyects/Python/avistamientos/avistamientos 1/data/ovnis.csv")
    #test_leer_avistamientos(lista_r)
    #test_contador_fecha(lista_r)
    #test_duracion_total(lista_r)
    #test_numero_formas_distintas(lista_r)
    #test_avistamiento_mayor_duracion(lista_r)
    #test_avistamiento_comentario_mas_largo(lista_r)
    #test_punto_medio(lista_r)
    #test_avistamientos_en_radio(lista_r)
    #test_filtra_entre_fechas(lista_r)
    #test_contador_por_año(lista_r)
    #test_contador_por_año_defaultdict(lista_r)
    #test_contador_por_año_counter(lista_r)
    #test_año_con_mas_avistamientos(lista_r)
    #test_año_con_mas_avistamientos_counter(lista_r)
    #test_año_con_mas_avistamientos_forma_counter(lista_r)