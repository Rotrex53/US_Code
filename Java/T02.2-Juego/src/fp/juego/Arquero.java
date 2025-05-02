package fp.juego;

public class Arquero extends Personaje {
	private Integer precision;

	public Arquero(String nombre, Integer nivel, Integer vidas, Integer precision) {
		super(nombre, nivel, vidas);
		this.precision = precision;
	}
	
	public Integer getPrecision() {
		return precision;
	}

	public String toString() {
		return getClass() + ": " + "nombre=" + getNombre() + ", nivel=" + getNivel() + ", numVidas=" + getVidas() + ", precision=" + getPrecision();
	}
	
}
