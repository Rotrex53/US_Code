package fp.universidad.tipos.test;

import fp.universidad.tipos.*;

public class TestNota {

	public static void main(String[] args) {
		try {
			Asignatura asignatura = new Asignatura("Fundamentos de Programación(Python)","0000230",6.,TipoAsignatura.ANUAL,1);
			Nota n1 = new Nota(asignatura, 2012, 9.4, TipoNota.PRIMERA, false);
			Nota n2 = new Nota(asignatura, 2012, 9.4, TipoNota.SEGUNDA, false);
			
//			System.out.println(n1);
//			System.out.println(n1.getCalificacion(10.));
//			System.out.println(n1.getCurso(2014));	OJO QUE HAY QUE ARREGLAR EL AÑO
//			System.out.println(n1.hashCode());
//			System.out.println(n1.equals(n2));
			System.out.println(n1.compareTo(n2));
			System.out.println(n1);
		}
		catch(Exception e) {
			System.out.println(e);
		}

	}

}
