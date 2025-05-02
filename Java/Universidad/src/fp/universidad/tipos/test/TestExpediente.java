package fp.universidad.tipos.test;

import fp.universidad.tipos.*;

public class TestExpediente {

	public static void main(String[] args) {
		Asignatura asignatura = new Asignatura("FP", "1234567", 12.0, TipoAsignatura.ANUAL, 1);
		Nota nota1 = new Nota(asignatura, 2024, 3.0, TipoNota.PRIMERA);
		Nota nota2 = new Nota(asignatura, 2024, 7.0, TipoNota.PRIMERA);
		
		Expediente expediente = new Expediente();
		expediente.nuevaNota(nota1);
		expediente.nuevaNota(nota2);
		
		System.out.println(expediente);
	}

}
