'''Suponga declaradas las siguientes variables: lista (de tipo list), tupla (de tipo tuple), 
conjunto (de tipo set) y diccionario (de tipo dict). Escriba una o dos instrucciones para 
realizar cada una de las siguientes acciones; si considera que no es posible realizar 
alguna de las acciones solicitadas, explique por qué.'''

lista=list()
tupla=tuple()
conjunto=set()
diccionario=dict()

#Añadir el valor 10 a conjunto.
conjunto.add(10)

#Sustituir el primer elemento de lista por el valor 20.
lista[0]=20

#Sustituir el primer elemento de tupla por el valor 20.
'''no se puede'''

#Eliminar la clave 10 de diccionario.
'''no sabemos'''

#Eliminar la primera posición de conjunto.
conjunto.pop()

#Qué muestra en la consola esta secuencia 
'''lista1=[i for i in range(0,11,2)] 
lista2=[(i,i+1) for i in lista1] 
print(sum((y for _,y in lista2)))'''
'''muestra una suma de los numeros impares del 0 al 11'''

#Dada la función
def funcion(x, y, z): 
    if y: 
        a=x+z 
    else: 
        a=x-z 
    return a
#¿Qué muestra en pantalla la expresión? 
print(funcion(5, False, -1)+funcion(3,True,2))
'''mostrará en pantalla (6+5): 11'''

#¿Cuál es la salida del siguiente trozo de código?
lista=[2,3,1,0] 
for i in lista: 
    print(sum(x for x in lista[i:]))
'''suma los elementos de la lista a partir del valor dado para i, llegando desde i hasta el final'''
lista=[2,3,1,0]
for i in lista:
    lista_desglosada=lista[i:]
    suma=0
    for x in lista_desglosada:
        suma += x
    print(suma)

#Indique en cada caso cuál sería el valor devuelto por la función:
def funcion(lista:list[tuple], valor): 
    res = [] 
    for e in lista: 
        if e[0] == valor: 
            res.append(e[1]) 
        if e[1][0] == valor: 
            break 
    return res
"a."; funcion([("a", "arriba"), ("b", "barco"), ("c", "casa")], "b")
"b."; funcion([("1", "arriba"), ("2", "barco"), ("1", "casa")], "1")
"c."; funcion([("arriba", "a"), ("barco", "b"), ("casa", "c")], "b")
'''a. [barco]'''
'''b. [arriba, casa]'''
'''c. []'''

#Crea una variable llamada hoy de tipo datetime con la fecha y hora actual. Muestra en 
#la consola el resultado de multiplicar el día de hoy por 24 más la hora
import datetime
hoy=datetime.datetime.now()
resultado=24*hoy.day + hoy.hour
print(resultado)

#Tenemos una tupla de tipo Persona con los siguientes atributos: 
#   nombre: str con el nombre de la persona. 
#   edad: int con la edad de la persona en años. 
#   tiene_licencia: Booleano que indica si la persona tiene licencia de conducir. 
#   hobbies: Conjunto de str con los hobbies o actividades que le gustan a la persona. 
#   paises_visitados: Conjunto de str con los países que la persona ha visitado. 
#   libros_leidos: Lista de str con los libros que la persona ha leído en orden de lectura.
from typing import NamedTuple 
Persona = NamedTuple('Persona',[("nombre",str),("edad",int),("tiene_licencia",bool),("hobbies",set[str]),
                                ("paises_visitados",set[str]),("libros_leidos",list[str])])
p1=Persona("Paco",23,True,{"Programar","Estudiar","Comer","Hablar"},{"España","Francia","Italia"},["El señor de los anillos"])
p2=Persona("Andrea",20,False,{"Deporte","Fiestas"},{"Uganda","Nigeria","Canada"},["Romeo y Julieta"])

#   a) Si tenemos dos variables p1 y p2 de tipo Persona, escriba una expresión lógica que 
#   devuelva si es cierto que el último libro que ha leído p1 es “Romeo y Julieta” y p2 no lo 
#   ha leído aún.
from typing import NamedTuple 
Persona = NamedTuple('Persona',[("nombre",str),("edad",int),("tiene_licencia",bool),("hobbies",set[str]),
                                ("paises_visitados",set[str]),("libros_leidos",list[str])])
p1=Persona("Paco",23,True,{"Programar","Estudiar","Comer","Hablar"},{"España","Francia","Italia"},["El señor de los anillos"])
p2=Persona("Andrea",20,False,{"Deporte","Fiestas"},{"Uganda","Nigeria","Canada"},["Romeo y Julieta"])

if p1.libros_leidos[-1] == "Romeo y Julieta" and p2.libros_leidos[-1] != "Romeo y Julieta":
    True

