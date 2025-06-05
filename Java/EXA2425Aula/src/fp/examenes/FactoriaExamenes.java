package fp.examenes;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class FactoriaExamenes {
	public Examen parsearExamen(String lineaCSV) {
		return new Examen(lineaCSV);
	}
	
	public static List<Examen> leeExamen(String ruta){
		List<Examen> examenes = new ArrayList<>();
		try {
			List<String> lineas = Files.readAllLines(Paths.get(ruta));
		for(int i=1; i<lineas.size(); i++) {							//Salto de la primera linea del csv
			examenes.add(new Examen(lineas.get(i)));
		}
		}catch(IOException e) {
			e.printStackTrace();
		}
		
		return examenes;
	}
}
