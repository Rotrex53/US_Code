package fp;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Objects;

import fp.utiles.Checkers;

// Criterio de orden natural -> implements Comparable<T>
public class Jugador implements Comparable<Jugador> {
	
	// Atributos (siempre private)
	private String nombre;
	private LocalDate fechaNacimiento;
	private Integer altura;
	private String nacionalidad;
	
	// Métodos
	// Constructor canónico
		public Jugador(String nombre,
			LocalDate fechaNacimiento,
			Integer altura,
			String nacionalidad) {
		// Checkers van antes de asignaciones
		// Opción 1: Método privado
		checkAltura(altura);
		
		// Opción 2: Clase Checkers
		// Compración de no nulo
		Checkers.checkNoNull(nombre,
				altura,fechaNacimiento,nacionalidad);
		
		// (Siempre poner la condición positiva, valores válidos)
		Checkers.check("La altura debe ser positiva",
				altura >=0);
		Checkers.check("La fecha de nacimiento debe"
				+ "ser posterior a 1900", 
				fechaNacimiento.getYear()>1900);
		Checkers.check("El nombre no esté vacío", 
				!nombre.equals(""));
		
		
		
		
		
		
		
		// Al atributo 
		// le asigno el valor del parámetro
		this.nombre = nombre;
		this.fechaNacimiento = fechaNacimiento;
		this.altura = altura;
		this.nacionalidad = nacionalidad;
		
		
		
	}
	
	// Constructor 2
	public Jugador(String nombre,
			LocalDate fechaNacimiento) {
		this.nombre = nombre;
		this.fechaNacimiento = fechaNacimiento;
		this.altura = null;
		this.nacionalidad = null;
	}
	
	// Constructor 3
	// "Jugador1,28/06/1990,190,Española"
	public Jugador(String s) {
		String[] datos = s.split(",");
		// Comprobar número de elementos
		if(datos.length!=4) {
			throw new IllegalArgumentException
			("Cadena con formato no válido");
		}
		
		String nombre = datos[0].trim();
		LocalDate fechaNacimiento =
			LocalDate.parse(datos[1].trim(),
			DateTimeFormatter.
			ofPattern("dd/MM/yyyy"));
		Integer altura = Integer.valueOf(
				datos[2].trim());
		String nacionalidad = datos[3].trim();
		
		
		checkAltura(altura);
		this.nombre = nombre;
		this.fechaNacimiento = fechaNacimiento;
		this.altura = altura;
		this.nacionalidad = nacionalidad;
		
		
	}
	
	
	// Restricciones
	private void checkAltura(Integer altura) {
		if(altura<0) {
			throw new 
			IllegalArgumentException(
			"La altura no puede ser negativa");
		}
	}
	
	// Getters y setters
	public String getNombre() {
		return this.nombre;
	}
	
	public void setNombre(String nuevoNombre) {
		this.nombre = nuevoNombre;
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
		checkAltura(altura);
		this.altura = altura;
	}

	public String getNacionalidad() {
		return nacionalidad;
	}

	public void setNacionalidad(String nacionalidad) {
		this.nacionalidad = nacionalidad;
	}
	
	
	// Propiedad derivada
	// Edad
	public Integer getEdad() {
		return fechaNacimiento
				.until(LocalDate.now())
				.getYears();
	}

	public String toString() {
		return "Jugador [nombre=" + nombre + ", fechaNacimiento=" + fechaNacimiento + ", altura=" + altura
				+ ", nacionalidad=" + nacionalidad + "]";
	}

	@Override
	public int hashCode() {
		return Objects.hash(fechaNacimiento, nombre);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Jugador other = (Jugador) obj;
		return Objects.equals(this.fechaNacimiento, 
				other.fechaNacimiento) 
				&& 
				Objects.equals(this.nombre, 
						other.nombre);
	}

	@Override
	public int compareTo(Jugador o) {
		int r = this.getNombre().compareTo(o.getNombre());
		if(r==0) {
			r = this.getFechaNacimiento().compareTo(o.getFechaNacimiento());
		}
		return r;
	}
	
}
