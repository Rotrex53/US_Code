package fp.examenes;

public record Aula(String nombre, Integer capacidad) {
	public Aula{
		checkNombre(nombre);
		checkCapacidad(capacidad);
	}

	private void checkCapacidad(Integer capacidad) {
		if(capacidad<=0) {
			throw new IllegalArgumentException("La capacidad debe ser mayor que 0");
		}
		
	}

	private void checkNombre(String nombre) {
		if(!Character.isLetter(nombre.charAt(0))) {
			throw new IllegalArgumentException("El nombre debe comenzar por una letra");
		}
		
	}
	
	
}
