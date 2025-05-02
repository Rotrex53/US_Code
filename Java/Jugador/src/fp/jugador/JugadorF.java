package fp.jugador;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.Objects;

import fp.utiles.Checkers;

public class JugadorF {
	private String nombre;
	private LocalDate fechaNacimiento;
	private Integer altura;
	private String nacionalidad;
	
	//Constructor canónico
	public JugadorF(String nombre, LocalDate fechaNacimiento, Integer altura, String nacionalidad) {
		//Checkers antes de asignar
		checkAltura(altura);
		this.nombre = nombre;
		this.fechaNacimiento = fechaNacimiento;
		this.altura = altura;
		this.nacionalidad = nacionalidad;
	}
	
	//Constructor 2
	public JugadorF(String nombre, LocalDate fechaNacimiento) {
		this.nombre = nombre;
		this.fechaNacimiento = fechaNacimiento;
		this.altura = null;
		this.nacionalidad = null;
	}
	
	//Constructor 3
	//"Jugador1, 28/06/1990,190,Española"
	public JugadorF(String s) {
		String[] datos = s.split(","); //"String[] es un Array (una lista pero que no se puede modificar el nºelementos tras crearse"
		//Comprobar nºelementos
		if(datos.length!=4) {
			throw new IllegalArgumentException("Cadena no válida");
		}
		//Parseo de los elementos del CSV
		String nombre = datos[0].trim();
		LocalDate fechaNacimiento = LocalDate.parse(datos[1].trim(), DateTimeFormatter.ofPattern("dd/MM/yyyy"));
		Integer altura = Integer.valueOf(datos[2].trim());
		String nacionalidad = datos[3].trim();
		
		//Checkers antes de asignarç
		//Opción 1: Método privado
		checkAltura(altura);
		
		//Opción 2: Clase Checkers (Poner la condición valida ya que después es if(!condicion)
		Checkers.check("la altura deber ser positiva", altura>=0);
		Checkers.check("La fecha de nacimiento debe" + "ser posterior a 1900", fechaNacimiento.getYear()>1900);
		
		
		
		this.nombre = nombre;
		this.fechaNacimiento = fechaNacimiento;
		this.altura = altura;
		this.nacionalidad = nacionalidad;
		
	}
	
	//Resticciones
	private void checkAltura(Integer altura) {
		if(altura<0) {
			throw new IllegalArgumentException(
				"La altura no puede ser negativa");
		}
	}
	
	//Getters y setters
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}

	public void setFechaNacimiento(LocalDate fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}

	public Integer getAltura() {
		return altura;
	}

	public void setAltura(Integer altura) {
		//Checkers antes de asignar
		checkAltura(altura);
		this.altura = altura;
	}

	public String getNacionalidad() {
		return nacionalidad;
	}

	public void setNacionalidad(String nacionalidad) {
		this.nacionalidad = nacionalidad;
	}
	//Propiedad derivada: Edad a partir de fechaNacimiento
	public Integer getEdad() {
		return fechaNacimiento.until(LocalDate.now()).getYears();
	}

	public String toString() {
		return "JugadorF [nombre=" + nombre + ", fechaNacimiento=" + fechaNacimiento + ", altura=" + altura
				+ ", nacionalidad=" + nacionalidad + "]";
	}

	public int hashCode() {
		return Objects.hash(fechaNacimiento, nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		JugadorF other = (JugadorF) obj;
		return Objects.equals(fechaNacimiento, other.fechaNacimiento) && Objects.equals(nombre, other.nombre);
	}
	public class JugadorT implements Comparable<JugadorF>{
		public int compareTo(JugadorF o) {
			int r = this.getNombre().compareTo(o.getNombre());
			if (r==0) {	r = this.getfechaNacimiento() }
			return 0;
			
		}
	}
}

