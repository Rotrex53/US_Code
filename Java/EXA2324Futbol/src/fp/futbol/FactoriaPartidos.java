package fp.futbol;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class FactoriaPartidos {
	public Partido parsearPartido(String lineaCSV) {
		return new Partido(lineaCSV);
	}
	
	public static List<Partido> leeEstadisticasPartidos(String ruta) {
		List<Partido> res = new ArrayList<>();
		try {
			List<String> lineas = Files.readAllLines(Paths.get(ruta));
			for(int i=1; i<lineas.size(); i++) {
				res.add(new Partido(lineas.get(i)));
			}
		} catch(IOException e) {
			e.printStackTrace();
		}
		return res;
	}
}
