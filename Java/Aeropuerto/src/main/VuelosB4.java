package main;

import java.time.LocalDate;
import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class VuelosB4 extends Vuelos{

	public VuelosB4(String nombre, Collection<Vuelo> vuelos) {
		super(nombre, vuelos);
	}
	
	
	//1. Dado un destino, ¿existe algun vuelo con ese destino?
	
	public Boolean existeVueloDestino(String destino){
		Predicate<Vuelo> p = v -> v.getDestino().equals(destino);		//lo podemos hacer directamente pero para empezar y saber que hacemos empezamos así
		
		return getVuelos().stream()
				.anyMatch(p);
	}
	
	
	//2. Dado un número n devuelve cierto si todos los vuelos tienen al menos n pasajeros
	
	public Boolean todosVuelosNPasajeros(Integer n) {
		Predicate<Vuelo> p = vuelo -> vuelo.getNumPasajeros()>=n;
		
		return getVuelos().stream()
				.allMatch(p);			//allMatch() es una funcion TERMINAL, NO INTERMEDIA, ya que no puedes hacer nada mas despues de ella, ya devolvera ese resultado
	}
	
	
	//3. Dada una fecha, ¿cuántos vuelos hay ese día?
	
	public Long getNumVuelosFecha(LocalDate fecha) {
		Predicate<Vuelo> p = v -> v.getFecha().equals(fecha);
		
		return getVuelos().stream()
				.filter(p)				//Como filter() es una funcion INTERMEDIA, puedes seguir aplicando funciones. No te obliga a devolver algo (como allMatch())
				.count();
	}
	
	//4. Dada una fecha devuelve una lista con los vuelos posteriores a esa fecha
	
	public List<Vuelo> getVuelosPosteriores(LocalDate fecha){
		return getVuelos().stream()
				.filter(v -> v.getFecha().isAfter(fecha)).collect(Collectors.toList());			//OJO, si ponemos v.getFecha().isAfter(fecha)).toList() no está mal pero crea una lista INMUTABLE, asi que mejor la otra forma
	}
	
	
	//6. Dado un conjunto de destinos devuelve el número de pasajeros a los destinos del conjunto
	
	public Integer getNumPasajerosDestino(Set<String> destinos) {
		//Function<Vuelo, Integer> f = v -> v.getNumPasajeros(); 				Estas Function son las que van dentro del map, puede usarse una opción u otra (lo hemos rehecho fuera para que se vea mas claro)
		//Function<Vuelo, Integer> f2 = Vuelo::getNUmPasajeros(); 
		
		return getVuelos().stream()
				.filter(v -> destinos.contains(v.getDestino()))
				.mapToInt(v -> v.getNumPasajeros()).sum();						//OJO: si ponemos .map en vez de .mapToInt entonces no podriamos hacer la función sum()
	}
	
	//7. Dado un mes como un entero devuelve el precio medio de los vuelos de ese mes
	
	public Double getPrecioMedioVueloMes(Integer mes) {
		return getVuelos().stream()
				.filter(v -> v.getFecha().getMonthValue()==mes)
				.mapToDouble(Vuelo::getPrecio)
				.average().orElse(0.);											//OJO: la función orElse() va a devolver 0 si la lista (tras el filtrado) esta vacia
	}
	
	
	//9. Devuelve el vuelo con mayor número de pasajeros. Si no se puede calcular devuelve null						VAMOS A EMPEZAR A ORDENAR ASI QUE EMPEZAREMOS CON LA INTERFAZ COMPARATOR
	
	public Vuelo getVueloMasPasajeros() {
		Comparator<Vuelo> cmp = Comparator.comparing(Vuelo::getNumPasajeros);				//OJO: si hay empate (del orden natural) entonces agregamos .thenComparing(Comparator.comparing(...)) y agregamos el otro campo a comparar
		
		
		Optional<Vuelo> opt = getVuelos().stream()
				.max(cmp);
		
		//Opción 1 -> NoSuchElementException()
		opt.get();
		
		//Opción 2 -> orElse()					<---- MEJOR OPCIÓN
		return opt.orElse(null);
	}
	
	
	//10. Dado un destino devuelve el código del vuelo de menor precio que vuela a ese destino. Eleva NoSuchElementException si no se puede calcular
	
	public String getCodigoVueloMenorPrecio(String destino) {
		
		//filter + min + map + get
		return getVuelos().stream()									//Stream<Vuelo>
				.filter(v -> v.getDestino().equals(destino))		//Stream<Vuelo>
				.min(Comparator.comparing(Vuelo::getPrecio))		//Optional<Vuelo>
				.map(Vuelo::getCodigo)								//Optional<String>
				.get();												//String
	}
	
	
	//11. Dado un número n devuelve una lista con los n vuelos más baratos
	
	public List<Vuelo> getNVuelosMasBaratos(Integer n){
		Comparator<Vuelo> cmp = Comparator.comparing(Vuelo::getPrecio);
		
		return getVuelos().stream()
				.sorted(cmp)
				.limit(n)
				.collect(Collectors.toList());
	}
	
	
	//12. Dado un número n devuelve una lista con los n vuelos de mayor duración
	
	public List<Vuelo> getNVuelosMasDuracion(Integer n){
		return getVuelos().stream()
				.sorted(Comparator.comparing(Vuelo::getDuracion).reversed())
				.limit(n)
				.collect(Collectors.toList());	
	}
}
