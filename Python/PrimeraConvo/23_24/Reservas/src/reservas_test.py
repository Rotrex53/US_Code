from reservas import *

def test_lee_reservas():
    print(f"Total reservas: {len(lista_r)}")

def test_total_facturado():
    fecha_inicio = None
    fecha_final = None
    res = total_facturado(lista_r, fecha_inicio, fecha_final)
    if fecha_final!=None and fecha_inicio!=None:
        print(f"Desde {fecha_inicio.day} de {fecha_inicio.month} de {fecha_inicio.year} hasta " +
              f"{fecha_final.day} de {fecha_final.month} de {fecha_final.year}: {res}")
    if fecha_inicio==None and fecha_final!=None:
        print(f"Hasta {fecha_final.day} de {fecha_final.month} de {fecha_final.year} (fecha inicio None): {res}")
    if fecha_final==None and fecha_inicio!=None:
        print(f"Desde {fecha_inicio.day} de {fecha_inicio.month} de {fecha_inicio.year} (fecha final None): {res}")
    if fecha_final==None and fecha_inicio==None:
        print(f"En todo el periodo de datos: {res}")


def test_reservas_mas_largas():
    n = 3
    res = reservas_mas_largas(lista_r, n)
    print(f"Con n={n}: {res}")


def test_cliente_mayor_facturacion():
    servicios = {"Parking"}
    res = cliente_mayor_facturacion(lista_r, servicios)
    if servicios==None:
        print(f"Sin filtrar por servicios: {res}")
    else:
        print(f"Con {servicios}: {res}")

def test_servicios_estrella_por_mes():
    tipo_habitacion = None
    res = servicios_estrella_por_mes(lista_r, tipo_habitacion)
    print(f"Para {tipo_habitacion}:")
    for cv in res.items():
        print(cv)

def test_media_dias_entre_reservas():
    res = media_dias_entre_reservas(lista_r)
    print(res)

def test_cliente_reservas_mas_seguidas():
    min_reservas = 5
    res = cliente_reservas_mas_seguidas(lista_r, min_reservas)
    print(res)



if __name__=="__main__":
    ruta = "C:/Users/rodri/Desktop/US_Code/Python/PrimeraConvo/23_24/Reservas/data/reservas.csv"
    lista_r = lee_reservas(ruta)
    #test_lee_reservas()
    #test_total_facturado()
    #test_reservas_mas_largas()
    #test_cliente_mayor_facturacion()
    #test_servicios_estrella_por_mes()
    #test_media_dias_entre_reservas()
    #test_cliente_reservas_mas_seguidas()
