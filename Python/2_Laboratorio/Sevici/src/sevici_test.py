from sevici import *

def test_leer_estaciones(lista_r):
    print(f"hay {len(lista_r)} registros")
    print(f"El primer registro es {lista_r[0]}")
    print(f"El segundo registro es {lista_r[1]}")
    print(f"El tercer registro es {lista_r[2]}")
    print(f"El ultimo registro es {lista_r[-1]}")
    print(f"El penúltimo registro es {lista_r[-2]}")
    print(f"El antepenúltimo registro es {lista_r[-3]}")





if __name__ == "__main__":
    lista_r = leer_estaciones("./Python/Sevici/data/estaciones.csv")
    test_leer_estaciones(lista_r)