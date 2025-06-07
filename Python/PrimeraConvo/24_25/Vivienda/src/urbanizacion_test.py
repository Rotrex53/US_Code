from urbanizacion import *

def test_lee_viviendas():
    res = lee_viviendas(ruta)
    print(f"Número de registros leídos: {len(res)}")
    print(f"Las dos primeras: {res[0]}{res[1]}")
    print(f"Las dos últimas: {res[-2]}{res[-1]}")

def test_total_mejoras_por_calle():
    par_impar = "par"
    res = total_mejoras_por_calle(lista_r, par_impar)
    print(f"Número de mejoras en viviendas: {par_impar}")
    for calle, num_mejoras in res.items():
        print(f"{calle} --> {num_mejoras}")

def test_vivienda_con_mejora_mas_rapida():
    res = vivienda_con_mejora_mas_rapida(lista_r)
    print(f"La vivienda que hizo una mejora en menos tiempo es {res}")
        
def test_calle_mayor_diferencia_precios():
    res = calle_mayor_diferencia_precios(lista_r)
    print(f"La calle es: {res}")

def test_n_viviendas_top_valoradas_por_calle():
    fecha = datetime.strptime("2020-01-01", "%Y-%m-%d").date()
    n = 4
    res = n_viviendas_top_valoradas_por_calle(lista_r, fecha, n)
    print(f"Para n={n} y fecha={fecha} son: ")
    for clave, valor in res.items():
        print(f"{clave} --> {valor}")

def test_valor_metro_cuadrado_por_calle_y_año():
    res = valor_metro_cuadrado_por_calle_y_año(lista_r)
    for tupla in res:
        print(tupla)






if __name__=="__main__":
    ruta="C:/Users/rodri/Desktop/US_Code/Python/PrimeraConvo/24_25/Vivienda/data/urbanizacion.csv"
    lista_r = lee_viviendas(ruta)
    #test_lee_viviendas()
    #test_total_mejoras_por_calle()
    #test_vivienda_con_mejora_mas_rapida()
    #test_calle_mayor_diferencia_precios()
    #test_n_viviendas_top_valoradas_por_calle()
    test_valor_metro_cuadrado_por_calle_y_año()