#   b) Si tenemos un conjunto de tuplas de tipo Persona, escriba la expresión que muestre en 
#   la consola la suma de las edades de las personas que tienen más de 3 hobbies y su 
#   nombre comienza por ‘A’ 
conjunto_tuplas={p1,p2}
for p in conjunto_tuplas:
    if len(p.hobbies) > 3 and p.nombre[0] == "A":
        suma_edades=sum(p.edad)
print(suma_edades)

#   c) Si p1 y p2 son de tipo Persona, escriba una expresión lógica que sea verdadera si tanto 
#   p1 como p2 han leído “Romeo y Julieta”, y han nacido en años distintos.
if ("Romeo y Julieta" in p1.libros_leidos and "Romeo y Julieta" in p2.libros_leidos) and (p1.edad != p2.edad):
    True

#   Tenemos un fichero csv con la información de automóviles de segunda mano en venta. 
#   Como el siguiente 
#   1234XYZ, Ford,23/10/2021,21620,34328.7 
#   0987ABC, Seat,18/10/2022,12230,26245.9 
#   ... 
#   Los datos son matrícula de tipo str, nombre de la marca de tipo str, fecha de tipo date, 
#   kilometraje de tipo int y precio de tipo float

#   Define un namedtuple Automovil y una función de lectura para dicho fichero que 
#   devuelva una lista de tuplas. Chequee que las matrículas son 4 dígitos seguidos de tres 
#   letras, que las fechas son posteriores al año 2020 incluido y que los kilómetros son 
#   positivos.  
#   Nota: la invocación cadena.isdigit() de Python devuelve True si todos los caracteres de 
#   cadena son dígitos.  
#   Igualmente, la función isalpha devuelve True si todos lo caracteres de la cadena que 
#   invoca son alfabéticos.
from typing import NamedTuple 
from datetime import date
import csv
Automovil = NamedTuple("Automovil",[("matricula",str),("marca",str),("fecha",date),("kilometraje",int),("precio",float)])

def leer_csv(fichero_csv:str)->list[tuple]:
    with open(fichero_csv, encoding="utf-8") as f:
        lista_r=[]
        lector=csv.reader(f)

        for matricula,marca,fecha_cadena,kilometraje,precio in lector:
            fecha = datetime.datetime.strptime(fecha_cadena, "%Y-%m-%d")
            kilometraje=int(kilometraje)
            precio=float(precio)

            r=Automovil(matricula,marca,fecha,kilometraje,precio)

            lista_r.append(r)
    
    return lista_r

fichero_csv = "ruta/del/archivo.csv" 
lista_automoviles=leer_csv(fichero_csv)
lista_entero=[]
lista_str=[]
verificacion_matricula=False
verificacion_año=False
verificacion_kilometraje=False

for vehiculo in lista_automoviles:
    if len(vehiculo.matricula) == 7:
        if vehiculo.matricula[:4].isdigit():
            lista_entero.append(vehiculo.matricula)
        
        if vehiculo.matricula[4:].isalpha():
            lista_str.append(vehiculo.matricula)

if len(lista_entero) == 4 and len(lista_str) == 3:
    verificacion_matricula = True
else:
    print("no cumple la matricula")

for vehiculo in lista_automoviles:
    if vehiculo.fecha.year >= 2020:
        verificacion_año = True

for vehiculo in lista_automoviles:
    if vehiculo.kilometraje > 0:
        verificacion_kilometraje = True

if verificacion_año == True and verificacion_kilometraje == True and verificacion_matricula == True:
    print("Cumple todos los requisitos")

else: 
    print("No cumple todos los requisitos pedidos")

#   Implemente una función que recibe una lista de tuplas de tipo Automovil y devuelva 
#   una lista ordenada de las marcas de la lista sin repetir. La lista estará ordenada por 
#   longitud de caracteres del nombre de la marca.
def marcas_ordenadas_longitud(lista:list[Automovil])->list:
    lista_marcas_longitud=[]
    for vehiculo in lista:
        if vehiculo.marca not in lista_marcas_longitud:
            lista_marcas_longitud.append(vehiculo.marca)
    return sorted(lista_marcas_longitud, key=len)

#   Implemente una función media_kilometros que reciba una lista de tuplas de tipo 
#   Automovil y un año y devuelva la media de kilómetros de los coches cuya fecha de 
#   matriculación coincide con el año indicado. Si no hay coches del año indicado, la 
#   función devuelve None.
def media_kilometrajes(lista:list[Automovil], año:int)->float | None:
    suma_kilometrajes=0
    contador=0
    for vehiculo in lista:
        if vehiculo.fecha.year == año:
            suma_kilometrajes += vehiculo.kilometraje
            contador += 1
        else:
            suma_kilometrajes=None
            contador=None
    media=suma_kilometrajes/contador
    return media