from suscripciones import *

def test_lee_suscripciones():
    print(len(lista_r))

def test_suscripciones_mas_rentables():
    n = 3
    tipos_plan = {"Básico"}
    res = suscripciones_mas_rentables(lista_r, n, tipos_plan)
    print(res)

def test_plan_mas_perfiles():
    fecha_ini = None
    fecha_fin = None
    res = plan_mas_perfiles(lista_r, fecha_ini, fecha_fin)
    print(res)

def test_media_dias_por_plan():
    res = media_dias_por_plan(lista_r)
    print(res)

def test_addon_mas_popular_por_año():
    res = addon_mas_popular_por_año(lista_r)
    print(res)

def test_evolucion_años():
    res = evolucion_años(lista_r)
    print(res)




if __name__=="__main__":
    ruta = "C:/Users/rodri/Desktop/US_Code/Python/PrimeraConvo/24_25/Subscripciones/data/subscripciones.csv"
    lista_r = lee_suscripciones(ruta)
    #test_lee_suscripciones()
    #test_suscripciones_mas_rentables()
    #test_plan_mas_perfiles()
    #test_media_dias_por_plan()
    #test_addon_mas_popular_por_año()
    test_evolucion_años()