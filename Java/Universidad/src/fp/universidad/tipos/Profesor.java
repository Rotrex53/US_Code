package fp.universidad.tipos;

import java.time.*;
import java.util.*;

public class Profesor extends Persona{
	private TipoCategoria categoria;
	private ArrayList<Tutoria> tutorias;
	
	public Profesor(String dni, String nombre, String apellidos, LocalDate fechaNacimiento, String email) {
		super(dni, nombre, apellidos, fechaNacimiento, email);
		checkEdad(fechaNacimiento);
		setCategoria(categoria);
		setTutorias(tutorias);
	}
	
	private void checkEdad(LocalDate fechaNacimiento) {
		LocalDate hoy = LocalDate.now();
		Integer edad = Period.between(fechaNacimiento, hoy).getYears();
		if(edad<18) {
			throw new IllegalArgumentException("Es menor de edad, edad no válida");
		}
	}

	public TipoCategoria getCategoria() {
		return categoria;
	}

	public void setCategoria(TipoCategoria categoria) {
		this.categoria = categoria;
	}

	public ArrayList<Tutoria> getTutorias() {
		return tutorias;
	}

	public void setTutorias(ArrayList<Tutoria> tutorias) {
		this.tutorias = null;
	}
	
	
	public int hashCode() {
		return getDni().hashCode() + 31*getNombre().hashCode() + 31*31*getApellidos().hashCode();
	}
	
	public boolean equals(Object o) {
		if(this == o) return true;
		if(o instanceof Profesor) {
			Profesor profesor = (Profesor) o;
			return getDni().equals(profesor.getDni()) && getNombre().equals(profesor.getNombre()) && getApellidos().equals(profesor.getApellidos());
		}
		return false;
	}
	
	public String toString() {
		return " (" + getCategoria() + ") ";
	}
	
	
	public void nuevaTutoria(LocalTime hora_comienzo, Duration duracion, DayOfWeek dia_semana) {
		LocalTime hora_fin = hora_comienzo.plus(duracion);
		String dia_string = dia_semana.toString();
		Tutoria tutoria = new Tutoria(dia_string, hora_comienzo, hora_fin);
		tutorias.add(tutoria);
	}
	
	public void borraTutoria(LocalTime hora_comienzo, Duration duracion, DayOfWeek dia_semana) {
		LocalTime hora_fin = hora_comienzo.plus(duracion);
		String dia_string = dia_semana.toString();
		
		for(int i = 0; i<tutorias.size(); i++) {
			Tutoria tutoria = tutorias.get(i);
			
			if(hora_comienzo != tutoria.hora_comienzo() || 
					hora_fin != tutoria.hora_fin() || 
					dia_string != tutoria.dia_semana()) {
				break;
			}
			
			else {
				tutorias.remove(i);
			}
		}
	}
	
	public void borraTutorias() {
		tutorias.removeAll(tutorias);
	}
	
}
