package fp.test;

import java.time.LocalDate;

import fp.Jugador;
import fp.JugadorInmutable;

public class TestJugador {
	
	public static void main(String[] args) {
		
		// Constructor canónico
		Jugador j1 = new Jugador(
				"A",
				LocalDate.of(1900, 5, 1),
				190, "Española");
		// Constructor c2
		Jugador j2 = new Jugador(
				"A",
				LocalDate.of(2000, 5, 1));
		
		System.out.println(j1.getNombre());
//		j1.setNombre("JJ1");
		System.out.println(j1.getNombre());
		
		System.out.println(j1);
		
		System.out.println(j1.equals(j2));
		System.out.println(j1==j2);
		
		System.out.println(j1.hashCode());
		System.out.println(j2.hashCode());
		
		System.out.println(j1.compareTo(j2));
		
		try {
		Jugador j3 = new Jugador(
				"A",
				LocalDate.of(1900, 5, 1),
				-20, "Española");
		}
		catch(Exception e) {
			System.out.println(""
					+ "Excepción lanzada al "
					+ "crear j3");
		}
		
		System.out.println("Fin");

		
		
		String s = "Jugador1,28/06/1990,190,Española";
		Jugador j4 = new Jugador(s);
		System.out.println(j4);
		
		
		JugadorInmutable ji = 
				new JugadorInmutable("A",
						LocalDate.of(1900, 5, 1),
						190, "Española");
		System.out.println(ji.altura());
	}

}
