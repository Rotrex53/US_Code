package fp.universidad.tipos;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class FactoriaUniversidad {
	
	public Espacio creaEspacio(String c) {
		return new Espacio(c);
	}
	
	public static List<Espacio> leeEspacios(String espacios) {
		List<Espacio> res = new ArrayList<Espacio>();
		try {
			List<String> lineas = Files.readAllLines(Paths.get(espacios));
			for (String línea:lineas){
				res.add(new Espacio(línea));
			}
		}
		catch(IOException e){
			e.printStackTrace();
		}
		return res;
	}
	
	
	public Despacho creaDespacho(String c) {
		return new Despacho(c);
	}
	
	public static List<Despacho> leeDespachos(String despachos){
		List<Despacho> res = new ArrayList<Despacho>();
		try {
			List<String> lineas = Files.readAllLines(Paths.get(despachos));
			for(String linea: lineas) {
				res.add(new Despacho(linea));
			}
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		return res;
	}
	
}
