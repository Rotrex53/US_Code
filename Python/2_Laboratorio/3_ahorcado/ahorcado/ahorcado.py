import os
import sys
import random

def get_data_file(filename):
    '''
    Obtiene la ruta correcta del archivo de datos, ya sea en el entorno de desarrollo o en el ejecutable empaquetado.
    '''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    else:
        # Ajustamos la ruta para que suba un nivel y busque en la carpeta data
        return os.path.join(os.path.dirname(__file__), '../data', filename)

def cargar_palabras(ruta):
    ruta = get_data_file(ruta)  # Asegúrate de que esta línea esté aquí
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip())
        return res

def elegir_palabra(palabras):
    '''
    Elige la palabra a adivinar:
    - Selecciona una palabra aleatoria de la lista 'palabras'
    - Devuelve la palabra seleccionada
    Ayuda: 
    - La función 'random.choice' del paquete 'random' recibe una lista de opciones y 
      devuelve una de ellas seleccionada aleatoriamente.
    '''
    return random.choice(palabras)

def enmascarar_palabra(palabra, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    res=[]
    for l in palabra:
        if l in letras_probadas:
            res.append(l)
        else:
            res.append("_")

    return res


def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''
    res=[]
    l=input("introduce una letra: ").lower()
    while len(l)!=1 or not l.isalpha():
        l=input("Por favor, introduce solo una letra: ").lower()
    while l in letras_probadas:
        l=input("introduce una letra no probada: ").lower()
    res.append(l)
    #letras_probadas.add(l)
    return " ".join(res)

def comprobar_letra(palabra_secreta, letra):
    '''
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Mostrar el mensaje correspondiente informando al usuario
    - Devolver True si estaba y False si no
    '''
    if letra in palabra_secreta:
        print("Bien hecho, esta letra está en la palabra")
        return True
    else:
        print("Vaya... Esta letra no está en la palabra")
        return False
    
def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    '''
    for letra in palabra_secreta:
        if letra not in letras_probadas:
            return False
    return True

def ejecutar_turno(palabra_secreta, letras_probadas):
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Añadir la letra al conjunto de letras probadas
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla
    '''
    palabra_enmascarada=enmascarar_palabra(palabra=palabra_secreta, letras_probadas=letras_probadas)
    print(f"Palabra: {palabra_enmascarada}")
    l=pedir_letra(letras_probadas)
    if l in palabra_secreta:
        print("Perfecto! La palabra contiene esa letra")
        return True
    else:
        print("Oh vaya! Esa letra no se encuentra en la palabra")
        return False
    

def jugar(max_intentos, palabras):
    '''
    Completar una partida hasta que el jugador gane o pierda:
    - Mostrar mensaje de bienvenida
    - Elegir la palabra secreta a adivinar
    - Inicializar las variables del juego (letras probadas e intentos fallidos)
    - Ejecutar los turnos de juego necesarios hasta finalizar la partida, y en cada turno:
      > Averiguar si ha habido acierto o fallo
      > Actualizar el contador de fallos si es necesario
      > Comprobar si se ha superado el número de fallos máximo
      > Comprobar si se ha completado la palabra
      > Mostrar el mensaje de fin adecuado si procede o el número de intentos restantes
    '''
    print("Bienvenido al Ahorcado, se eligirá una palabra secreta mostrandose\ncuales serán los puestos y usted deberá adivinar las letras restantes. \nMucha suerte! Vamos allá...")
    
    palabra_elegida=elegir_palabra(palabras)
    lista_letras_probadas=[]
    
    letra=None
    palabra_enmascarada=enmascarar_palabra(palabra=palabra_elegida, letras_probadas=lista_letras_probadas) #letras_probadas=None
    
    print(f"Palabra enmascarada: {palabra_enmascarada}")

    resultado=False

    while max_intentos > 0 and resultado!=True:

        letra=pedir_letra(letras_probadas=lista_letras_probadas)
        lista_letras_probadas.append(letra)
        acierto=comprobar_letra(palabra_secreta=palabra_elegida, letra=letra)

        if acierto==True:
            print("Resultado: Acierto")
        else:
            print("Resultado: Fallo")
            max_intentos=max_intentos-1
            print(f"Te quedan {max_intentos} intentos")

        resultado=comprobar_palabra_completa(palabra_secreta=palabra_elegida, letras_probadas=lista_letras_probadas)
    
    if resultado==True:
        print("Has ganado! Enhorabuena")
    else:
        print("Vaya... Has perdido, otra vez será")

        






# Iniciar el juego
if __name__ == "__main__":
    palabras = cargar_palabras('palabras_ahorcado.txt')  # Asegúrate de que solo estás pasando el nombre del archivo
    jugar(6, palabras)