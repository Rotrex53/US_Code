package fp;

public class Perro implements Animal{
	
	// Atributos (SIEMPRE SON PRIVADOS)
	private String raza;
	private Color color;
	private Integer edad;
	
	// Métodos:
	
	// Constructor
	public Perro
	(String raza, Color color, Integer edad) {
		this.raza = raza;
		this.color = color;
		this.edad = edad;
	}
	
	// Getters and setters
	// Getter: consulta
	public String getRaza() {
		return this.raza;
	}
	
	// Setter: modificación
	public void setRaza(String raza) {
		this.raza = raza;
	}

	public Color getColor() {
		return color;
	}

	public void setColor(Color color) {
		this.color = color;
	}

	public Integer getEdad() {
		return edad;
	}

	@Override
	public String toString() {
		return 
				"Perro [raza=" + raza + ", color=" 
				+ color + ", edad=" + edad + "]";
	}

	@Override
	public void correr() {
		// TODO Auto-generated method stub
		System.out.println("Correr");
	}
	
	
	
	// toString, equals, hashCode
}
