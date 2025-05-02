from repaso_complemento import *



##################
print("algo")

##################
import datetime
hoy=datetime.datetime.now()
hoy_con_fecha_completa=datetime.datetime.now().date()
hoy_solo_dia_del_mes=datetime.datetime.now().date().day
hoy_solo_mes=datetime.datetime.now().date().month
hoy_solo_year=datetime.datetime.now().date().year
hoy_con_hora_completa=datetime.datetime.now().time()
hoy_solo_hora=datetime.datetime.now().time().hour
hoy_solo_minuto=datetime.datetime.now().time().minute
hoy_solo_segundos=datetime.datetime.now().time().second

print(hoy,"\n",hoy_con_fecha_completa,"\n",hoy_solo_dia_del_mes,"\n",hoy_solo_mes,"\n",
      hoy_solo_year,"\n",hoy_con_hora_completa,"\n",hoy_solo_hora,"\n",
      hoy_solo_minuto,"\n",hoy_solo_segundos,"\n")

##################
math.pi     #es el numero pi

##################
'''operaciones: '''
suma= "+"
resta= "-"
division= "/"
division_entera="//"
multiplicacion= "*"
resto= "%"
potencia= "**"
asignacion="="
igual="=="
desigual="!="
mayor=">"
menor="<"
mayor_igual=">="
menor_igual="<="
And="and"
Or="or"
Not="not"

###################
'''estructuras: '''
#MAIN
if __name__=="__main__":
    funcion_principal()
#SUMA
def suma_n_primeros(n:int)->int:
    suma=0
    for i in range(1,n+1):
        print(i, suma)
        suma=suma+i
        #tambien suma+=i
    return suma
#CONTADOR
def lee_n_numeros_pares(n:int)->int:
    contador = 0
    for i in range(n):
        x=int(input("deme un número entero: "))
        if es_par(x):
            contador+=1
    return contador
#EXISTE
def es_compuesto(n:int)->bool:
    existe=False
    for i in range (2,n):
        if es_multiplo(n,i):
            existe=True
            break
    return existe
'''     esquema existe(coleccion de elementos, condicion )
            existe=Falso
            hacemos un recorrido de la coleccion
                si el elemento cumple la condicion
                    existe=Verdad
                    break
            devuelve existe
'''
#PARATODO
def es_primo(n:int)->bool:
    paraTodo=True
    for i in range (2,n):
        if es_multiplo(n,i):
            paraTodo=False
            break
    return paraTodo
'''     esquema paraTodo(coleccion, condicion)
            paraTodo=verdad
            recorremos la coleccion:
                si el elemento NO cumple la condicion
                    paraTodo=falso
                    break
            devuelve paraTodo
'''
#LEER ARCHIVO
def leer_clima(fichero:str)->list[RegistroClima]:
    lista_registros=[]
    with open(fichero) as f:
        lector=csv.reader(f)
        next(lector) #solo si el fichero tiene una primera línea distinta
        for fecha_cadena, lluvia, tmax, tmin in lector:
        #for tupla in lector
        #convertir las cadenas de caracteres en datos con su tipo
            fecha=datetime.datetime.strptime(fecha_cadena,"%Y-%m-%d").date()
            #si la lectura se hubiera hecho sin desempaquetar
            #aquí pondriamos
            #fecha=datetime.strptime(tupla[0],"%Y-%m-%d").date()
            lluvia=float(lluvia)
            tmax=float(tmax)
            tmin=float(tmin)
            r=RegistroClima(fecha,lluvia,tmax,tmin)
            lista_registros.append(r)
        return lista_registros
    
##################
'''variables: '''
#tipos:
x=0
x=4.5
x="hola"
x=True
lista=list()            #[]
tupla=tuple()           #()
conjunto=set()          #{}
diccionario=dict()      #{}       not yet       vuelos={"Iberia": ["Madrid", "Barcelona, Valencia"], "Ryanair": ["Paris","Londres"]}
Named_Tuple = NamedTuple("RegistroClima", [("fecha", datetime),
                        ("lluvia", float), ("temp_max", float), ("temp_min",float)])
fecha=datetime.strptime(fecha_cadena,"%Y-%m-%d")

'''funciones varias: '''
len(lista)
min(x)
max(x)
enumerate(lista)
zip(lista1,lista2)
range(2,x)
lista1.append(x)
conjunto.add(x)
lista=lista[ : :-1]     #partes de esta función lógica-> 
                        #   [ : -> donde inicia la lectura de (en este caso) la lista {nada == desde el inicio}
                        #   : : -> donde finaliza la lectura de la lista {nada == hasta el final}
                        #   : ] -> forma de leerlo {-1 == del revés}
open(fichero)
csv.reader(fichero)
next(lector)
min(lista,   key=lambda x: x.temp_min)
lista[0]
lista[-1]
fecha=datetime.datetime.strptime(fecha_cadena,"%Y-%m-%d")        #str -> datetime
fecha_cadena=fecha.strftime("%Y-%m-%d")                         #datetime -> str
lista.sort()
sum(len(lista1))
letras.isdigit()
letras.isalpha()