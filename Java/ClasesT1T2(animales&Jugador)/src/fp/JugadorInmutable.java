package fp;

import java.time.LocalDate;

// SOLO CON TIPOS INMUTABLES

public record JugadorInmutable(
		String nombre,
		LocalDate fechaNacimiento,
		Integer altura,
		String nacionalidad) 
	implements Comparable<JugadorInmutable> {

	// ¿Qué está ya hecho en los records?
	// Constructor canónico
	// todos los métodos getters
	// toString, equals, hashcode
	
	// No están: Restricciones
	public JugadorInmutable {
		checkAltura(altura);
	}
	
	
	private void checkAltura(Integer altura) {
		if(altura<0) {
			throw new 
			IllegalArgumentException(
			"La altura no puede ser negativa");
		}
	}
	
	// No está: propiedades derivadas
	// Propiedad derivada
	// Edad
	public Integer edad() {
		return fechaNacimiento
				.until(LocalDate.now())
				.getYears();
	}
	
//	// No está: compareTo
//	public int compareTo(JugadorInmutable o) {
//		int r = this.nombre().compareTo(o.nombre());
//		if(r==0) {
//			r = this.fechaNacimiento().compareTo(o.fechaNacimiento());
//		}
//		return r;
//	}

	
}
