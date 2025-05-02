//RECORDATORIO: al crear la clase hay que marcar la opcion: main(String[] args)

package fp.universidad.tipos.test;

import fp.universidad.tipos.Asignatura;
import fp.universidad.tipos.TipoAsignatura;

public class TestAsignatura {

	
	
	public static void main(String[] args) {
		try {
			Asignatura fp1 = new Asignatura("Fundamentos de Programación(Python)","0000230",6.,TipoAsignatura.ANUAL,1);
			Asignatura fp2 = new Asignatura("Fundamentos de Programación(Java)","0000230",6.,TipoAsignatura.ANUAL,1);
			Asignatura falso1 = new Asignatura("a", "1234567",13.,TipoAsignatura.ANUAL,4);
			
			System.out.println(fp1.equals(fp2));
			System.out.println(fp1.equals(falso1));
			System.out.println(fp1);
			System.out.println(fp1.codigo());
			System.out.println(fp1.creditos());
		}
		
		catch(Exception e){
			System.out.println(e);
		}
		
		
	}
}