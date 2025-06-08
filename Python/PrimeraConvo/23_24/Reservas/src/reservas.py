from typing import NamedTuple, List, Optional, Tuple, Set, Dict
from datetime import date,datetime
import csv
from collections import defaultdict, Counter

Reserva = NamedTuple("Reserva",  
                     [("nombre", str), 
                      ("dni", str), 
                      ("fecha_entrada", date), 
                      ("fecha_salida", date), 
                      ("tipo_habitacion", str), 
                      ("num_personas", int), 
                      ("precio_noche", float), 
                      ("servicios_adicionales", List[str]) 
                    ])

def lee_reservas(ruta_fichero: str) -> List[Reserva]:
    with open(ruta_fichero, encoding="UTF-8") as f:
        lista=[]
        lector = csv.reader(f)
        next(lector)
        for nombre,dni,fecha_entrada,fecha_salida,tipo_habitacion,num_personas,precio_noche,servicios_adicionales in lector:
            fecha_entrada=datetime.strptime(fecha_entrada, "%Y-%m-%d").date()
            fecha_salida=datetime.strptime(fecha_salida, "%Y-%m-%d").date()
            num_personas=int(num_personas)
            precio_noche=float(precio_noche)
            servicios_adicionales=parsea_servicios(servicios_adicionales)
            lista.append(Reserva(nombre,dni,fecha_entrada,fecha_salida,tipo_habitacion,num_personas,precio_noche,servicios_adicionales))
    return lista

def parsea_servicios(servicios_str:str)-> list[str]:
    res = []
    servicios = servicios_str.split(",")
    for servicio in servicios:
        res.append(servicio)
    return res


def total_facturado(reservas: List[Reserva],  
             fecha_ini: Optional[date] = None,  
             fecha_fin: Optional[date] = None) -> float:
    res = 0.
    for reserva in reservas:
        if (fecha_ini==None or reserva.fecha_entrada>=fecha_ini) and (fecha_fin==None or reserva.fecha_entrada<=fecha_fin):      #a lo mejor el ==None va antes
            res+=reserva.precio_noche*(reserva.fecha_salida-reserva.fecha_entrada).days
    return res


def reservas_mas_largas(reservas:List[Reserva],n:int = 3) -> List[Tuple[str, date]]:
    diccAux = {}
    for reserva in reservas:
        duracionReserva = (reserva.fecha_salida-reserva.fecha_entrada).days
        if duracionReserva not in diccAux:
            diccAux[duracionReserva] = []
        diccAux[duracionReserva].append((reserva.nombre, reserva.fecha_entrada))

    listaOrdenada = sorted(diccAux.items(), key=lambda x:x[0], reverse=True)[:n]
    resultado = []
    for item in listaOrdenada:
        resultado.append(item[1])
    return resultado


def cliente_mayor_facturacion(reservas: List[Reserva],  
                        servicios: Optional[Set[str]] = None 
                        ) -> Tuple[str, float]:
    diccAux = {}
    if servicios==None:
        reservas_filtradas = reservas
    else:
        reservas_filtradas = (reserva for reserva in reservas if any(serv in servicios for serv in reserva.servicios_adicionales))
    for reserva in reservas_filtradas:
        if reserva.dni not in diccAux:
            diccAux[reserva.dni] = 0.
        valorFacturacion = reserva.precio_noche*(reserva.fecha_salida-reserva.fecha_entrada).days
        diccAux[reserva.dni] = diccAux.get(reserva.dni, 0.0) + valorFacturacion

    return max(diccAux.items(), key=lambda x:x[1])


def servicios_estrella_por_mes(reservas: List[Reserva],  
                     tipos_habitacion: Optional[Set[str]] = None) -> Dict[str, str]:
    servicios_por_mes = defaultdict(list)
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
            "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    for reserva in reservas:
        if tipos_habitacion==None or reserva.tipo_habitacion in tipos_habitacion:
            nombre_mes = meses[reserva.fecha_entrada.month-1]
            servicios_por_mes[nombre_mes] += reserva.servicios_adicionales
            
    res = {}
    for mes, servicios in servicios_por_mes.items():
        res[mes] = Counter(servicios).most_common(1)[0][0]
    return res


def media_dias_entre_reservas(reservas: List[Reserva]) -> float:
    dias = []
    reservas_ordenadas = sorted(reservas, key=lambda x:x.fecha_entrada)
    for r1,r2 in zip(reservas_ordenadas, reservas_ordenadas[1:]):
        dias.append((r2.fecha_entrada - r1.fecha_entrada).days)
    return sum(dias)/len(dias)


def cliente_reservas_mas_seguidas(reservas: List[Reserva],  
                                    min_reservas: int 
                                    ) -> Tuple[str, float]:
    diccAux = defaultdict(list)
    for reserva in reservas:
        diccAux[reserva.dni].append(reserva)
    
    media_por_cliente=[]
    for dni, lista_reservas in diccAux.items():
        if len(lista_reservas)>=min_reservas:
            media=media_dias_entre_reservas(lista_reservas)
            media_por_cliente.append((dni, media))

    return min(media_por_cliente, key=lambda x:x[1])