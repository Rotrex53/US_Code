package comparadores;

import java.util.*;

public class ComparadoresTest{
	
	public static void main(String[] args) {
		try {
			//Datos
			
			Comparadores c1 = new Comparadores(1, 3);
			Comparadores c2 = new Comparadores(0, 4);
			Comparadores c3 = new Comparadores(0, 2);
		
			List<Comparadores> lista = new LinkedList<>();
			lista.add(c1);
			lista.add(c2);
			lista.add(c3);
		
			
			//Métodos
			
			//Normal:   Orden por el primer integer y despues el segundo, orden natural de "Comparadores"
			Collections.sort(lista);			
			
			//Comparator independiente:  Orden por el segundo integer (gracias a Comparator)
			Collections.sort(lista, new Comparador2());		
															//OJO: la linea superior es la forma larga (crear un Comparator y despues implementarlo)
			
			//Referencia a método:  Orden por el primer integer unicamente (no importa el segundo)
			Comparator<Comparadores> Comparador3 = Comparator.comparing(Comparadores::getInt1);		//Comparadores::getInt1 --> referencia a método
			Collections.sort(lista, Comparador3);
			
			//Expresión lambda + comparing:  Orden por suma de los integers
			Comparator<Comparadores> Comparador4 = Comparator.comparing(x -> x.getInt1()+x.getInt2());	//aunque tenemos la funcion sumaDatos no se puede usar, hay que poner una expresión lambda
			Collections.sort(lista, Comparador4);		
			
			//Expresión lambda:  Orden por integer1
			Comparator<Comparadores> Comparador5 = (x,y) -> x.getInt1().compareTo(y.getInt1());		//mediante expresiones lambda directamente
			Collections.sort(lista, Comparador5);
			
				//si queremos por un segundo criterio:	orden por integer 2 (si hay empate en integer 1)
			Comparator<Comparadores> Comparador6 = (x,y) -> x.getInt2().compareTo(y.getInt2());		
			Collections.sort(lista, Comparador5.thenComparing(Comparador6));
			
				//con reversed:	OJO: integer 2 en reversed no el primero (si queremos ambos lo sacamos del parentesis)
			Collections.sort(lista, Comparador5.thenComparing(Comparador6.reversed()));
			
			//Aplicar Otros Métodos con comparación
			
			Comparadores maxC = Collections.max(lista, Comparator.comparing(Comparadores::getInt1));
			Comparadores minC = Collections.min(lista, Comparator.comparing(Comparadores::getInt1).thenComparing(Comparadores::getInt2));
			
			
			//Output
			
//			System.out.println(c1.compareTo(c2));
			System.out.println(lista);
			System.out.println(maxC);
			System.out.println(minC);
		}
		
		catch(Exception e) {
			System.out.println(e);
		}
		


	}
}
