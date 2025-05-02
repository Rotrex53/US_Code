package fp.universidad.tipos;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

import fp.utiles.Checkers;

public class Persona {
	//Atributos -> Siempre privados
	private String dni;
	private String nombre;
	private String apellidos;
	private LocalDate fechaNacimiento;
	private String email;
	
	//Metodos
		//Constructor -> Siempre público llamado igual que la clase
	//Constructor canónico
	public Persona(String dni, String nombre, String apellidos, LocalDate fechaNacimiento, String email) {
		//Asignaciones
		setDni(dni);
		setNombre(nombre);
		setApellidos(apellidos);
		setFechaNacimiento(fechaNacimiento);
		setEmail(email);
		
		
	}
		//Constructor 2
	public Persona(String dni, String nombre, String apellidos, LocalDate fechaNacimiento) {
		//Asignaciones
		this(dni, nombre, apellidos, fechaNacimiento, ""); //Llamando al constructor canónico y ahorro código
		
		//TODO: Restricciones
	}
	
	
	//Getters & Setters
	public String getDni() {
		return dni;
	}
	public void setDni(String dni) {
		Checkers.check("Dni formato inválido", dni.length() == 9 && EsDNIValido(dni));
		this.dni = dni;
	}
	private boolean EsDNIValido(String dni) {
		Boolean res = true;
		
		for(int i = 0; i<(dni.length() - 1); i++) {
			if(!Character.isDigit(dni.charAt(i))) {
				res = false;
				break;
			}
		}
		
		for(int i = 8; i==dni.length(); i++) {
			if(!Character.isAlphabetic(dni.charAt(i))) {
				res = false;
				break;
			}
		}
		return res;
	}
	
	
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	
	public String getApellidos() {
		return apellidos;
	}
	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}
	
	
	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}
	public void setFechaNacimiento(LocalDate fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}
	
	
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		Checkers.check("Email formato incorrecto", email.isEmpty() || email.contains("@"));
		this.email = email;
	}
	
	//propiedad derivada: edad
	public Integer getEdad() {
		return Period.between(fechaNacimiento, LocalDate.now()).getYears();
	}
	
	
	//toString
	//"28864657W – García Vaquero, Pascual – 15/09/1998"
	public String toString() {
		return dni + " - " + apellidos + ", " + nombre + " - " + fechaNacimiento.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));
	}
	
	
	//compareTo, equals, hashcode
	public int hashCode() {
		return getDni().hashCode() + 31*getNombre().hashCode() + 31*31*getApellidos().hashCode();
	}
	
	public boolean equals(Object o) {
		if(this == o) return true;
		if(o instanceof Persona) {
			Persona persona = (Persona) o;		//Hemos parseado "o" como asignatura ya que es un tipo Object y lo pasamos a Asignatura
			return getDni().equals(persona.getDni()) && getNombre().equals(persona.getNombre()) && getApellidos().equals(persona.getApellidos());	//Son iguales si sus códigos son iguales
		}
		return false;
	}
	
	public int compareTo(Persona o) {
		int res = getApellidos().compareTo(o.getApellidos());
		
		if(res == 0) {
			res = getNombre().compareTo(o.getNombre());
			
			if(res == 0) {
				res = getDni().compareTo(o.getDni());
			}
		}
		return res;
	}
}
