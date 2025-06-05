package fp.burger.test;

import java.time.Duration;
import java.time.LocalDate;
import java.util.List;
import java.util.Map;
import java.util.SortedSet;

import fp.burger.Competicion;
import fp.burger.FactoriaVisita;
import fp.burger.Visita;

public class TestCompeticion {

	public static void main(String[] args) {
		List<Visita> listaCSV = FactoriaVisita.leeVisita("data/burger.csv");
		
		Competicion competicion = new Competicion(listaCSV.stream());
		
//		Visita v1 = listaCSV.getFirst();
//		System.out.println(v1);
//		System.out.println(v1.getPaladar());
//		System.out.println(v1.getNumEvaluacioney s());
		
		
		//FACTORIA-----------------------------------------------------------------------------
		System.out.println("Leidas " + listaCSV.size() + " visitas \n\n");
		System.out.println("Primera visita: " + listaCSV.getFirst() + "\n\n");
		System.out.println("Última visita: " + listaCSV.getLast() + "\n\n");
		
		//EJ1----------------------------------------------------------------------------------
		Duration d = Duration.ofMinutes(240);
		SortedSet<String> ej1 = competicion.getEmailsOrdenados(d);
		System.out.println("Los emails de las visitas mayor a "
		+ d.toMinutes() + " minutos son: \n" + ej1 + "\n\n");
		
		//EJ2----------------------------------------------------------------------------------
		Integer ej2 = competicion.getTotalVisitasComilones();
		System.out.println("El total de visitas con un número de "
				+ "evaluaciones mayor a la media es: \n" + ej2 + "\n\n");
		
		//EJ3----------------------------------------------------------------------------------
		String ej3 = competicion.getPeorHamburgueseriaPorCalidadIngredientes();
		System.out.println("Si se tiene en cuenta solo la calidad "
				+ "de ingredientes, la peor hamburguesería es: \n" + ej3 + "\n\n");
		
		//EJ4----------------------------------------------------------------------------------
		Map<String, String> ej4 = competicion.getTopComilonPorCPEnDia(LocalDate.of(2024, 06, 02));
		System.out.println("En el día " + LocalDate.of(2024, 06, 02)
		+ " la persona que más comió de cada CP es: \n" + ej4 + "\n\n");
		
		//EJ5----------------------------------------------------------------------------------
		String ej5 = competicion.getHamburgueseriaGanadora();
		System.out.println("La hamburguesería ganadora del campeonato es: \n" + ej5 + "\n\n");
	}

}
