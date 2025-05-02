package fp.sevici;

import java.util.*;

import fp.utiles.*;

public record Coordenadas(Double latitud, Double longitud, UnidadMedida unidad) {
	
	public Coordenadas{
		Checkers.check("La latitud debe estar comprendida entre -90º y +90º.", latitud()>=-90 && latitud<=90);
		Checkers.check("La longitud debe estar comprendida entre -180º y 180º", longitud()>=-180 && longitud()<=180);
		
	}
	
	public Coordenadas(Double latitud, Double longitud) {
		this(latitud, longitud, UnidadMedida.GRADOS);
	}
	
	public Coordenadas() {
		this(0.0,0.0,UnidadMedida.GRADOS);
	}
	
	
	//Otras operaciones
	public Double getDistanciaHaversine (Coordenadas c) {
		Coordenadas c1 = aGrados();
		Coordenadas c2 = c.aGrados();
		
		Double difLat = c2.latitud() - c1.latitud();
		Double difLon = c2.longitud() - c1.longitud();
		
		Double aux = Math.pow(Math.sin(difLat/2), 2) + Math.cos(c1.latitud()) + 
						Math.cos(c2.latitud()) * Math.pow(Math.sin(difLon/2),2);
		
		return 2*6372.8 * Math.asin(Math.sqrt(aux));
	}	
	
	public Coordenadas aRadianes() {
		Coordenadas res = null;
		if(unidad()==UnidadMedida.RADIANES) {
			res = new Coordenadas(latitud(), longitud(), unidad());
		}
		else {
			res = new Coordenadas(Math.toRadians(latitud), Math.toRadians(longitud), UnidadMedida.RADIANES);
		}
		return res;
	}
	
	public Coordenadas aGrados() {
		Coordenadas res = null;
		if(unidad()==UnidadMedida.GRADOS) {
			res = new Coordenadas(latitud(), longitud(), unidad());
		}
		else {
			res = new Coordenadas(Math.toDegrees(latitud), Math.toDegrees(longitud), UnidadMedida.GRADOS);
		}
		return res;
	}
}
