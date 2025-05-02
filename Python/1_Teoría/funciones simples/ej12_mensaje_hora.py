'''Defina una función que devuelva un mensaje de “buenos días”, “buenas tardes” o
“buenas noches” en función de la hora del sistema. Para determinar la hora del
sistema use la sentencia hora=datetime.datetime.now().time().hour'''


import datetime

def mensaje(hora:int)-> str:
    hora=datetime.datetime.now().time().hour
    if hora>6 and hora<12:
        saludo="buenos días"
    elif hora>=12 and hora<20:
        saludo="buenas tardes"
    else:
        saludo="buenas noches"
    return saludo

#print(mensaje(datetime.datetime.now().time().hour))