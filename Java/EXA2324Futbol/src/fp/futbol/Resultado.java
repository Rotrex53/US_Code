package fp.futbol;

public record Resultado(Integer minuto, Integer golesLocal, Integer golesVisitante) {
	public Resultado{
		checkMinutos(minuto);
		checkGolesLocal(golesLocal);
		checkGolesVisitante(golesVisitante);
	}

	private void checkGolesVisitante(Integer golesVisitante) {
		if(golesVisitante<0) {
			throw new IllegalArgumentException("Los goles visitantes tienen que ser mayores o iguales a 0");
		}
		
	}

	private void checkGolesLocal(Integer golesLocal) {
		if(golesLocal<0) {
			throw new IllegalArgumentException("Los goles locales tienen que ser mayores o iguales a 0");
		}		
	}

	private void checkMinutos(Integer minuto) {
		if(minuto<0) {
			throw new IllegalArgumentException("Los minutos tienen que ser mayores o iguales a 0");
		}
		
	}
}
