from tenis import *

def test_leer_archivo(lista_r):
    print(f"el registro es: {lista_r}")

def test_ganador(lista_r):
    lista_ganadores=ganador(lista_r)
    print(f"ganadores: {lista_ganadores}")

def test_tenista_mas_victorias0(lista_r):
    fecha1_elegida=None
    fecha2_elegida=17/1/2016
    tenista_mas_victorias=tenista_mas_victorias0(lista_partidos=lista_r, fecha1=fecha1_elegida, fecha2=fecha2_elegida)
    print(f"el tenista mas victorioso entre las fechas: {fecha1_elegida,fecha2_elegida} es: {tenista_mas_victorias}")




if __name__ == "__main__":
    lista_r=leer_archivo('C:/Users/rodri/OneDrive/Desktop/US_proyects/Python/3_repaso_examen/Examen2/Tenis/data/tenis.csv')
    #test_leer_archivo(lista_r)
    #test_ganador(lista_r)
    test_tenista_mas_victorias0(lista_r)