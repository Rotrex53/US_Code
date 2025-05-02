package main.test;

import main.*;

public class Animales_test {

	public static void main(String[] args) {
		humano persona1 = new humano(12, 1.40, TipoAnimal.mamiferos, "Juan", "Hola me llamo Juan");
		
		System.out.println(persona1.getNombre());
	}

}
