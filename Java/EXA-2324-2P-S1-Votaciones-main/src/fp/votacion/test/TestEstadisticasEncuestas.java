package fp.votacion.test;

import java.time.LocalDate;
import java.util.List;
import java.util.Map;
import java.util.SortedMap;
import java.util.SortedSet;
import java.util.stream.Stream;

import fp.votacion.*;

public class TestEstadisticasEncuestas {

	public static void main(String[] args) {
		String ruta = "data/encuestas_electorales.csv";
		List<Encuesta> e1 = FactoriaEncuestas.leeEncuesta(ruta);
		
//		System.out.println(e1.getFirst());
		
		Stream<Encuesta> listStream1 = e1.stream();
		
		Stream<Encuesta> listStream2 = e1.stream();
		EstadisticasEncuestas ee2 = new EstadisticasEncuestas(listStream2);

		
		EstadisticasEncuestas ee1 = new EstadisticasEncuestas(listStream1);

		
//		System.out.println(ee1.equals(ee2));
		
		//EJ1---------------------------------------------------------------------------------------
		String consultora = "Consultora A";
		LocalDate fechaMaxima = LocalDate.of(2024, 05, 29);
		Double ej1 = ee1.getMediaNumEncuestadosConsultorayFecha(consultora, fechaMaxima);
		System.out.println("La media de la consultora " + consultora + " con fecha de fin anterior a "
				+ fechaMaxima + " es " + ej1 + "\n\n");
		
		//EJ2---------------------------------------------------------------------------------------
		TipoEncuesta tipo = TipoEncuesta.Internet;
		Encuesta ej2 = ee1.getEncuestaMasEncuestadosPorDia(tipo);
		System.out.println("La encuesta de tipo " + tipo + 
				" con mayor ratio de encuestados por día es: \n" + ej2 + "\n\n");
		
		//EJ3---------------------------------------------------------------------------------------
		Integer n = 3;
		List<String> ej3 = ee1.getPartidosMasFrecuentesOrdenados(n);
		System.out.println("Los " + n + " partidos más frecuentes en las encuestas son: \n" 
				+ ej3 + "\n\n");
		
		//EJ4---------------------------------------------------------------------------------------
		Integer umbral = 2636;
		SortedMap<String, Boolean> ej4 = ee1.getSuperaEncuestadosPorPais(umbral);
		System.out.println("¿Todas las encuestas de estos países superan los " 
				+ umbral + " encuestados?: \n" + ej4 + "\n\n");
		
		//EJ5---------------------------------------------------------------------------------------
		Double umbralPorcentaje = 97.;
		Map<String, SortedSet<String>> ej5 = ee1.getPaisesPorPartidoMayorPorcentaje(umbralPorcentaje);
		System.out.println("Países donde cada partido ha obtenido un porcentaje de votos superior a "
				+ umbralPorcentaje + "%: \n" + ej5 + "\n\n");
		
		//A parte
//		System.out.println(ee1.getMenorNumEncuestadosPorPais("Alemania"));
	}

}
