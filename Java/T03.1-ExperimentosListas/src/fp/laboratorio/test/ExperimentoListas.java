package fp.laboratorio.test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

import fp.laboratorio.Estudiante;
import fp.laboratorio.EstudianteImpl;

public class ExperimentoListas {

	public static void main(String[] args) {

		Estudiante e1 = new EstudianteImpl("Ada", "Lovelace", "adalov");
		Estudiante e2 = new EstudianteImpl("Grace", "Murray", "gramur");
		Estudiante e3 = new EstudianteImpl("Frances", "Allen", "fraall");
		Estudiante e4 = new EstudianteImpl("Hedy", "Lamarr", "hedlam");
		Estudiante e5 = new EstudianteImpl("Radia", "Perlman", "ritper");
		Estudiante e6 = new EstudianteImpl("Margaret", "Hamilton", "marham");

		// Crea una lista vacía de estudiantes
		// Creando una lista a partir del constructor por defecto (el que no tiene
		// parametros) (escogemos)
		List<Estudiante> lista = new ArrayList<>();

		List<Estudiante> lista2 = new LinkedList<>();

		// Añade 5 estudiantes (e1-e5) a la lista
		lista.add(e1);
		lista.add(e2);
		lista.add(e3);
		lista.add(e4);
		lista.add(e5);

		// Visualiza el nmero de estudiantes que tiene la lista
		System.out.println("Número de estudiantes: " + lista.size());

		// Visualiza los estudiantes de las posiciones 0, 1 y 5.
		try {
			System.out.println("Estudiante0: " + lista.get(0));
			System.out.println("Estudiante1: " + lista.get(1));
			System.out.println("Estudiante5: " + lista.get(5)); // OJO: el indice del estudiante 5 es el nº4
		} catch (IndexOutOfBoundsException e) {
			System.out.println("Capturada excepcion: " + e.getMessage());
		}
		// Visualiza, de los estudiantes 2 y 4 solo su uvus.
		System.out.println("Estudiante2: " + lista.get(2).getUVUS());
		System.out.println("Estudiante4: " + lista.get(4).getUVUS());

		// Inserta el estudiante e6 como tercer estudiante de la lista
		lista.add(2, e6);
		mostrarLista(lista);

		// Busca la posición de la estudiante que se llama Frances Allen.
		Integer indx = lista.indexOf("Frances Allen");
		System.out.println("La posición de Frances es: " + indx);
		System.out.println("=======================");
		indx = buscarIndiceEstudiante(lista, "Frances", "Allen");
		System.out.println("La posición de Frances es: " + indx);
		System.out.println("=======================");

		// Obten una sublista con los estudiantes de la posici�n 1 a la 4.
		List<Estudiante> sublista =  lista.subList(1, 5);
		System.out.println("La sublista desde la posicion 1 a la 4 es: " + sublista);
		System.out.println("=======================");

		// Visualiza ambas listas
		System.out.println(lista);
		System.out.println("=======================");
		System.out.println(sublista);
		System.out.println("=======================");
		mostrarLista(lista);
		System.out.println("=======================");
		mostrarLista(sublista);
		System.out.println("=======================");

		// Elimina de la sublista el segundo estudiante (�ndice 1).
		sublista.remove(1);
		mostrarLista(sublista);
		System.out.println("=======================");
		mostrarLista(lista);
		System.out.println("=======================");

		// Muestra ambas listas.

		// Muestras ambas listas, pero haciendo que haya un estudiante por línea.

	}

	

	private static void mostrarLista(List<Estudiante> lista) {
		for(Estudiante e: lista) {
			System.out.println("\t>>>" + e);
		}
	}



	private static Integer buscarIndiceEstudiante(List<Estudiante> estudiantes, String nombre, String apellidos) {
		Integer res = -1;
		for (int i = 0; i<estudiantes.size() ;i++ ) {
			//filtro
			Estudiante e = estudiantes.get(i);
			if (e.getNombre().equals(nombre) && e.getApellidos().equals(apellidos));{
				res = i;
				break;
			}
		}
		return res;
	}



	private static void mostrarIterable(Iterable<Estudiante> lista) {
		for (Estudiante e : lista) {
			System.out.println(e);
		}
	}

	public static Integer buscarEstudiantePorNombreyApellidos(List<Estudiante> lista, String nombre, String apellidos) {
		int pos = -1;
		for (int i = 0; i < lista.size(); i++) {
			Estudiante e = lista.get(i);
			if (e.getNombre().equals(nombre) && e.getApellidos().equals(apellidos)) {
				pos = i;
				break;
			}
		}
		return pos;
	}

}
