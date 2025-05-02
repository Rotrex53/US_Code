from entrenos import *

def test_leer_entrenos():
    lista_r=leer_entreno("./VSCode FP/Python/laboratorio/clase3_(10-10)/data/entrenos.csv")
    print(f"El numero de entrenamientos fue: {len(lista_r)}")
    print(f"el primer entrenamiento fue: {lista_r[0]}")
    print(f"el segundo entrenamiento fue: {lista_r[1]}")
    print(f"el tercero entrenamiento fue: {lista_r[2]}")
    print(f"el ultimo entrenamiento fue: {lista_r[-1]}")
    print(f"el penultimo entrenamiento fue: {lista_r[-2]}")
    print(f"el antepenultimo entrenamiento fue: {lista_r[-3]}")

def test_tipos_entreno():
    lista_r=leer_entreno("./VSCode FP/Python/laboratorio/clase3_(10-10)/data/entrenos.csv")
    lista_tipos_entrenos=tipos_entreno(lista_r)
    lista_tipos_entrenos.sort()
    print(f"los entrenamientos son: {lista_tipos_entrenos}")

def test_entrenos_duracion_superior():
    d=50
    lista_r=leer_entreno("./VSCode FP/Python/laboratorio/clase3_(10-10)/data/entrenos.csv")
    lista_duracion_superior=entrenos_duracion_superior(lista_r, d)
    print(f"Las duraciones superiores a {d} son: {lista_duracion_superior}")

def test_suma_calorias():
    lista_r=leer_entreno("./VSCode FP/Python/laboratorio/clase3_(10-10)/data/entrenos.csv")
    fecha_inicial="27/2/2019 5:04"
    fecha_final="7/12/2021 10:08"
    total_calorias=suma_calorias(lista_r, f_inicio=fecha_inicial, f_fin=fecha_final)
    print(f"La suma de calorias entre {fecha_inicial} y {fecha_final} es: {total_calorias}")


def funcion_principal():
    #test_leer_entrenos()
    #test_tipos_entreno()
    #test_entrenos_duracion_superior()
    test_suma_calorias()

if __name__=="__main__":
    funcion_principal()