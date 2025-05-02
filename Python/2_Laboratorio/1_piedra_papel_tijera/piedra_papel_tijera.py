import random

def ordenador_decide_jugada():
    #Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar_torneo()->int:
    print("comienze el juego: \n")
    ronda=1
    puntuacion_usuario=0
    puntuacion_ord=0

    while ronda!=4:
        print("ronda nº",ronda)

        elección_ordenador=ordenador_decide_jugada()
        elección_usuario=usuario_decide_jugada()

        print("el ordenador escogio", elección_ordenador)

        resultado=determina_ganador(elección_usuario, elección_ordenador)

        if resultado == "Ganaste":
            resultado="Has ganado"
            ronda=ronda+1
            puntuacion_usuario=puntuacion_usuario+1
        elif resultado == "Perdiste":
            resultado="Has perdido"
            ronda=ronda+1
            puntuacion_ord=puntuacion_ord+1
        else:
            resultado="Habeis empatado"
            ronda=ronda+1
        print(resultado)
    
    if puntuacion_ord>puntuacion_usuario:
        resultado_final = "El ganador fue el ordenador"
    
    elif puntuacion_ord<puntuacion_usuario:
        resultado_final = "El ganador fue el usuario"

    else:
        resultado_final = "Ha habido un empate"
    
    return print(resultado_final)
    #print(resultado_final)
