package fp.examenes.test;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.stream.Collectors;

import fp.examenes.CalendarioExamenes;
import fp.examenes.Examen;
import fp.examenes.FactoriaExamenes;
import fp.examenes.TipoExamen;

public class TestCalendarioExamenes {

	public static void main(String[] args) {
		List<Examen> csvLeido = FactoriaExamenes.leeExamen("data/examenes.csv");
		CalendarioExamenes calendario = new CalendarioExamenes(csvLeido.stream());

		//Ej1
		System.out.println("EJ1==========================================================");
		testGetExamenesPorAula(calendario);
		
		System.out.println("EJ2==========================================================");
		testGetExamenMayorPorcentajeAsistentes(calendario, LocalTime.of(8, 30), "F1.30");
		testGetExamenMayorPorcentajeAsistentes(calendario, LocalTime.of(15, 30), "I2.31");
		
		System.out.println("EJ3==========================================================");
		testGetAulasExamenesTipo(calendario, TipoExamen.PRACTICO);
		testGetAulasExamenesTipo(calendario, TipoExamen.TEORICO);
		
		System.out.println("EJ4==========================================================");
		testGetAulaMasOcupada(calendario, LocalDate.of(2024, 05, 25));
		testGetAulaMasOcupada(calendario, LocalDate.of(2024, 06, 07));
		
		System.out.println("EJ5==========================================================");
		testGetFechasConMasAulasDe(calendario, 5);
		testGetFechasConMasAulasDe(calendario, 8);

	}

	public static void testGetExamenesPorAula(CalendarioExamenes calendario) {
		Map<String, Set<Examen>> ej1 = calendario.getExamenesPorAula();
		System.out.println("Exámenes por aula (por motivos de espacio, solo se muestran las asignaturas): \n");
		ej1.keySet().stream()
			.forEach(e -> System.out.println("Aula " + e + ": " + 
					ej1.get(e).stream()
					.map(Examen::getAsignatura).collect(Collectors.toList()) + "\n"));
	}
	
	public static void testGetExamenMayorPorcentajeAsistentes(CalendarioExamenes calendario, LocalTime hora, String aula) {
		Examen ej2 = calendario.getExamenMayorPorcentajeAsistentes(hora, aula);
		System.out.println("Examen con mayor porcentaje de asistentes realizado en el aula " + aula +
				" y con hora de comienzo posterior a las " + hora + ": \n" + ej2 + "\n");
	}
	
	public static void testGetAulasExamenesTipo(CalendarioExamenes calendario, TipoExamen tipo) {
		SortedSet<String> ej3 = calendario.getAulasExamenesTipo(tipo);
		System.out.println("Aulas utilizadas en exámenes de tipo " + tipo + ": " + ej3 + "\n");
	}
	
	public static void testGetAulaMasOcupada(CalendarioExamenes calendario, LocalDate fecha) {
		String ej4 = calendario.getAulaMasOcupada(fecha);
		System.out.println("Aula con mayor ocupación en la fecha " + fecha + ": " + ej4 + "\n");
	}
	
	public static void testGetFechasConMasAulasDe(CalendarioExamenes calendario, Integer i) {
		List<LocalDate> ej5 = calendario.getFechasConMasAulasDe(i);
		System.out.println("Fecha con más de " + i + " aulas: " + ej5);
		
	}

}
