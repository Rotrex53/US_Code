package fp.votacion;

import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class EstadisticasEncuestas {
	private List<Encuesta> encuestas;
	
	
	public EstadisticasEncuestas(Stream<Encuesta> s){
		this.encuestas = s.collect(Collectors.toList());
	}

	
	public List<Encuesta> getEncuestas(){
		return encuestas;
	}

	@Override
	public String toString() {
		return "EstadisticasEncuestas [encuestas=" + encuestas + "]";
	}


	@Override
	public int hashCode() {
		return Objects.hash(encuestas);
	}


	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		EstadisticasEncuestas other = (EstadisticasEncuestas) obj;
		return Objects.equals(encuestas, other.encuestas);
	}
	
	
	public Double getMediaNumEncuestadosConsultorayFecha(String consultora, LocalDate fechaMaxima) {
		return getEncuestas().stream()									//Stream<Encuesta>
				.filter(x -> x.getNombre().equals(consultora) 
						&& x.getFecha_fin().isBefore(fechaMaxima))		//Stream<Encuesta> (menos cantidad)
				.mapToInt(x -> x.getNum_encuestados())					//Stream<IntStream>
				.average()												//Double
				.orElse(0.);
	}
	
	public Encuesta getEncuestaMasEncuestadosPorDia(TipoEncuesta tipo) {
		return getEncuestas().stream()								//Stream<Encuesta>
				.filter(x -> x.getTipo().equals(tipo))				//Stream<Encuesta> (menos cantidad)
				.max(Comparator.comparing(Encuesta::getRatio_encuestados_diario))
				.get();
	}
	
	public List<String> getPartidosMasFrecuentesOrdenados(Integer n){
		Map<String, Long> contarPartidos = getEncuestas().stream()
				.flatMap(e -> e.getResultados().stream())
				.collect(Collectors.groupingBy(
						Resultado::getPartido, Collectors.counting()));
		Comparator<Map.Entry<String, Long>> comp = Map.Entry.comparingByValue();
		
		return contarPartidos.entrySet().stream()
				.sorted(comp.reversed())
				.limit(n)
				.map(e -> e.getKey())
				.collect(Collectors.toList());
	}
	
	public SortedMap<String, Boolean> getSuperaEncuestadosPorPais(Integer umbral){
		return getEncuestas().stream()											//Stream<Encuesta>
				.collect(Collectors.groupingBy(
						Encuesta::getPais,
						TreeMap::new,											//TreeMap<Pais, List<Encuesta>>
						Collectors.collectingAndThen(
								Collectors.toList(),							//coge la primera lista, desps la segunda,...
								encuestas -> todasEncuestasSuperanUmbral(		//SortedMap<Pais, Boolean>
										encuestas, umbral)
								)
						)
					);
	}


	private Boolean todasEncuestasSuperanUmbral(List<Encuesta> encuestas, Integer umbral) {
		return encuestas.stream()			//Stream<Encuesta>
				.allMatch(e -> e.getNum_encuestados()>umbral);							//
	}
	
	public Map<String, SortedSet<String>> getPaisesPorPartidoMayorPorcentaje(Double umbralPorcentaje){
		Map<String, SortedSet<String>> res = new TreeMap<>();
		for(int i=0; i<getEncuestas().size(); i++) {
			List<Resultado> resultados = getEncuestas().get(i).getResultados();
			for(int r=0; r<resultados.size();r++) {
				if(resultados.get(r).getPorcentaje()>umbralPorcentaje) {
					String clave = resultados.get(r).getPartido();
					if(!res.containsKey(clave)) {
						res.put(clave, new TreeSet<>());
					}
					res.get(clave).add(getEncuestas().get(i).getPais());
				}
			}
		}
		return res;
	}
	
	
	
	
	//Aparte
	
	public Integer getMenorNumEncuestadosPorPais(String pais){
		return getEncuestas().stream()
				.filter(e -> e.getPais().equals(pais))			//Stream<Encuesta> (filtro por pais)
				.min(Comparator.comparing(Encuesta::getNum_encuestados))
				.map(Encuesta::getNum_encuestados)
				.orElse(0);
	}
	
}
