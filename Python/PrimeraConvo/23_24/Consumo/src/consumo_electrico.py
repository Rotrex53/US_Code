from typing import NamedTuple, List, Dict, Tuple, Counter, Optional
from datetime import date,datetime
import csv
from collections import defaultdict
 
IntervaloFechas = NamedTuple("IntervaloFechas",  
                     [("inicio", date), ("fin", date)]) 
 
Factura = NamedTuple("Factura",  
                     [("id_vivienda", str), 
                      ("tipo_vivienda", str), 
                      ("barrio", str), 
                      ("tipo_tarifa", str), 
                      ("periodo_facturado", IntervaloFechas), 
                      ("coste_potencia", float), 
                      ("consumo_punta", float), 
                      ("consumo_valle", float), 
                      ("precio_punta", float), 
                      ("precio_valle", float), 
                      ("importe_total", float)])


def lee_facturas(ruta_fichero: str) -> List[Factura]:
    with open(ruta_fichero, encoding="UTF-8") as f:
        lista = []
        lector = csv.reader(f)
        next(lector)
        for id_vivienda, tipo_vivienda, barrio, tipo_tarifa, periodo_inicio, \
        periodo_fin, coste_potencia_eur, consumo_punta_kwh, consumo_valle_khw, precio_kwh, importa_total_eur in lector:
            periodo_inicio = datetime.strptime(periodo_inicio, "%Y-%m-%d").date()
            periodo_fin = datetime.strptime(periodo_fin, "%Y-%m-%d").date()
            coste_potencia_eur = float(coste_potencia_eur)
            consumo_punta_kwh = float(consumo_punta_kwh)
            consumo_valle_khw = float(consumo_valle_khw)
            precio_kwh = parsea_precio_kwh(precio_kwh)
            importa_total_eur = float(importa_total_eur)
            if tipo_tarifa.lower()=="tramos":
                lista.append(Factura(id_vivienda, tipo_vivienda, barrio, tipo_tarifa, IntervaloFechas(periodo_inicio, periodo_fin), \
                                 coste_potencia_eur, consumo_punta_kwh, consumo_valle_khw, float(precio_kwh[0]), float(precio_kwh[1]), importa_total_eur))
            else:
                lista.append(Factura(id_vivienda, tipo_vivienda, barrio, tipo_tarifa, IntervaloFechas(periodo_inicio, periodo_fin), \
                                 coste_potencia_eur, consumo_punta_kwh, consumo_valle_khw, float(precio_kwh[0]), precio_kwh, importa_total_eur))
    return lista
        
def parsea_precio_kwh(precio_kwh_str:str) -> List[float]:
    precio_kwh = precio_kwh_str.split("/")
    lista = []
    for parte in precio_kwh:
        lista.append(parte)
    return lista
    

def extrae_precio_por_mes(facturas: List[Factura], tipo_tarifa: str) -> Dict[str, Tuple[float, float]]:
    precio_kwh_por_año_mes = defaultdict(list)
    for factura in facturas:
        if factura.tipo_tarifa == tipo_tarifa:
            año_mes = datetime.strftime(factura.periodo_facturado.inicio, "%Y-%m")
            precio_kwh_por_año_mes[año_mes]=(factura.precio_punta, factura.precio_valle)

    return precio_kwh_por_año_mes


def busca_vivienda_mayor_consumo_acumulado(facturas: List[Factura]) -> Tuple[str, float]:
    tupla_res = ()
    consumo_acum_por_id = defaultdict(float)
    for factura in facturas:
        consumo_acum = factura.consumo_punta + factura.consumo_valle
        consumo_acum_por_id[factura.id_vivienda]+=consumo_acum
    tupla_res = max(consumo_acum_por_id.items(), key=lambda x:x[1])
    return tupla_res


def barrios_mayor_consumo_valle_medio(facturas: List[Factura], top_n: int) -> List[str]:
    consumo_valle_por_barrio = defaultdict(list)
    consumo_medio_por_barrio = defaultdict(float)
    lista_res = []
    for factura in facturas:
        consumo_valle_por_barrio[factura.barrio].append(factura.consumo_valle)
    
    for barrio, lista_consumos_valle in consumo_valle_por_barrio.items():
        consumo_medio_valle = sum(lista_consumos_valle)/len(lista_consumos_valle)
        consumo_medio_por_barrio[barrio]=consumo_medio_valle
    
    lista_res = sorted(consumo_medio_por_barrio.keys(), reverse=True)
    return lista_res[:top_n]


def compara_importe_tipos_factura(facturas: List[Factura], id_vivienda: str) -> Optional[Tuple[str, float, float]] | None:
    tupla_res = ()
    supuesto_facturado = 0.
    importe_total = 0.
    for factura in facturas:
        if factura.id_vivienda==id_vivienda:
            if factura.tipo_tarifa=="tramos":
                str_cambio_tarifa = f"{factura.tipo_tarifa} -> única"
                supuesto_facturado += factura.precio_punta*(factura.consumo_punta + factura.consumo_valle) + factura.coste_potencia
                importe_total += factura.importe_total
                tupla_res = (str_cambio_tarifa, importe_total, supuesto_facturado)

            else:
                str_cambio_tarifa = f"{factura.tipo_tarifa} -> tramos"
                supuesto_facturado += ((factura.consumo_punta+factura.consumo_valle)*factura.precio_punta) + factura.coste_potencia
                importe_total += factura.importe_total
                tupla_res = (str_cambio_tarifa, importe_total, supuesto_facturado)
    
    if tupla_res!=():
        return tupla_res
    else:
        return None
    

def busca_cambios_beneficiosos(facturas: List[Factura]) -> List[Tuple[str, int, float]]:
    id_viviendas = set(factura.id_vivienda for factura in facturas)
    id_viviendas = sorted(list(id_viviendas))
    total_ahorro_por_tarifa = defaultdict(float)
    total_cambios_por_tarifa = Counter()
    lista_res = []

    for id in id_viviendas:
        str_cambio_tarifa, total_actual, total_supuesto = compara_importe_tipos_factura(facturas, id)
        if total_supuesto<total_actual:
            total_ahorro = total_actual-total_supuesto
            total_ahorro_por_tarifa[str_cambio_tarifa]+=total_ahorro
            total_cambios_por_tarifa[str_cambio_tarifa]+=1
        
    for str_cambio_tarifa in total_cambios_por_tarifa:
        lista_res.append((str_cambio_tarifa, total_cambios_por_tarifa[str_cambio_tarifa], total_ahorro_por_tarifa[str_cambio_tarifa]))

    return lista_res