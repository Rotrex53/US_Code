package fp.vino;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

import fp.utiles.Checkers;

public class FactoriaVinos {
	
	private Vino parsearVino(String linea) {
		String [] trozos = linea.split(",");
		Checkers.check("cadena no trozeada", trozos.length==5);
		String pais = trozos[0].strip();
		String region = trozos[1].strip();
		Integer puntos = Integer.parseInt(trozos[2].strip());
		Double precio = Double.parseDouble(trozos[3].strip());
		String uva = trozos[4].strip();
		return new Vino(pais, region, puntos, precio, uva);
	}
	
	public Vinoteca leerVinoteca(String ruta) {
		Vinoteca res ;
		try {
			List<String> lineas = Files.readAllLines(Paths.get(ruta));
			for (String linea: lineas) {
				res.agregarVino(parsearVino(linea));
			}
		}
		catch(IOException e){
			e.printStackTrace();
		}
		return res;
	}
}
