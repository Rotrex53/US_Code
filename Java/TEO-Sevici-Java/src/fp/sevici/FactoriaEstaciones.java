package fp.sevici;

import java.util.*;
import fp.utiles.*;

public class FactoriaEstaciones {
	
	public static RedEstaciones leerRedEstaciones(String nombreFichero, String nombreRed) {
		List<String> lineas = Ficheros.leeFichero("error al leer", nombreFichero);
		lineas.remove(0);
		
		Set<Estacion> estacionesLeidas = new HashSet<Estacion>();
		
		for(String linea: lineas) {
			estacionesLeidas.add(parsearEstacion(linea));
		}
		
		return new RedEstaciones(nombreRed, estacionesLeidas);
	}
	
	public static Estacion parsearEstacion(String lineaCSV) {
		String [] trozos = lineaCSV.split(",");
		String [] trozo1 = trozos[0].trim().split("_");
		
		return null;
	}
}
