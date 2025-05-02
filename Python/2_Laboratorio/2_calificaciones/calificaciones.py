def nota_teoria()->tuple:
    print("introducir notas, si no se ha presentado ponga cualquier cosa")
    
    examen_1=input("nota del examen 1: ")
    examen_2=input("nota del examen 2: ")

    try:
        examen_1=float(examen_1)
    except ValueError:
        examen_1=examen_1

    try:
        examen_2=float(examen_2)
    except ValueError:
        examen_2=examen_2

    if not isinstance(examen_1, float) and not isinstance(examen_2, float):
        examen_1 = 0.0
        examen_2 = 0.0

    if not isinstance(examen_1, float):
        examen_1=0.0

    if not isinstance(examen_2, float):
        examen_2=0.0

    media_teoria=(examen_1+examen_2)/2

    if media_teoria < 4:
        media_teoria=0
        print(f"con las notas: {examen_1} y {examen_2}")
        print("la nota media es: 0, por ser la media menos de un 4 \n")
    else:
        print(f"con las notas: {examen_1} y {examen_2}")
        print(f"la nota media es: {media_teoria} \n")

    return examen_1, examen_2, media_teoria

def nota_practica()->tuple:
    print("introducir la nota de la práctica, si no se ha presentado ponga cualquier cosa")
    examen_LAB=input("nota del examen de laboratorio: ")

    try:
        examen_LAB=float(examen_LAB)
    except ValueError:
        examen_LAB=examen_LAB
    if not isinstance(examen_LAB, float):
        examen_LAB=0.0
    
    return examen_LAB


def nota_cuatrimestre():
    examen_1, examen_2, media_teoria=nota_teoria()
    examen_LAB=nota_practica()
    tupla=(examen_1, examen_2, examen_LAB)
    if media_teoria<4:
        nota_final_cuatrimestre=0
    else:
        nota_final_cuatrimestre=(media_teoria*0.2)+(examen_LAB*0.8)

    print(f"Tu nota final del cuatrimestre es: {nota_final_cuatrimestre}")
    return nota_final_cuatrimestre