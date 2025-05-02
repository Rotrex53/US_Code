package fp.universidad.tipos;
import fp.utiles.*;

public record Asignatura (String nombre, String codigo, Double creditos, TipoAsignatura tipo, Integer curso) implements Comparable<Asignatura>{
	//HECHO:
		//Constructor canónico
		//Getters
		//toString, equals, hashcode -> el toString hay que sobrescribirlo para dar nuestras condiciones
	
	//NO HECHO:
		//Propiedades derivadas
		//Restricciones
		//compareTo
	
	
	//TODO: Propiedad derivada: acronimo (significa TO DO [por hacer, no "todo"])
	public String acronimo() {
		return null;
	}
	
	
	//toString, sobre escribirlo
	@Override
	public String toString() {
		return "(" + codigo + ") " + nombre;
	}
	
	
	//Restricciones		OJO no podemos poner setDigitos() y dentro del set poner el check porque los record NO TIENEN getters ni setters
	public Asignatura{
		Checkers.check("Creditos no validos",creditos != null && creditos > 0); //otra forma de definir las restricciones mas rapida
		Checkers.check("Codigo incorrecto", EsCodigoValido(codigo) && codigo.length() == 7);
		Checkers.check("curso no valido", curso >= 1 && curso <= 4);
	}
	
	private boolean EsCodigoValido(String codigo) {
		Boolean res = true;
		
		for(int i = 0; i<codigo.length(); i++) {
			if(!Character.isDigit(codigo.charAt(i))) {
				res = false;
				break;
			}
		}
		return res;
	}
	
	
	//Equals, hashCode, CompareTo
	public int hashCode() {
		return codigo.hashCode();
	}
	
	public boolean equals(Object o) {
		if(this == o) return true;
		if(o instanceof Asignatura) {
			Asignatura asignatura = (Asignatura) o;		//Hemos parseado "o" como asignatura ya que es un tipo Object y lo pasamos a Asignatura
			return this.codigo.equals(asignatura.codigo);	//Son iguales si sus códigos son iguales
		}
		return false;
	}
	
	public int compareTo(Asignatura o) {
		return codigo.compareTo(o.codigo);
	}
}
