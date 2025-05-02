package main;

import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;

public class VuelosB5 extends Vuelos{

	public VuelosB5(String nombre, Collection<Vuelo> vuelos) {
		super(nombre, vuelos);
		// TODO Auto-generated constructor stub
	}
	
//	Dada una fecha f devuelve el número de destinos diferentes de todos los vuelos de esa fecha.
	
		//Contador
	public Long getNumDestinoDiferentesFechas(LocalDate f) {
		return getVuelos().stream()
				.filter(v -> v.getFecha().equals(f))	//Stream<Vuelo>
				.map(Vuelo::getDestino) 	//Stream<String>
//				.collect(Collectors.toSet()).size() 	//Set<String>   sin repetidos
				.distinct()		//Streak<String> sin repetidos
				.count();		//Long
	}
	
//	Devuelve un conjunto ordenado con los vuelos ordenados por el orden natural del tipo.
	public SortedSet<Vuelo> getVuelosOrdenados(){
		//SortedSet<Vuelo> ss = new TreeSet<>(Comparator.comparing(Vuelo::getDestino))		OJO: es una forma de decirle que orden seguir al TreeSet
		
//		Opción 1: para solo orden natural
//		return getVuelos().stream()
//				.collect(Collectors.toCollection(TreeSet::new));
		
		//Opcion 2: para casos distintos al orden natural: Lambda
		
		return getVuelos().stream()
		.collect(Collectors.toCollection( () -> new TreeSet<>(Comparator.naturalOrder())));
				
	}
	
//	Dada una letra devuelve un conjunto ordenado alfabéticamente de manera ascendente con los destinos que empiezan por esa letra.
	public SortedSet<String> getDestinosOrdenados(Character c){
		return getVuelos().stream()
				.filter(v -> c.equals(v.getDestino().charAt(0)))	//Stream<Vuelo>
				.map(v -> v.getDestino())		//Stream<String>
				.collect(Collectors.toCollection(TreeSet::new));
//				.collect(Collectors.toCollection( () -> new TreeSet<>(Comparator.naturalOrder(reversed))));		Asi seria si pidieran orden descendente
	}
	
//	Devuelve un conjunto ordenado por longitud de caracteres con los destinos de todos los vuelos.
	public SortedSet<String> getDestinosOrdenadosPorLongitud() {
		Comparator<String> cmp = Comparator.comparing(String::length)
				.thenComparing(Comparator.naturalOrder());			//por si empatan por longitud entonces orden natural (alfabetico)
		
		return getVuelos().stream()
				.map(Vuelo::getDestino)
				.collect(Collectors.toCollection( () -> new TreeSet<>(cmp)));
	}
	
//	Devuelve un Map que a cada fecha le haga corresponder una lista con sus vuelos.
		//groupingBy por defecto (1 parámetro)
	public Map<LocalDate, List<Vuelo>> getVuelosPorFecha(){
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getFecha));
	}
	
//	Devuelve un Map que a cada fecha le haga corresponder un conjunto con sus vuelos.
		//groupingBy donde el 2º parametro es .toSet()
	public Map<LocalDate, Set<Vuelo>> getVuelosPorFecha2(){
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getFecha, Collectors.toSet()));
	}
	
//	Devuelve un Map que a cada fecha le haga corresponder el número de vuelos.
		//Contador: Collectors.counting()
	public Map<LocalDate, Long> getNumeroVuelosFecha() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getFecha, Collectors.counting()));
	}
	
	//Versión 2: devuelve Integer en vez de Long
	public Map<LocalDate, Integer> getNumeroVuelosFecha2() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(
									Vuelo::getFecha, 
									Collectors.collectingAndThen(
												Collectors.counting(), lon -> lon.intValue()
												)
									)
						);
	}
	
//	Devuelve un Map que a cada destino le haga corresponder el número total de plazas.
		//Acumulador: Collectors.summing()
	public Map<String, Integer> getNumPlazasPorDestino(){
		return getVuelos().stream()
				.collect(
				Collectors.groupingBy(
							Vuelo::getDestino,
							Collectors.summingInt(Vuelo::getNumPlazas)
							)
				);
	}
	
//	Devuelve un Map que a cada destino le haga corresponder el precio medio de sus vuelos.
		//Media: Collectors.averaging
	public Map<String, Double> getPrecioMedioPorDestino(){
		return getVuelos().stream()
				.collect(
				Collectors.groupingBy(
							Vuelo::getDestino,
							Collectors.averagingDouble(Vuelo::getPrecio)
							)
				);
	}
	
//	Devuelve un Map que a cada destino le haga corresponder un conjunto con las fechas de los vuelos a ese destino.
		//Transformación de los valores: Collectors.mapping
	public Map<String, Set<LocalDate>> getConjuntoFechasDestino(){
		return getVuelos().stream()
				.collect(
				Collectors.groupingBy(
						Vuelo::getDestino,
						Collectors.mapping(
									Vuelo::getFecha,
									Collectors.toSet())
						)
				);
	}
	
	//Versión SortedMap
	//groupingBy con 3 parámetros
	//keyMapper, constructor, valueMapper
	public Map<String, Set<LocalDate>> getConjuntoFechasDestino2(){
		return getVuelos().stream()
				.collect(
				Collectors.groupingBy(
						Vuelo::getDestino,
						TreeMap::new,							//() -> new TreeMap<>(),
						Collectors.mapping(
									Vuelo::getFecha,
									Collectors.toSet())
						)
				);
	}
}
