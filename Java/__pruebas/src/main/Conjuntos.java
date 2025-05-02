package main;

import java.util.*;

public class Conjuntos {

	public static void main(String[] args) {
		Set<Character> letras = new HashSet<>();
		
		letras.add('A');
		letras.add('V');
		letras.add('U');

		System.out.println(letras.contains('V'));
		
		SortedSet<Character> letrasOrden = new TreeSet<>();
		
		letrasOrden.add('A');
		letrasOrden.add('V');
		letrasOrden.add('U');
		System.out.println(letrasOrden);

		System.out.println(letrasOrden.contains('V'));
		System.out.println(letrasOrden.getFirst());
		
		letrasOrden.add('V');
		System.out.println(letrasOrden);

	}

}
