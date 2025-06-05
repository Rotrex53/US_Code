package fp.examenes;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class CalendarioExamenes {
	private List<Examen> examenes;
	
	public CalendarioExamenes(Stream<Examen> streamExamenes) {
		this.examenes = streamExamenes.collect(Collectors.toList());
	}
	
	public List<Examen> getExamenes(){
		return examenes;
	}
	
	public Integer getNumExamenes() {
		return getExamenes().size();
	}
	
	public String toString(){
		return getExamenes().stream().map(Examen::toString).collect(Collectors.joining("\n"));
	}
	
	//Ej1 -> bucles
	public Map<String, Set<Examen>> getExamenesPorAula(){
		Map<String, Set<Examen>> res = new TreeMap<>();
		for(Examen e: getExamenes()) {
			for(Aula a: e.getAulas()) {
				if(!res.containsKey(a.nombre())) {
					res.put(a.nombre(), new HashSet<>());
				}
				res.get(a.nombre()).add(e);
			}
		}
		return res;
	}
	
	//Ej2
	public Examen getExamenMayorPorcentajeAsistentes(LocalTime t, String nombreAula) {
		Predicate<Examen> estaEnAula = e -> e.getAulas().stream().anyMatch(a -> a.nombre().equals(nombreAula));
		return getExamenes().stream()
				.filter(e -> e.getFechaHora().toLocalTime().isAfter(t) && 
						estaEnAula.test(e))
				.max(Comparator.comparing(Examen::getPorcentajeAsistentes)).get();
	}
	
	//Ej3
	public SortedSet<String> getAulasExamenesTipo(TipoExamen tipo){
		return getExamenes().stream()
				.filter(e -> e.getTipo().equals(tipo))
				.flatMap(e -> e.getAulas().stream())
				.map(Aula::nombre)
				.collect(Collectors.toCollection(TreeSet::new));
	}
	
	//Ej4
	public String getAulaMasOcupada(LocalDate fecha) {		
		return getExamenesPorAula().entrySet().stream()
				.map(entrada -> Map.entry(
						entrada.getKey(),
						entrada.getValue().stream()
						.filter(e -> e.getFechaHora().toLocalDate().equals(fecha))
						.mapToLong(e -> e.getDuracion().toMinutes()).sum()))
				.max(Comparator.comparing(Map.Entry::getValue))
				.map(Map.Entry::getKey).orElseThrow(NoSuchElementException::new);
	}
	
	//Ej5
	public List<LocalDate> getFechasConMasAulasDe(Integer umbral) {
		return getExamenes().stream()
				.filter(e -> e.getAulas().size()>umbral)
				.map(e -> e.getFechaHora().toLocalDate())
				.collect(Collectors.toCollection(TreeSet::new))
				.stream().toList();
	}
}
