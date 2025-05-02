package fp.universidad.tipos;
import java.time.*;

public record Tutoria(String dia_semana, LocalTime hora_comienzo, LocalTime hora_fin) {
	
	//Constructor 2
	public Tutoria(String dia_semana, LocalTime hora_comienzo, Duration duracion) {
		this(dia_semana, hora_comienzo, hora_comienzo.plus(duracion));
	}
	
	public Integer getDuracion() {
		return (int) hora_comienzo.until(hora_fin, null);
	}
	
	public String toString() {
		return dia_semana + " " + hora_comienzo + "-" + hora_fin;
	}
	
}
