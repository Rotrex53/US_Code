package stream;

import java.util.*;
import java.util.function.Consumer;
import java.util.stream.Collectors;

public class StreamTest {

	public static void main(String[] args) {
		//Datos
		
		Stream s1 = new Stream(10, 1.40, "Pepe", "49112343E");
		Stream s2 = new Stream(11, 1.50, "María", "49113570E");
		Stream s3 = new Stream(12, 1.60, "Paola", "49111300E");
		Stream s4 = new Stream(13, 1.70, "Manuel", "49118090E");
		Stream s5 = new Stream(14, 1.80, "Ricardo", "49115020E");
		
		List<Stream> lista = new ArrayList<>();
		lista.add(s5);
		lista.add(s4);
		lista.add(s3);
		lista.add(s2);
		lista.add(s1);
		List<Stream> listaVacia = new ArrayList<>();
		Streams listaStreams = new Streams(lista);
		Streams listaStrVacia = new Streams(listaVacia);
		
		Consumer<Stream> cambiar = listaStreams.cambioDNI("00000000A");
		
		
		//Metodos
		
		
		
		
		//Output
//		System.out.println(listaStreams);
//		System.out.println(s1);
//		System.out.println(s1.compareTo(s2));
//		System.out.println(listaStreams.ContadorMayorQueEdad(10));
//		System.out.println(listaStreams.ContadorEdadAltura(10, 1.40));
//		System.out.println(listaStreams.todosEdadAltura(12, 1.60));
//		System.out.println(listaStreams.existeEdadAltura(12, 1.60));
//		System.out.println(listaStreams.minDeAlturaPorEdad(12));
//		System.out.println(listaStrVacia.minDeAlturaPorEdad(12));				//NoSuchElementException -> lista vacía
//		System.out.println(listaStrVacia.minDeAlturaPorEdadSinError(12));		//null -> por la función ".orElse(null)"
//		System.out.println(listaStrVacia.minDeAlturaPorEdadConOpt(12));	 		//null -> por el optional + .isPresent() -> devuelve true si contiene algo
//		System.out.println(listaStreams.compararPorEdad().reversed());
//		System.out.println(listaStreams.sumaEdadesMayoresA(9));
//		System.out.println(listaStreams.mediaEdadesMayoresA(9));
//		listaStreams.cambioEdadPorAltura(12, 1.40);
//		System.out.println(listaStreams.toString());
//		System.out.println(listaStreams.listaEdadesPorAlturaMayorA(1.30));
//		System.out.println(listaStreams.listaEdadesPorAlturaMayorA_2(1.30));
		System.out.println(listaStreams.nombresPorEdad());
//		System.out.println(listaStreams.mayorDeEdad());
//		System.out.println(listaStreams.getStreams().stream().findAny());
//		System.out.println(listaStreams.getStreams().stream().findFirst());
//		System.out.println(listaStreams.getStreams().stream().limit(2));
//		System.out.println(listaStreams.getStreams().stream().noneMatch(x -> x.getAltura()<1.30));
//		System.out.println(listaStreams.getStreams().stream().peek(cambiar).collect(Collectors.toList()));
		
	}

}
