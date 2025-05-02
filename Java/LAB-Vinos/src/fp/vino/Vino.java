package fp.vino;

public record Vino(String pais, String region, Integer puntos, Double precio, String uva) {
	
	public Double calidadPrecio(Integer puntos, Double precio) {
		return puntos/precio;
	}
}
