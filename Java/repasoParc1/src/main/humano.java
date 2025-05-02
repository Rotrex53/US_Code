package main;

public class humano implements Animal{
	private Integer edad;
	private Double altura;
	private TipoAnimal tipo;
	private String nombre;
	private String palabras;
	
	public humano(Integer edad, Double altura, TipoAnimal tipo, String nombre, String palabras) {
		CheckTipo(tipo);
		setEdad(edad);
		setAltura(altura);
		setNombre(nombre);
		setPalabras(palabras);
		
	}
	
	public void CheckTipo(TipoAnimal tipo) {
		if(tipo != TipoAnimal.mamiferos) {
			throw new IllegalArgumentException("Tipo no compatible");
		}
	}

	public Integer getEdad() {
		return edad;
	}

	public void setEdad(Integer edad) {
		CheckEdad(edad);
		this.edad = edad;
	}

	private void CheckEdad(Integer edad) {
		if(edad < 0) {
			throw new IllegalArgumentException("Edad no compatible");
		}
	}

	public Double getAltura() {
		return altura;
	}

	public void setAltura(Double altura) {
		CheckAltura(altura);
		this.altura = altura;
	}
	
	private void CheckAltura(Double altura) {
		if(altura < 0.0) {
			throw new IllegalArgumentException("Altura no compatible");
		}
	}

	public TipoAnimal getTipo() {
		return tipo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		CheckNombre(nombre);
		this.nombre = nombre;
	}

	private void CheckNombre(String nombre) {
		if(!nombre.matches("[a-zA-Z]+")) {
			throw new IllegalArgumentException("Nombre no compatible");
		}
	}
	
	public void setPalabras(String palabras) {
		this.palabras = palabras;
	}
	
	public String getPalabras() {
		return palabras;
	}

	public String hacerSonido() {
		// TODO Auto-generated method stub
		return getPalabras();
	}
	
	
}
