from poblacion import *

def test_lee_poblaciones(lista_r):
    print(f"La cantidad de registros leidos han sido: {len(lista_r)}")
    print(f"mostrar primero {lista_r[0]}")

def test_calcula_paises(lista_r):
    lista_total_paises=calcula_paises(lista_r)
    lista_total_paises.sort()
    print(f"Los países son: {lista_total_paises}")

def test_filtra_por_pais(lista_r):
    nombre_o_codigo_elegido="ARB"
    lista_filtrada_nombre_o_codigo=filtra_por_pais(lista_registro=lista_r, nombre_o_codigo=nombre_o_codigo_elegido)
    print(f"Los datos del país filtrado con nombre o código {nombre_o_codigo_elegido} son: {lista_filtrada_nombre_o_codigo}")

def test_filtra_por_paises_y_año(lista_r):
    año_elegido=2000
    nombres_paises={"France","Congo","Namibia"}
    lista_filtra_por_paises_y_año=filtra_por_paises_y_año(lista_r, año=año_elegido, lista_varios_paises=nombres_paises)
    print(f"La lista filtrada según el año {año_elegido} y los nombres de paises {nombres_paises} es: {lista_filtra_por_paises_y_año}")

def test_muestra_evolucion_poblacion(lista_r):
    nombre_o_codigo_elegido="Spain"
    lista_años, lista_habitantes=muestra_evolucion_poblacion(lista_registro=lista_r, nombre_o_codigo=nombre_o_codigo_elegido)
    plt.title("Gráfica")
    plt.plot(lista_años, lista_habitantes)
    plt.xlabel("Año")
    plt.ylabel("Población")
    plt.grid(True)
    plt.show()

def test_muestra_comparativa_paises_año(lista_r):
    año_elegido=1990
    conjunto_paises={"Spain","Germany","France"}
    lista_paises, lista_habitantes=muestra_comparativa_paises_año(lista_registro=lista_r, año=año_elegido, lista_varios_paises=conjunto_paises)
    plt.title(f"Gráfica en el {año_elegido}")
    plt.bar(lista_paises, lista_habitantes)
    plt.xlabel("Paises")
    plt.ylabel("Población")
    plt.grid(False)
    plt.show()



def funcion_principal():
    lista_r=lee_poblaciones("./VSCode FP/Python/laboratorio/clase4_(17-10)/data/population.csv")
    #test_lee_poblaciones(lista_r)
    #test_calcula_paises(lista_r)
    #test_filtra_por_pais(lista_r)
    #test_filtra_por_paises_y_año(lista_r)
    #test_muestra_evolucion_poblacion(lista_r)
    test_muestra_comparativa_paises_año(lista_r)


    



if __name__=="__main__":
    funcion_principal()