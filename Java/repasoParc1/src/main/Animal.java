package main;

public interface Animal {
	//Constantes
	String Reino = "Animal";
	
	//Métodos Abstractos
	Integer getEdad();
	Double getAltura();
	TipoAnimal getTipo();
	String getNombre();
	String hacerSonido();
}
