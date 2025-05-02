package fp.lexico.test;

import java.nio.charset.StandardCharsets;
import java.util.*;
import fp.lexico.*;

public class TestLexico {

	public static void main(String[] args) {
		LectorTexto lector1 = new LectorTexto();
		lector1.agregaFichero("./res/lazarillo.txt", StandardCharsets.UTF_8);
		System.out.println("LECTOR 1");
		System.out.println(lector1.getPalabras().subList(0, 100));
	
		LectorTexto lector2 = new LectorTexto();
		System.out.println("LECTOR 2");
		lector2.agregaFichero("./res/platero.txt", StandardCharsets.UTF_8);
		System.out.println(lector2.getPalabras().subList(0,100)+ "\n");
		
			List<String> palabras1 = Arrays.asList("patata", "abuelo", "agua", "hermano");
			Lexico conj1 = new Lexico(palabras1);
		
			List<String> palabras2 = Arrays.asList("patata", "padre", "fanta", "hermano", "piedra");
			Lexico conj2 = new Lexico(palabras2);
		
		System.out.println("Palabras 1: " + conj1.getPalabras() + "\n");
		System.out.println("Palabras 2: " + conj2.getPalabras() + "\n");
		System.out.println("Palabras comunes: " + conj1.getPalabrasComunes(conj2) + "\n");
		System.out.println("Total palabras 1: " + conj1.getTotalPalabras() + "\n");
		System.out.println("Total palabras 2: " + conj2.getTotalPalabras() + "\n");
		System.out.println("Palabras no incluidas en la base de datos: " + conj1.getDiferenciaPalabras(conj2) + "\n");
	}

}