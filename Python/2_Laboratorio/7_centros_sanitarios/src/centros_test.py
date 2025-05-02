from centros import *

def test_leer_archivo(lista_r):
    print(f"se han leido un total de {len(lista_r)} lineas del csv")

def test_calcular_total_camas_centros_accesibles():
    resultado = calcular_total_camas_centros_accesibles(lista_r)
    print(f"el total de camas accesibles para discapacitados es: {resultado}")




if __name__=="__main__":
    lista_r = leer_centros("C:/Users/rodri/OneDrive/Desktop/US_proyects/Python/2_Laboratorio/7_centros_sanitarios/data/centrosSanitarios.csv")
    #test_leer_archivo(lista_r)
    test_calcular_total_camas_centros_accesibles()
