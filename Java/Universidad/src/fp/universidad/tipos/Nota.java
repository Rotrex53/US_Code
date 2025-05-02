package fp.universidad.tipos;
import fp.utiles.*;

public record Nota(Asignatura asignatura, Integer cursoAcademico, Double valorNumerico, 
		TipoNota convocatoria, Boolean matriculaHonor)  {
	
	//Constructor 2:
	public Nota(Asignatura asignatura, Integer cursoAcademico,Double valorNumerico, TipoNota convocatoria ) {
		this(asignatura, cursoAcademico, valorNumerico, convocatoria, false);
	}
	
	
	public Nota{
		Checkers.check("Valor numérico no valido", valorNumerico >= 0 && valorNumerico <= 10);
		Checkers.check("Matrícula no vinculable", matriculaValida(valorNumerico, matriculaHonor));
	}
	private boolean matriculaValida(Double valorNumerico, Boolean matriculaHonor) {
		Boolean res = true;
		if(matriculaHonor == true) {
			if(!(valorNumerico >= 9)) {
				res = false;
			}
		}
		return res;
	}
	
	
	//Propiedad derivada
	//Calificacion
	public String getCalificacion(Double valorNumerico) {
		String calificacion = null;
		if(valorNumerico<5) {
			calificacion = "SUSPENSO";}
		else if(valorNumerico<7 && valorNumerico>=5) {
			calificacion = "APROBADO";}
		else if(valorNumerico>=7 && valorNumerico<9) {
			calificacion = "NOTABLE";}
		else if(valorNumerico>=9 && matriculaHonor == false) {
			calificacion = "SOBRESALIENTE";	}
		else {calificacion = "MATRICULA DE HONOR";	}
		return calificacion;
	}
	
	//Curso Académico:
	public String getCurso(Integer cursoAcademico) {
		String curso = cursoAcademico + "-" + (cursoAcademico + 1); //Integer.sum(cursoAcademico, 1)
		return curso ;
	}

	
	@Override
	public String toString() {
		
		return asignatura + ", " +  getCurso(cursoAcademico) + ", " + convocatoria + ", " + valorNumerico + ", " + getCalificacion(valorNumerico);
	}
	
	
	public int hashCode() {
		return cursoAcademico.hashCode() + 31*asignatura.hashCode() + 31*31*convocatoria.hashCode();
	}
	
	
	public boolean equals(Object o) {
		if(this == o) return true;
		if(o instanceof Nota) {
			Nota nota = (Nota) o;
			return cursoAcademico.equals(nota.cursoAcademico) && asignatura.equals(nota.asignatura) && convocatoria.equals(nota.convocatoria);
		}
		return false;
	}
	
	
	public int compareTo(Nota o) {
		int res = cursoAcademico.compareTo(o.cursoAcademico);
		if(res == 0) {
			res = asignatura.compareTo(o.asignatura);
			if(res == 0) {
				res = convocatoria.compareTo(o.convocatoria);
			}
		}
		return res;
	}
}