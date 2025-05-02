package fp.universidad.tipos;

import java.util.*;

public record Grado(String nombre, Set<Asignatura> obligatorias, Set<Asignatura> optativas, Double minimo_creditos_optativas, Double num_total_creditos) {
	
	public Grado{
		checkMinimoCreditosOptativas();
	}
	
	private void checkMinimoCreditosOptativas() {
		Set<Double> res = new HashSet<>();
		for(Asignatura asignatura: optativas) {
			res.add(asignatura.creditos());
		}
		if(res.size()!=1) {
			throw new IllegalArgumentException("Los créditos optativos de las asignaturas no son los mismos");
		}
		if(minimo_creditos_optativas<0 || minimo_creditos_optativas>num_total_creditos) {
			throw new IllegalArgumentException("minimo de creditos de optativas no válido");
		}
	}

	public String getNombre() {
		return nombre;
	}

	public Set<Asignatura> getObligatorias() {
		return obligatorias;
	}

	public Set<Asignatura> getOptativas() {
		return optativas;
	}

	public Double getMinimoCreditosOptativas() {
		return minimo_creditos_optativas;
	}

	public Double getNumTotalCreditos() {
		return num_total_creditos;
	}

	
	public int hashCode() {
		return nombre.hashCode();
	}
	
	public boolean equals(Object o) {
		if(this==o) return true;
		if(o instanceof Grado) {
			Grado grado = (Grado) o;
			return getNombre().equals(grado.getNombre());
		}
		return false;
	}
	
	public int compareTo(Grado g) {
		Integer res = getNombre().compareTo(g.getNombre());
		return res;
	}
	
	public String toString() {
		return nombre;
	}
	
	
	public Set<Asignatura> getAsignaturas(Integer curso){
		//TODO
		return null;
	}
	
	public Asignatura getAsignatura(String codigo) {
		//TODO
		return null;
	}
}
