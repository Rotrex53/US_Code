package fp.universidad.tipos;
import java.util.*;
import fp.utiles.Checkers;

public class Expediente {
	private List<Nota> notas;
	
	public Expediente () {
		notas = new ArrayList<Nota>();
	}

	public List<Nota> getNotas() {
		return notas;
	}

	@Override
	public int hashCode() {
		return Objects.hash(notas);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Expediente other = (Expediente) obj;
		return Objects.equals(notas, other.notas);
	}
	
	public String toString() {
		return getNotas().toString();
	}
	
	public void nuevaNota(Nota n) {
		if(notas.contains(n)) {
			notas.remove(n);
		}
		else {
			Checkers.check("un alumno no se puede presentar a mas de 2 convocatorias por curso", contarConvocatoriasCurso(n)<=2);
		}
		notas.add(n);
	}

	private Integer contarConvocatoriasCurso(Nota n) {
		Integer contador = 0;
		
		for(Nota nota: notas) {
			if(nota.cursoAcademico().equals(n.cursoAcademico()) && nota.asignatura().equals(n.asignatura())) {
				contador++;
			}
		}
		return contador;
	}
	
	public Double getNotaMedia() {
		Double res = 0.0;
		Integer numNotas = 0;
		for (Nota nota: notas) {
			if (nota.valorNumerico()>=5) {
				res += nota.valorNumerico();
				numNotas++;
			}
		}
		if(numNotas != 0) {
			return res/numNotas;
		}
		return res;
	}
	
}
