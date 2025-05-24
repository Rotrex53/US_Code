package stream;

import java.time.LocalDate;
import java.util.*;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class Streams {
	List<Stream> streams;
	
	public Streams(List<Stream> streams){
		this.streams = streams;
	}
	
	public List<Stream> getStreams(){
		return streams;
	}
	
	public void setStreams(List<Stream> s) {
		streams = s;
	}
	
	public String toString() {
		return streams.toString();
	}
	
	
	public Long ContadorMayorQueEdad(Integer edad) {
		return getStreams().stream()
				.filter(x -> x.getEdad()>edad)
				.count();
	}
	
	public Long ContadorMayorQueEdadPredicate(Integer edad) {
		Predicate<Stream> mayorQueEdad = x -> x.getEdad()>edad;
		return getStreams().stream()
				.filter(mayorQueEdad)
				.count();
	}
	
	public static Predicate<Stream> streamEdad(Integer edad){
		return x -> x.getEdad().equals(edad);
	}
	
	public static Predicate<Stream> streamAltura(Double altura){
		return x -> x.getAltura().equals(altura);
	}
	
	public Long ContadorEdadAltura(Integer edad, Double altura) {
		return getStreams().stream()
				.filter(streamEdad(edad).and(streamAltura(altura))).count();
	}
	
	public Boolean todosEdadAltura(Integer edad, Double altura) {
		Predicate<Stream> porEdad = x -> x.getEdad().equals(edad);
		Predicate<Stream> porAltura = x -> x.getAltura().equals(altura);
		return getStreams().stream()
				.filter(porEdad).allMatch(porAltura);
	}
	
	public Boolean existeEdadAltura(Integer edad, Double altura) {
		Predicate<Stream> porEdad = x -> x.getEdad().equals(edad);
		Predicate<Stream> porAltura = x -> x.getAltura().equals(altura);
		return getStreams().stream()
				.anyMatch(porEdad.and(porAltura));
	}
	
	public Stream minDeAlturaPorEdad(Integer edad) {
		Predicate<Stream> porEdad = x -> x.getEdad().equals(edad);
		return getStreams().stream()
				.filter(porEdad).min(Comparator.comparing(Stream::getAltura)).get();
	}
	
	public Stream minDeAlturaPorEdadSinError(Integer edad) {
		Predicate<Stream> porEdad = x -> x.getEdad().equals(edad);
		return getStreams().stream()
				.filter(porEdad).min(Comparator.comparing(Stream::getAltura)).orElse(null);
	}
	
	public Stream minDeAlturaPorEdadConOpt(Integer edad) {
		Predicate<Stream> porEdad = x -> x.getEdad().equals(edad);
		Stream s = null;
		Optional<Stream> op = getStreams().stream()
				.filter(porEdad).min(Comparator.comparing(Stream::getAltura));
		if(op.isPresent()) {
			s = op.get();
		}
		return s;
	}
	
	public java.util.stream.Stream<Stream> ordenEdad() {
		return getStreams().stream()
				.sorted(Comparator.comparing(Stream::getEdad));
	}
	
	public List<Stream> compararPorEdad() {
		Function<Stream, Integer> funcionPorEdad = x -> x.getEdad();
		Collections.sort(streams, Comparator.comparing(funcionPorEdad));
		return streams;
	}
	
	public List<Stream> compararPorEdad2() {
		Function<Stream, Integer> funcionPorEdad = Stream::getEdad;
		Collections.sort(streams, Comparator.comparing(funcionPorEdad));
		return streams;
	}
	
	public Integer sumaEdadesMayoresA(Integer edad) {
		Predicate<Stream> mayorEdadA = x -> x.getEdad()>edad;
		return getStreams().stream()
				.filter(mayorEdadA)
				.mapToInt(x -> x.getEdad())
				.sum();
	}
	
	public Double mediaEdadesMayoresA(Integer edad) {
		Predicate<Stream> mayorEdadA = x -> x.getEdad()>edad;
		return getStreams().stream()
				.filter(mayorEdadA)
				.mapToInt(x -> x.getEdad())
				.average()
				.getAsDouble();
	}
	
//	Uso de FlatMap: si tengo List dentro de List lo aplana
//	public List<Pasajero> pasajerosVuelosFecha(LocalDate fecha) {
//		return getVuelos().stream()
//		.filter(x -> x.getFechaSalida().equals(fecha))
//		.flatMap(x -> x.getPasajeros().stream())
//		.collect(Collectors.toList());
//	}
	
	public Consumer<Stream> cambioDNI(String DNI){
		Consumer<Stream> c = x -> x.setDNI(DNI);
		return c;
	}
	
	public void cambioEdadPorAltura(Integer edad, Double altura){
		getStreams().stream()
		.filter(x -> x.getAltura().equals(altura))
		.forEach(x -> x.setEdad(edad));
	}
	
	public List<Integer> listaEdadesPorAlturaMayorA(Double altura){
		return getStreams().stream()
				.filter(x -> x.getAltura()>altura)
				.map(x -> x.getEdad())
				.collect(Collectors.toList());
	}
	
	public List<Integer> listaEdadesPorAlturaMayorA_2(Double altura){
		return getStreams().stream()
				.filter(x -> x.getAltura()>altura)
				.map(x -> x.getEdad())
				.collect(Collectors.toCollection(LinkedList::new));
	}
	
	public Map<Integer, List<String>> nombresPorEdad(){
		return getStreams().stream()
				.collect(Collectors.groupingBy(Stream::getEdad, Collectors.mapping(Stream::getNombre, Collectors.toList())));
	}
	
	//partitioningBy(Predicate): es un groupingBy pero con true-false de claves
	public Map<Boolean, List<Stream>> mayorDeEdad(){
		Predicate<Stream> mayoriaDeEdad = x -> x.getEdad()>=18;
		return getStreams().stream()
				.collect(Collectors.partitioningBy(mayoriaDeEdad));
	}
	
	
}
