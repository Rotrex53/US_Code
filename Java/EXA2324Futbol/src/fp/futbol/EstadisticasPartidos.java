package fp.futbol;

import java.util.Comparator;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class EstadisticasPartidos {
	private List<Partido> partidos;
	
	public EstadisticasPartidos(Stream<Partido> streamPartidos) {
		this.partidos = streamPartidos.collect(Collectors.toList());
	}
	
	public List<Partido> getPartidos(){
		return partidos;
	}
	
	public Integer getNumPartidos() {
		return getPartidos().size();
	}
	
	public String toString() {
		return getPartidos().stream().map(Partido::toString).collect(Collectors.joining("\n"));
	}

	@Override
	public int hashCode() {
		return Objects.hash(partidos);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		EstadisticasPartidos other = (EstadisticasPartidos) obj;
		return Objects.equals(partidos, other.partidos);
	}
	
	//Ej1
	public Integer getNumGolesEquipos(Set<String> equipos) {
		Integer res = 0;
		for(Partido p: getPartidos()) {
			if(equipos.contains(p.getEquipoLocal())) {
				res =+ p.getGolesLocal();
			} if(equipos.contains(p.getEquipoVisitante())) {
				res =+ p.getGolesVisitante();
			}
		}
		return res;
	}
	
	//Ej2
	public Integer getNumGolesDespuesMinuto(Integer minutoUmbral) {
		
		return getPartidos().stream()
				.filter(p -> p.getMinutos().getLast() >= minutoUmbral)
				.collect(Collectors.groupingBy(
						Partido::getResultadosParciales,
						TreeMap::new,
						Collectors.mapping(, Collectors.toList())));
				
	}
	
	//Ej3
	public SortedSet<Partido> getNPartidosMasEspectadores(Integer n){
		Comparator<Partido> comparador = getPartidos().stream()
											.map(Partido::getResultadosParciales);
		return getPartidos().stream()
				.collect(Collectors.toCollection(() -> new TreeSet<>(comparador)));
	}
}
