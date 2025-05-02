package test;

import java.time.*; import java.util.List; import main.*;

public class VueloTest {

	public static void main(String[] args) {
		Trayecto trayecto1 = new Trayecto("Huelva", "Sevilla");
		Trayecto trayecto2 = new Trayecto("Cáceres", "Badajoz");
		
		List<String> tripulacion1 = List.of("AV1111", "PP1234", "CP9876");
		List<String> tripulacion2 = List.of("AV2222", "PP5678", "CP5432");
		
		Vuelo v1 = new Vuelo(
				trayecto1, 12.3, 13, 20, "HW0000", LocalDate.of(2000, 2, 2), 
				Duration.ofHours(1), tripulacion1, false, 0.5
				);
		
		
		Vuelo v2 = new Vuelo(
				trayecto2, 6.0, 14, 25, "HW0000", LocalDate.of(2000, 2, 2), 
				Duration.ofHours(5), tripulacion2, false, 1.6
				);
		
		System.out.println(v1);
		System.out.println(v2);
		
		System.out.println(v1.getTripulacion());
		System.out.println(v2.getTripulacion());
		
		System.out.println(v1.equals(v2));
		System.out.println(v2.compareTo(v1));
		//System.out.println(v1.incrementaPrecioPorcentaje(0.2));
	}

}
