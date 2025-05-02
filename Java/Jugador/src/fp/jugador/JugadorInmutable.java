package fp.jugador;

import java.time.LocalDate;

//SOLO CON TIPOS INMUTABLES
public record JugadorInmutable(
		String nombre, 
		LocalDate fechaNacimiento,
		Integer altura, 
		String nacionalidad) implements Comparable<JugadorF>{
	//¿Qué está ya hecho en los records?:
		//Constructor Canónico
		//todos los metodos getters
		//toString, equals, hashcode
	
	//No estan;
		//Las Restricciones
		//CompareTo
		//Propiedades derivadas
	
	//Restricciones
	public JugadorInmutable{
		checkAltura(altura);
	}
	
		private void checkAltura(Integer altura) {
			if(altura<0) {
				throw new IllegalArgumentException(
					"La altura no puede ser negativa");
			}
		}
		
	//Propiedad derivada: Edad a partir de fechaNacimiento
	public Integer getEdad() {
		return fechaNacimiento.until(LocalDate.now()).getYears();
	}
	
	//CompareTo
	public int compareTo(JugadorInmutable o){
			int r = this.nombre().compareTo(o.getNombre());
			if (r==0) {	r = this.getfechaNacimiento().compareTo(o.fechaNacimiento()) }
			return r;
	}
}
