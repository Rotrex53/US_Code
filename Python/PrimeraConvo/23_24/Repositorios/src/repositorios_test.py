from repositorios import *

def test_lee_repositorios():
    print(len(lista_r))

def test_total_commits_por_anyo():
    res = total_commits_por_anyo(lista_r)
    print(res)

def test_n_mejores_repos_por_tasa_crecimiento():
    res = n_mejores_repos_por_tasa_crecimiento(lista_r)
    print(res)

def test_recomendar_lenguajes():
    repo = lista_r[4]
    res = recomendar_lenguajes(lista_r, repo)
    print(res)

def test_media_minutos_entre_commits_por_usuario():
    res = media_minutos_entre_commits_por_usuario(lista_r)
    print(res)







if __name__=="__main__":
    ruta = "C:/Users/rodri/Desktop/US_Code/Python/PrimeraConvo/23_24/Repositorios/data/repositorios.csv"
    lista_r = lee_repositorios(ruta)
    #test_lee_repositorios()
    #test_total_commits_por_anyo()
    #test_n_mejores_repos_por_tasa_crecimiento()
    #test_recomendar_lenguajes()
    test_media_minutos_entre_commits_por_usuario()