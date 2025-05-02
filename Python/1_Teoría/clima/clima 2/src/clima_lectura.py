import csv
from typing import NamedTuple
from datetime import datetime

RegistroClima = NamedTuple("RegistroClima", [("fecha", datetime),
("lluvia", float), ("temp_max", float), ("temp_min",float)])

def leer_clima(fichero:str)->list[RegistroClima]:
    lista_registros=[]
    with open(fichero) as f:
        lector=csv.reader(f)
        next(lector) #solo si el fichero tiene una primera línea distinta

        for fecha_cadena, lluvia, tmax, tmin in lector:
        #for tupla in lector        (esto seria si queremos los datos empaquetados)

            #convertir las cadenas de caracteres en datos con su tipo
            fecha=datetime.strptime(fecha_cadena,"%Y-%m-%d").date()     #(strptime transforma un str a un formato time para que lo pueda leer el datetime)

            #si la lectura se hubiera hecho sin desempaquetar aquí pondriamos:
            #fecha=datetime.strptime(tupla[0],"%Y-%m-%d").date()
            lluvia=float(lluvia)
            tmax=float(tmax)
            tmin=float(tmin)
            r=RegistroClima(fecha,lluvia,tmax,tmin)
            lista_registros.append(r)

    return lista_registros