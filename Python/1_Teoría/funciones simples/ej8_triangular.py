'''A partir de esa función definimos una función denominada triangular tal que dados
dos números enteros m y n se define como el cociente entre el valor absoluto de n y el
producto de los valores absolutos de n-m y m. Por ejemplo, si n=-3 y m=2 triangular de
n y m es 3/(2x5)=0,3, si n=5 y m=-2, entonces triangular(n,m) es igual a 5/(2x7)=5/14.'''

from ej7_valor_absoluto import valor_absoluto
import math

#h=int(input("v1: \n"))
#m=int(input("v2: \n"))
def triangular(h:int, m:int)->float:
    return valor_absoluto(h)/(valor_absoluto(h-m)*valor_absoluto(m))
    #entre el valor absoluto de n
    #y el producto de los valores de n-m y m

    #Se invoca un Print para comprobar con un ejemplo si funciona
#print(triangular(h,m))
