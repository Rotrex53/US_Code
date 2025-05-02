package fp.universidad.tipos;

import java.time.*;
import java.util.*;
import fp.utiles.Checkers;

public class Alumno extends Persona{
	private Set<Asignatura> asignaturas;
	private Expediente expediente;
	
	public Alumno(String dni, String nombre, String apellidos, LocalDate fechaNacimiento, String email) {
		super(dni, nombre, apellidos, fechaNacimiento, email);
		setEmail(email);
		
		this.asignaturas = new HashSet<Asignatura>();
		this.expediente = new Expediente();
		
	}
	
	@Override
	public void setEmail(String email) {
		Checkers.check("email no válido", !email.isEmpty() && email.endsWith("@alum.us.es"));
		super.setEmail(email);
	}

	public Set<Asignatura> getAsignaturas() {
		return asignaturas;
	}

	public Expediente getExpediente() {
		return expediente;
	}
	
	//El equals y el compareTo son EL MISMO que el de persona que esta siendo HEREDADO por lo que no se implementa
	
	public void matriculaAsignatura(Asignatura a) {
		Checkers.check("ya esta matriculado en esa asignatura", !estaMatriculado(a));	//Por comprobar pero no haria falta
		asignaturas.add(a);
	}

	private boolean estaMatriculado(Asignatura a) {
		return asignaturas.contains(a);
	}
	
	public void eliminaAsignatura(Asignatura a) {
		Checkers.check("no esta matriculado en esta asignatura", !estaMatriculado(a));	//Por comprobar pero no haria falta
		asignaturas.remove(a);
	}
	
	public void evaluaAsignatura(Asignatura a, Integer curso, TipoNota convocatoria, Double nota, Boolean esMatricula) {
		Checkers.check("el alumno no esta matriculado en la asignatura", estaMatriculado(a));
		expediente.nuevaNota(new Nota(a, curso, nota,  convocatoria, esMatricula));
	}
	
	public Integer getCurso() {
		//TODO
		return null;
	}
	
	public String toString() {
		return "(" + "?" + "º)" + super.toString();
	}
	
}
