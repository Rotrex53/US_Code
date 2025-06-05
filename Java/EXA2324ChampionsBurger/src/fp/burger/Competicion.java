package fp.burger;

import java.time.Duration;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.SortedMap;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Competicion {
	private SortedSet<Visita> visitas;
	
	public Competicion(Stream<Visita> visitas) {
		Comparator<Visita> comparador = Comparator.
				comparing(Visita::getCodigoPostal).
				thenComparing(Visita::compareTo);
		
		SortedSet<Visita> conjunto = visitas
				.collect(Collectors.toCollection(() -> new TreeSet<>(comparador)));
		
		this.visitas = conjunto;
	}

	public String toString() {
		String res = "";
		for(Visita visita: visitas) {
			String completo = visita + "\n";
			res.concat(completo);
		}
		return res;
	}

	@Override
	public int hashCode() {
		return Objects.hash(visitas);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Competicion other = (Competicion) obj;
		return Objects.equals(visitas, other.visitas);
	}
	
	
	//Ej1
	public SortedSet<Visita> getVisitas() {
		return visitas;
	}

	public SortedSet<String> getEmailsOrdenados(Duration d){
		Double temperaturaMediaTotal = getVisitas().stream()
										.mapToDouble(Visita::getTemperatura)
										.average()
										.getAsDouble();
		
		return getVisitas().stream()
				.filter(x -> x.getTiempoTranscurrido().compareTo(d)>0 && x.getTemperatura().compareTo(temperaturaMediaTotal)<0)
				.map(Visita::getEmail).collect(Collectors.toCollection(TreeSet::new));
	}
	
	//Ej2
	public Integer getTotalVisitasComilones() {
		Double mediaEvaluacionesTotal = getVisitas().stream()
											.mapToInt(Visita::getNumEvaluaciones)
											.average().getAsDouble();
											
		return getVisitas().stream()
				.filter(x -> x.getNumEvaluaciones() > mediaEvaluacionesTotal)
				.collect(Collectors.collectingAndThen(Collectors.counting(), Long::intValue));
	}
	
	//Ej3
	public String getPeorHamburgueseriaPorCalidadIngredientes() {
		Map<String, Double> map = getVisitas().stream()
				.flatMap(x -> x.getEvaluaciones().stream())
				.collect(Collectors
						.groupingBy(Evaluacion::hamburgueseria, 
								Collectors.averagingInt(Evaluacion::calidadIngredientes)));
		return map.entrySet().stream()
				.min(Map.Entry.comparingByValue())
				.map(Map.Entry::getKey)
				.orElse(null);
	}
	
	//Ej4
	public Map<String, String> getTopComilonPorCPEnDia(LocalDate d){
		return getVisitas().stream()
				.filter(x -> x.getEntrada().toLocalDate().equals(d))
				.collect(Collectors
						.groupingBy(Visita::getCodigoPostal,
								Collectors.collectingAndThen(Collectors
										.maxBy(Comparator.comparingInt(Visita::getNumEvaluaciones).reversed()
												.thenComparing(Visita::getEntrada)), 
										x -> x.map(Visita::getEmail).get())));
	}
	
	//Ej5
	public String getHamburgueseriaGanadora() {
		SortedMap<String, List<Double>> HambPorSumaPuntFinales = new TreeMap<>();
		SortedMap<String, Double> HambPorPuntPromedio = new TreeMap<>();
		Double comparador = 0.;
		String ganadora = "";
		for(Visita v: visitas) {
			for(Evaluacion e: v.getEvaluaciones()) {
				String clave = e.hamburgueseria();
				if(!HambPorSumaPuntFinales.containsKey(clave)) {
					HambPorSumaPuntFinales.put(clave, new ArrayList<>());
				}
				HambPorSumaPuntFinales.get(clave).add(e.getPuntuacionFinal());
			}
		}
		
		for(Map.Entry<String, List<Double>> entrada: HambPorSumaPuntFinales.entrySet()) {
			String hamburgueseria = entrada.getKey();
			List<Double> valores = entrada.getValue();
			Double sum = 0.;
			
			for(Double valor: valores) {
				sum+=valor;
			}
			
			Double puntPromedio = sum/valores.size();
			HambPorPuntPromedio.put(hamburgueseria, puntPromedio);
		}
		
		for(Map.Entry<String, Double> entrada: HambPorPuntPromedio.entrySet()) {
			Double valor = entrada.getValue();
			if(comparador==0.) {
				comparador = valor;
			}if(comparador<valor) {
				comparador = valor;
				ganadora = entrada.getKey();
			}
			
		}
		
		return ganadora;
	}
}
