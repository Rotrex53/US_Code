from typing import NamedTuple,List,Set,Tuple,Dict,Optional 
from datetime import datetime,date 
import csv
from collections import defaultdict, Counter

Commit = NamedTuple("Commit",      
       [("id", str), # Identificador alfanumérico del commit 
        ("mensaje", str), # Mensaje asociado al commit 
        ("fecha_hora", datetime) # Fecha y hora en la que se registró el commit 
       ]) 
Repositorio = NamedTuple("Repositorio",      
      [("nombre", str),  # Nombre del repositorio 
       ("propietario", str), # Nombre del usuario propietario 
       ("lenguajes", Set[str]),  # Conjunto de lenguajes usados 
       ("privado", bool),  # Indica si es privado o público 
       ("commits", List[Commit])  # Lista de commits realizados 
       ])


def lee_repositorios(csv_filename: str) -> List[Repositorio]:
    with open(csv_filename, encoding="UTF-8") as f:
        lista = []
        lector = csv.reader(f)
        next(lector)
        for nombre, propietario, lenguajes, privado, commits in lector:
            lenguajes = parsea_lenguajes(lenguajes)
            privado = parsea_privado(privado)
            commits = parsea_commits(commits)
            lista.append(Repositorio(nombre, propietario, lenguajes, privado, commits))
    return lista

def parsea_lenguajes(lenguajes_str: str) -> Set[str]:
    set_res = set()
    lenguajes = lenguajes_str.split(",")
    for leng in lenguajes:
        set_res.add(leng)
    return set_res

def parsea_privado(privado_str: str) -> bool:
    if privado_str.lower()=="true":
        return True
    else:
        return False

def parsea_commits(commits_str: str) -> List[Commit]:
    lista_res = []
    commits_str = commits_str.replace("[", "").replace("]", "")
    commits = commits_str.split(";")
    if commits_str == "":
        return lista_res
    for commit_str in commits:
        parte_commit = commit_str.split("#")
        id = parte_commit[0]
        mensaje = parte_commit[1]
        fecha_hora = datetime.strptime(parte_commit[2], "%Y-%m-%d %H:%M:%S")
        lista_res.append(Commit(id, mensaje, fecha_hora))
    return lista_res


def total_commits_por_anyo(repositorios:List[Repositorio])->Dict[int, int]:
    commits_por_año =  defaultdict(int)
    for repo in repositorios:
        if repo.privado==False:
            for commit in repo.commits:
                anyo = commit.fecha_hora.year
                commits_por_año[anyo] += 1
  
    return commits_por_año


def n_mejores_repos_por_tasa_crecimiento(repositorios: List[Repositorio],  
                                        n:Optional[int]=3)->List[Tuple[str,float]]:
    lista_res = []
    nombres_por_tasa = defaultdict(list)
    for repo in repositorios:
        nombres_por_tasa[repo.nombre].append(calcular_tasa_crecimiento(repo))
    
    for nombre, lista_tasas in nombres_por_tasa.items():
        lista_res.append((nombre, max(lista_tasas)))
    return sorted(lista_res, key=lambda x:x[1], reverse=True)[:n]

def calcular_tasa_crecimiento(repositorio: Repositorio) -> float:
    tasa_crecimiento = 0.
    if len(repositorio.commits)<2 or (len(repositorio.commits)>=2 and dif_fechas(repositorio)==0):
        return tasa_crecimiento
    else:
        return float(len(repositorio.commits)/dif_fechas(repositorio))

def dif_fechas(respositorio: Repositorio) -> int:
    lista = respositorio.commits
    if lista[0].fecha_hora.year == lista[-1].fecha_hora.year:
        return 0
    else:
        return (lista[-1].fecha_hora - lista[0].fecha_hora).days
    

def recomendar_lenguajes (repositorios:List[Repositorio],  
                          repositorio:Repositorio)->Set[str]:
    set_res = set()
    lenguajes_por_repositorio = defaultdict(list)
    for repo in repositorios:
        for leng in repo.lenguajes:
            lenguajes_por_repositorio[repo.nombre].append(leng)

    lenguajes_repo_propuesto = repositorio.lenguajes
    for _, list_lenguajes in lenguajes_por_repositorio.items():
        chivato = False
        for lenguaje in lenguajes_repo_propuesto:
            if lenguaje in list_lenguajes:
                list_lenguajes.remove(lenguaje)
                chivato = True
        if list_lenguajes!=[] and chivato == True:
           for leng in list_lenguajes: 
            set_res.add(leng)
    
    return set_res


def media_minutos_entre_commits_por_usuario (repositorios:List[Repositorio],  
                         fecha_ini:Optional[date]=None, 
                         fecha_fin:Optional[date]=None)->Dict[str, float]:
    dicc_res = defaultdict(float)

    
    for repo in repositorios:
            fecha_repo = (commit.fecha_hora.date() for commit in repo.commits)
            if (fecha_ini==None or fecha_ini<=fecha_repo) and (fecha_fin==None or fecha_repo<fecha_fin):
                if media_minutos_entre_commits(repo.commits)!=None:
                    dicc_res[repo.propietario]+=abs(media_minutos_entre_commits(repo.commits))
    
    return dicc_res


def media_minutos_entre_commits(lista_commits: List[Commit]) -> float | None:
    media_minutos = 0.
    lista_acum = []
    if len(lista_commits)<2:
        return None
    
    lista_commits = sorted(lista_commits, key=lambda x:x.fecha_hora, reverse=True)
    for c1, c2 in zip(lista_commits, lista_commits[1:]):
        dif_min = (c2.fecha_hora - c1.fecha_hora).total_seconds()/60
        lista_acum.append(dif_min)
    media_minutos = sum(lista_acum)/len(lista_acum)
    
    return media_minutos
