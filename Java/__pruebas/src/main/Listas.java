package main;

import java.util.*;

public class Listas {

	public static void main(String[] args) {
		List<Double> temperaturas = new LinkedList<>();
		Integer num = 2;

		System.out.println("Lista original: " + temperaturas);

		temperaturas.add(23.4);
		temperaturas.add(24.6);
		temperaturas.add(25.8);
		System.out.println("Lista mod: " + temperaturas);

		System.out.println("Posicion " + num + " en la lista es: " + temperaturas.get(num));
		
		System.out.println("Longitud de lista = " + temperaturas.size());

	}

}
