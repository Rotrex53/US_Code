from sevici import *

def test_leer_estaciones(lista_r):
    print(f"hay {len(lista_r)} registros")
    print(f"El primer registro es {lista_r[0]}")
    print(f"El segundo registro es {lista_r[1]}")
    print(f"El tercer registro es {lista_r[2]}")
    print(f"El ultimo registro es {lista_r[-1]}")
    print(f"El penúltimo registro es {lista_r[-2]}")
    print(f"El antepenúltimo registro es {lista_r[-3]}")

def test_estaciones_bicis_libres(lista_r):
    estadiones_libres = estaciones_bicis_libres(fichero=lista_r)
    print(f"Las 5 estaciones con más bicis libres son: {estadiones_libres}")

def test_calcula_distancia():
    coord1 = Coordenadas(10.433533, 8.124352)
    coord2 = Coordenadas(37.376367, -5.982352)
    resultado = calcula_distancia(coord1, coord2)
    print(f"La distancia entre {coord1} y {coord2} es {resultado}")

def test_estaciones_cercanas(lista_r):
    k_elegida = 5
    coordenadas_elegidas = Coordenadas(37.376367, -5.982352)
    estaciones_cercanas_resultado = estaciones_cercanas(fichero=lista_r, distancia=coordenadas_elegidas, k=k_elegida)
    print(f"Las {k_elegida} estaciones más cercanas a {coordenadas_elegidas} son: {estaciones_cercanas_resultado}")



if __name__ == "__main__":
    lista_r = leer_estaciones("./Python/Sevici/data/estaciones.csv")
    #test_leer_estaciones(lista_r)
    #test_estaciones_bicis_libres(lista_r)
    #test_calcula_distancia()
    test_estaciones_cercanas(lista_r)