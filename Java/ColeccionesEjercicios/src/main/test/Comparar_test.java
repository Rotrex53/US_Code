package main.test;

import java.util.*; import main.Comparar;

public class Comparar_test {

	public static void main(String[] args) {
		List<Comparar> lista = new ArrayList<Comparar>();
		
		Comparar c1 = new Comparar("Fran",22);
		Comparar c2 = new Comparar("Pepe",23);
		Comparar c3 = new Comparar("Jose",24);
		
		lista.add(c3);
		lista.add(c1);
		lista.add(c2);
		System.out.println(lista);
		
		Comparator<Comparar> cmp = Comparator.comparingInt(Comparar::edad);
		Collections.sort(lista, cmp);
		
		System.out.println(lista);
		
	}
}
