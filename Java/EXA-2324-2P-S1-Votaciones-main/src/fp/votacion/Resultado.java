package fp.votacion;

public record Resultado(String Partido, Double Porcentaje) {
	
	
	public String getPartido() {
		return  Partido;
	}
	
	public Double getPorcentaje() {
		return Porcentaje;
	}
	
	
	public Resultado{
		checkPorcentaje(Porcentaje);
	}

	private void checkPorcentaje(Double porcentaje) {
		if(porcentaje<0) {
			throw new IllegalArgumentException("El porcentaje tiene que ser positivo");
		}
	}
}
