from clima_lectura import *
from clima_funciones import *

def test_lectura():
    lista_r=leer_clima("./VSCode FP/Python/CSV/clima_clase/data/madrid.csv")
    print("numero registros leidos", len(lista_r))
    print("el primer registro es ", lista_r[0])

def test_filtra_entre_fechas():
    fec1=datetime(1985, 12, 20).date()
    fec2=datetime(1987, 10, 26).date()
    lista_r=leer_clima("./VSCode FP/Python/CSV/clima_clase/data/madrid.csv") #se llama asi por ser lista readed
    lista_f=filtra_entre_fechas(lista_r, fec1, fec2)                         #se llama asi por ser lista filtrada
    print("numero de registros leidos ", len(lista_f))
    print("el primer registro es ", lista_f[0])
    print("el ultimo registro es ", lista_f[-1])

def test_filtra_entre_fechas_cadenas():
    lista_r=leer_clima("./VSCode FP/Python/CSV/clima_clase/data/madrid.csv") 
    lista_f=filtra_entre_fechas_cadenas(lista_r, "20/12/1985", "26/10/1987")                         
    print("numero de registros leidos ", len(lista_f))
    print("el primer registro es ", lista_f[0])
    print("el ultimo registro es ", lista_f[-1])

def test_temperatura_minima():
    lista_r=leer_clima("./VSCode FP/Python/CSV/clima_clase/data/madrid.csv")
    resultado_mas_frio=filtra_dia_mas_frio(lista_r)
    print("el dia más frio fue ",resultado_mas_frio.fecha)

def test_dia_mas_lluvioso():
    lista_r=leer_clima("./VSCode FP/Python/CSV/clima_clase/data/madrid.csv")
    resultado_mas_lluvioso=filtra_dia_mas_lluvioso(lista_r)
    print("el dia más lluvioso fue ",resultado_mas_lluvioso.fecha)

def funcion_principal():
    #test_lectura()
    #test_filtra_entre_fechas()
    #test_filtra_entre_fechas_cadenas()
    #test_temperatura_minima()
    test_dia_mas_lluvioso()
    #test dia mas lluvioso() [por hacer]




if __name__=="__main__":
    funcion_principal()