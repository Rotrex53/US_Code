package fp.burger;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class FactoriaVisita {
	public Visita parseaVisita(String lineaCSV) {
		return new Visita(lineaCSV);
	}
	
	public static List<Visita> leeVisita(String ruta){
		List<Visita> res = new ArrayList<>();
		try {
			List<String> lineas = Files.readAllLines(Paths.get(ruta));
			for(int i=1; i<lineas.size(); i++) {
				String linea = lineas.get(i);
				res.add(new Visita(linea));
			}
		}catch(IOException e) {
			e.printStackTrace();
		}
		return res;
		
	}
}
