package fp.burger;

public record Evaluacion(String hamburgueseria, Integer presentacion, 
		Integer ptoDeCarne, Integer calidadIngredientes, Integer calidadPan) {
	public Double getPuntuacionFinal() {
		return (presentacion + ptoDeCarne + calidadIngredientes + calidadPan)/4.;
	}
	
	public Evaluacion{
		checkPuntuaciones(presentacion, ptoDeCarne, calidadIngredientes, calidadPan);
	}

	private void checkPuntuaciones(Integer presentacion, Integer ptoDeCarne, Integer calidadIngredientes,
			Integer calidadPan) {
		if(presentacion<0 || presentacion>10) {
			throw new IllegalArgumentException("la puntuación no puede estar fuera del rango [0,10]");
		}if(ptoDeCarne<0 || ptoDeCarne>10) {
			throw new IllegalArgumentException("la puntuación no puede estar fuera del rango [0,10]");
		}if(calidadIngredientes<0 || calidadIngredientes>10) {
			throw new IllegalArgumentException("la puntuación no puede estar fuera del rango [0,10]");
		}if(calidadPan<0 || calidadPan>10) {
			throw new IllegalArgumentException("la puntuación no puede estar fuera del rango [0,10]");
		}
		
	}
}
