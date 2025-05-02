'''Defina una función tal que dados tres valores devuelva cierto si el primero está
incluido en el intervalo cerrado definido por los otros dos.'''

valor=input("valor: \n")
extremo_izq=input("extr.izq: \n")
extremo_der=input("extr.der: \n")

def esta_en_intervalo(valor:float, extremo_izq:float, extremo_der:float)-> bool:
    if valor >= extremo_izq and valor <= extremo_der:
        return print("Si")
    else:
        return print("No")
#también así return extremo_izq<= valor <= extremo_der

def no_esta_en_intervalo(valor:float, extremo_izq:float, extremo_der:float)-> bool:
    if valor < extremo_izq or valor > extremo_der:
        return print("Si")
    else:
        return print("No")

print("esta__en_intervalo: ", esta_en_intervalo)
print("no_esta_en_intervalo: ", no_esta_en_intervalo)
#otra forma mas funcional
'''
valor=int(input("introduce: valor \n"))
extremo_izq=int(input("introduce: extremo izq\n"))
extremo_der=int(input("introduce: extremo der: \n"))
    
if valor >= extremo_izq and valor <= extremo_der:
    incluido_o_no=True

else:
    incluido_o_no=False

print(incluido_o_no) 
'''