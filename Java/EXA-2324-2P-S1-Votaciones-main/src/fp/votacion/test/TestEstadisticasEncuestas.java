package fp.votacion.test;

import java.util.List;
import fp.votacion.*;

public class TestEstadisticasEncuestas {

	public static void main(String[] args) {
		String ruta = "data/encuestas_electorales.csv";
		List<Encuesta> e1 = FactoriaEncuestas.leeEncuesta(ruta);
		
		System.out.println(e1);
	}

}
