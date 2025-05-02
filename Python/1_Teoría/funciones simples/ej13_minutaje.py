'''Defina una función que devuelva el número de minutos transcurridos desde el
comienzo del día. Use las funciones hour y minute igual que en el ejercicio anterior.'''

import datetime

def minutos_transcurridos()->int:
    horas=datetime.datetime.now().time().hour
    minutos=datetime.datetime.now().time().minute
    resultado=60*horas+minutos
    return resultado

'''
hora=datetime.datetime.now().time().hour
minutos=datetime.datetime.now().time().minute
resultado=60*hora+minutos

print(resultado)
'''