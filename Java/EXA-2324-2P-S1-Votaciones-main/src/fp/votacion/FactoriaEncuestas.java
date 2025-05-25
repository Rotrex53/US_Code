package fp.votacion;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class FactoriaEncuestas {
	public static Encuesta parsearEncuesta(String lineaCSV) {
		return new Encuesta(lineaCSV);
	}

	public static List<Encuesta> leeEncuesta(String ruta){
		List<Encuesta> res = new ArrayList<Encuesta>();
		try {
			List<String> lineas = Files.readAllLines(Paths.get(ruta));
			for(int i=1; i<lineas.size(); i++) {
				String linea = lineas.get(i);
				res.add(parsearEncuesta(linea));
			}
		}catch(IOException e) {
			e.printStackTrace();
		}
		return res;
	}
}
