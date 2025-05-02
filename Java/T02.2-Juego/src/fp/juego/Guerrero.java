package fp.juego;

public class Guerrero extends Personaje {
	private Integer fuerza;

	public Guerrero(String nombre, Integer nivel, Integer vidas, Integer fuerza) {
		super(nombre, nivel, vidas);
		this.fuerza = fuerza;
	}
	
	public Integer getFuerza() {
		return fuerza;
	}
	
	public String toString() {
		return getClass() + ": " + "nombre=" + getNombre() + ", nivel=" + getNivel() + ", numVidas=" + getVidas() + ", fuerza=" + getFuerza();
	}
	
}
