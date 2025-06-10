from consumo_electrico import *

def test_lee_facturas():
    print(len(lista_r))

def test_extrae_precio_por_mes():
    tipo_tarifa = "única"
    res = extrae_precio_por_mes(lista_r, tipo_tarifa)
    for cv in res.items():
        print(cv)

def test_busca_vivienda_mayor_consumo_acumulado():
    res = busca_vivienda_mayor_consumo_acumulado(lista_r)
    print(res)

def test_barrios_mayor_consumo_valle_medio():
    top_n = 3
    res = barrios_mayor_consumo_valle_medio(lista_r, top_n)
    print(res)

def test_compara_importe_tipos_factura():
    id_vivienda = "005"
    res = compara_importe_tipos_factura(lista_r, id_vivienda)
    print(res)

def test_busca_cambios_beneficiosos():
    res = busca_cambios_beneficiosos(lista_r)
    print(res)


if __name__=="__main__":
    ruta = "C:/Users/rodri/Desktop/US_Code/Python/PrimeraConvo/23_24/Consumo/data/consumo.csv"
    lista_r = lee_facturas(ruta)
    #test_lee_facturas()
    #test_extrae_precio_por_mes()
    #test_busca_vivienda_mayor_consumo_acumulado()
    #test_barrios_mayor_consumo_valle_medio()
    #test_compara_importe_tipos_factura()
    test_busca_cambios_beneficiosos()