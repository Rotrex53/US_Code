package fp.juego;

public class Personaje {
	private String nombre;
	private Integer nivel;
	private Integer vidas;
	
	public Personaje(String nombre, Integer nivel, Integer vidas) {
		setNombre(nombre);
		setNivel(nivel);
		setVidas(vidas);
	}
	
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public String getNombre(){
		return nombre;
	}
	
	public void setNivel(Integer nivel) {
		this.nivel = nivel;
	}
	
	public Integer getNivel() {
		return nivel;
	}
	
	public void setVidas(Integer vidas) {
		this.vidas = vidas;
	}
	
	public Integer getVidas(){
		return vidas;
	}

	private void perderVida(Integer vidas) {
		if(vidas > 0) {
			vidas--;
		}
		throw new IllegalArgumentException("Game Over");
	}
	
	private void vidasExtra(Integer vidasExtra) {
		vidasExtra+=vidas;
	}
	
	public void atacar() {
		System.out.println(getNombre() + "realiza el ataque básico");
	}

	@Override
	public String toString() {
		return getClass().getSimpleName() + "[nombre=" + nombre + ", nivel=" + nivel + ", vidas=" + vidas + "]";
	}
	
	
	
	
}
