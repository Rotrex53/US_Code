from coordenadas import *

def test_calcular_distancia():
    coord1 = Coordenadas(40.7128,-74.0060)
    coord2 = Coordenadas(34.0522,-118.2437)
    resultado = calcular_distancia(coord1, coord2)
    print(f"el calculo de la distancia euclidea de {coord1} y {coord2} es: {resultado}")

def test_calcular_media_coordenadas():
    coords = [Coordenadas(40.7128, -74.0060),Coordenadas(34.0522, -118.2437),Coordenadas(41.8781, -87.6298)]
    resultado = calcular_media_coordenadas(coords)
    print(f"La media de las coordenadas es: {resultado}")




if __name__=="__main__":
    #test_calcular_distancia()
    test_calcular_media_coordenadas()