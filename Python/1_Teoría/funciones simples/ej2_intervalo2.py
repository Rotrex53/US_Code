'''Defina una función tal que dados tres valores devuelva cierto si el primer valor está
fuera del intervalo cerrado definido por los otros dos. Haga dos versiones una desde
cero y la segunda reusando la función del primer ejercicio.'''


def esta_en_intervalo(valor:float, extremo_izq:float, extremo_der:float)-> bool:
    return valor >= extremo_izq and valor <= extremo_der
#también así return extremo_izq<= valor <= extremo_der

#segunda versión reutilizando la función esta_en_intervalo
def no_esta_en_intervalo2(valor:float, extremo_izq:float,extremo_der:float)-> bool:
    return not esta_en_intervalo(valor, extremo_izq,extremo_der )