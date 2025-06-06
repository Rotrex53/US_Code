from motoFP import *

def test_lee_carreras():
    print(f"Número de carreras leídas: {len(lista_r)}")
    print(f"\nLas dos primeras son: \n {lista_r[0]}\n {lista_r[1]}")
    print(f"\nLas dos últimas son: \n {lista_r[-2]} \n {lista_r[-1]}")


def test_maximo_dias_sin_ganar():
    nombre_piloto = "Marc Marquez"
    res = maximo_dias_sin_ganar(lista_r, nombre_piloto)
    print(f"Test maximo_dias_sin_ganar")
    print(f"Para {nombre_piloto}: {res}")
    
def test_piloto_mas_podios_por_circuito():
    res = piloto_mas_podios_por_circuito(lista_r)
    print(f"Test piloto_mas_podios_por_circuito\n")
    for claveValor in res.items():
        print(claveValor)

def test_escuderias_con_solo_un_piloto():
    res = escuderias_con_solo_un_piloto(lista_r)
    print(f"Test escuderias_con_solo_un_piloto\n{res}")

def test_piloto_racha_mas_larga_victorias_consecutivas():
    anyo = 2024
    res = piloto_racha_mas_larga_victorias_consecutivas(lista_r, anyo)
    print(f"Test piloto_racha_mas_larga_victorias_consecutivas\n Para año={anyo} {res}")

def test_ultimos_ganadores_por_circuito():
    n = 2
    estado = "Seco"
    res = ultimos_ganadores_por_circuito(lista_r, n, estado)
    print(f"Test ultimos_ganadores_por_circuito\n Para n={n} y estado={estado}\n")
    for claveValor in res.items():
        print(claveValor)




if __name__=="__main__":
    ruta = "C:/Users/rodri/Desktop/US_Code/Python/PrimeraConvo/24_25/MotoFP/data/motoFP.csv"
    lista_r = lee_carreras(ruta)
    #test_lee_carreras()
    #test_maximo_dias_sin_ganar()
    #test_piloto_mas_podios_por_circuito()
    #test_escuderias_con_solo_un_piloto()
    #test_piloto_racha_mas_larga_victorias_consecutivas()
    test_ultimos_ganadores_por_circuito()