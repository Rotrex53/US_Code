package fp.test;
import fp.jugador.*; import java.time.LocalDate;

public class test_jugadorF {
	
	public static void main(String[] args) {
		//Constructor canónico
		JugadorF j1 = new JugadorF("Jugador 1", LocalDate.of(2000, 5, 1), 190, "Española");
		JugadorF j2 = new JugadorF("Jugador 1", LocalDate.of(2000, 5, 1), 185, "Francesa");
		
		System.out.println(j1.getNombre());
		System.out.println(j1.getNombre());
		System.out.println(j1);
		System.out.println(j1.equals(j2));
		System.out.println(j1==j2);		
		System.out.println(j2.hashCode());
		
		System.out.println(j1.compareTo(j2));
		
		try {
			jugador j3 = new Jugador(
					"A", LocalDate
					)
		}
		String s = "Jugador1, 28/06/1990,190,Española";
		Jugador j4 = new Jugador(s);
		System.out.println(j4);
		
		JugadorInmutable ji = new JugadorInmutable("A",LocalDate.of(1900, 5, 1),190,"Española");
		System.out.println(ji); //Si queremos obtener un atributo concreto usamos .nombre(), .fechaNacimiento(),...
	}
}
