package fp.votacion;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class FactoriaEncuestas {
	public Encuesta parsearEncuesta(String lineaCSV) {
		return new Encuesta(lineaCSV);
	}

	public static List<Encuesta> leeEncuesta(String ruta){
		List<Encuesta> res = new ArrayList<Encuesta>();
		try {
			List<String> lineas = Files.readAllLines(Paths.get(ruta));
			for(String linea: lineas) {
				res.add(new Encuesta(linea));
			}
		}catch(IOException e) {
			e.printStackTrace();
		}
		return res;
	}
}
