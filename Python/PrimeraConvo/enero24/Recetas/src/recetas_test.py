from recetas import *

def test_leer_recetas():
    print(f"Recetas leídas: {len(lista_r)} \n")
    print(f"Mostrando las 2 primeras recetas: \n {lista_r[0]} \n {lista_r[1]} \n")
    print(f"Mostrando las 2 últimas recetas: \n {lista_r[-2]} \n {lista_r[-1]} \n")
    
def test_receta_mas_barata():
    res = receta_mas_barata(lista_r, ('Plato principal'), 5)
    print(res)

def test_obten_ingredientes():
    res = obten_ingredientes(lista_r, 2, None)
    print(len(res))

def test_recetas_con_precio_menor_promedio():
    res = recetas_con_precio_menor_promedio(lista_r, 5)
    print(res)

def test_receta_mas_ingredientes():
    res = receta_mas_ingredientes(lista_r, None)
    print(res)

def test_ingredientes_mas_comunes_por_tipo():
    res = ingredientes_mas_comunes_por_tipo(lista_r)
    print(res)

def test_mes_con_precio_medio_mas_alto():
    res = mes_con_precio_medio_mas_alto(lista_r, 5)
    print(res)

if __name__ == "__main__":
    lista_r = leer_recetas("C:/Users/rodri/Desktop/US_Code/Python/PrimeraConvo/enero24/Recetas/data/recetas.csv")
    #test_leer_recetas()
    #test_receta_mas_barata()
    #test_obten_ingredientes()
    #test_recetas_con_precio_menor_promedio()
    #test_receta_mas_ingredientes()
    #test_ingredientes_mas_comunes_por_tipo()
    test_mes_con_precio_medio_mas_alto()