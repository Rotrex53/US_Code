package fp.juego;

public class Mago extends Personaje {
	private Integer mana;

	public Mago(String nombre, Integer nivel, Integer vidas, Integer mana) {
		super(nombre, nivel, vidas);
		this.mana = mana;
	}
	
	public Integer getMana() {
		return mana;
	}
	
	public String toString() {
		return getClass() + ": " + "nombre=" + getNombre() + ", nivel=" + getNivel() + ", numVidas=" + getVidas() + ", mana=" + getMana();
	}

}
