package fp.universidad.tipos;

import java.util.*;

import fp.utiles.Checkers;

public class Despacho extends Espacio{
	private Set<Profesor> profesores;
	
	public Despacho(String nombre, Integer capacidad, Set<Profesor> profesores) {
		super(TipoEspacio.OTRO, nombre, capacidad);
		checkNumProfesores(profesores, capacidad);
		checkTipo(getTipo());
		this.profesores = new HashSet<>(profesores);
	}
	
	public Despacho(String nombre, Integer capacidad, Profesor p) {
		super(TipoEspacio.OTRO, nombre, capacidad);
		checkNumProfesores(profesores, capacidad);
		checkTipo(getTipo());
		this.profesores = new HashSet<>(); //size = 1 (Hacer Checker)
		this.profesores.add(p);
	}
	
	public Despacho(TipoEspacio tipo, String nombre, Integer capacidad) {
		super(TipoEspacio.OTRO, nombre, capacidad);
		checkNumProfesores(profesores, capacidad);
		checkTipo(getTipo());
		this.profesores = new HashSet<>();
	}
	
	public Despacho(String c) {
		super(c);
	}
	
	
	private void checkNumProfesores(Set<Profesor> profesores, Integer capacidad) {
		Integer NumProfesores = profesores.size();
		if(NumProfesores>capacidad) {
			throw new IllegalArgumentException("Aforo superado");
		}
	}
	
	private void checkTipo(TipoEspacio tipo) {
		if(tipo != TipoEspacio.OTRO) {
			throw new IllegalArgumentException("Tipo no válido");
		}
	}
	
	
	public void setTipo(TipoEspacio tipo) {
		throw new IllegalArgumentException("Operación no válida");
	}
	
	public Set<Profesor> getProfesores() {
		return profesores;
	}

	public void setProfesores(Set<Profesor> profesores) {
		this.profesores = profesores;
	}
	
	
	public int hashCode() {
		return getNombre().hashCode() + getPlanta().hashCode();
	}
	
	public boolean equals(Object o) {
		if(this==o) return true;
		if(o instanceof Despacho) {
			Despacho despacho = (Despacho) o;
			return getNombre().equals(despacho.getNombre()) && getPlanta().equals(despacho.getPlanta());
		}
		return false;
	}
	
	public String toString() {
		return super.toString() + profesores.toString();
	}
}
