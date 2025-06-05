package fp.futbol;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Partido {
	private LocalDate fechaPartido;
	private String equipoLocal;
	private String equipoVisitante;
	private Long numEspectadores;
	private Competicion competicion;
	private List<Resultado> resultadosParciales;
	private Integer golesLocal;
	private Integer golesVisitante;
	private List<Integer> minutos;
	
	
	public Partido(LocalDate fechaPartido, String equipoLocal, String equipoVisitante, Long numEspectadores,
			Competicion competicion, List<Resultado> resultadosParciales, Integer golesLocal, Integer golesVisitante,
			List<Integer> minutos) {
		checkOrdenResultados(resultadosParciales);
		this.fechaPartido = fechaPartido;
		this.equipoLocal = equipoLocal;
		this.equipoVisitante = equipoVisitante;
		this.numEspectadores = numEspectadores;
		this.competicion = competicion;
		this.resultadosParciales = resultadosParciales;
		this.golesLocal = golesLocal;
		this.golesVisitante = golesVisitante;
		this.minutos = minutos;
	}
	
	//Constructor con String
	public Partido(String l) {
		String [] trozos = l.split(";");
		this.fechaPartido = LocalDate.parse(trozos[0].strip(), DateTimeFormatter.ofPattern("dd/MM/yyyy")) ;
		this.equipoLocal = trozos[1].strip();
		this.equipoVisitante = trozos[2].strip();
		this.numEspectadores = Long.parseLong(trozos[3].strip());
		this.competicion = Competicion.valueOf(trozos[4].strip().toUpperCase());
		this.resultadosParciales = parsearResultados(trozos[5].strip());
		this.golesLocal = getGolesLocalPorPartido(parsearResultados(trozos[5].strip()));
		this.golesVisitante = getGolesVisitantePorPartido(parsearResultados(trozos[5].strip()));
		this.minutos = getMinutosPorPartido(parsearResultados(trozos[5].strip()));
	}

	private List<Integer> getMinutosPorPartido(List<Resultado> lista) {
		List<Integer> res = new ArrayList<>();
		for(Resultado r: lista) {
			res.add(r.minuto());
		}
		return res;
	}

	private Integer getGolesLocalPorPartido(List<Resultado> lista) {
		Integer res = 0;
		for(Resultado r: lista) {
			res =+ r.golesLocal();
		}
		return res;
	}
	
	private Integer getGolesVisitantePorPartido(List<Resultado> lista) {
		Integer res = 0;
		for(Resultado r: lista) {
			res =+ r.golesVisitante();
		}
		return res;
	}
	
	private List<Resultado> parsearResultados(String trozo) {
		List<Resultado> res = new ArrayList<>();
		String clean = trozo.replace("[", "").replace("]", "");
		String [] trozos = clean.split(",");
		for(String str: trozos) {
			res.add(parseaResultado(str));
		}
		return res;
	}

	private Resultado parseaResultado(String str) {
		String [] trozos = str.split("-");
		Integer minutos = Integer.parseInt(trozos[0].strip());
		Integer golesLocal = Integer.parseInt(trozos[1].strip());
		Integer golesVisitante = Integer.parseInt(trozos[2].strip());
		return new Resultado(minutos, golesLocal, golesVisitante);
	}

	private void checkOrdenResultados(List<Resultado> resultadosParciales) {
			Boolean res = false;
			Integer comparador = 0;
		for(Resultado r: resultadosParciales) {
			if(comparador==0) {
				comparador=r.minuto();
			}
			if(r.minuto()>=comparador) {
				comparador=r.minuto();
				res = true;
			}
		}
		if(res=false) {
			throw new IllegalArgumentException("Los resultados deben estar ordenados por minutos ascendente");
		}
		
	}

	public LocalDate getFechaPartido() {
		return fechaPartido;
	}

	public String getEquipoLocal() {
		return equipoLocal;
	}

	public String getEquipoVisitante() {
		return equipoVisitante;
	}

	public Long getNumEspectadores() {
		return numEspectadores;
	}

	public Competicion getCompeticion() {
		return competicion;
	}

	public List<Resultado> getResultadosParciales() {
		return resultadosParciales;
	}

	public Integer getGolesLocal() {
		return golesLocal;
	}

	public Integer getGolesVisitante() {
		return golesVisitante;
	}

	public List<Integer> getMinutos() {
		return minutos;
	}

	@Override
	public String toString() {
		return "Partido [fechaPartido=" + fechaPartido + ", equipoLocal=" + equipoLocal + ", equipoVisitante="
				+ equipoVisitante + ", numEspectadores=" + numEspectadores + ", competicion=" + competicion
				+ ", resultadosParciales=" + resultadosParciales + ", golesLocal=" + golesLocal + ", golesVisitante="
				+ golesVisitante + ", minutos=" + minutos + "]";
	}

	@Override
	public int hashCode() {
		return Objects.hash(equipoLocal, equipoVisitante, fechaPartido);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Partido other = (Partido) obj;
		return Objects.equals(equipoLocal, other.equipoLocal) && Objects.equals(equipoVisitante, other.equipoVisitante)
				&& Objects.equals(fechaPartido, other.fechaPartido);
	}
	
	public int compareTo(Partido p) {
		Integer res = getFechaPartido().compareTo(p.getFechaPartido());
		if(res==0) {
			res = getEquipoLocal().compareTo(p.getEquipoLocal());
		} if(res==0) {
			res = getEquipoVisitante().compareTo(p.getEquipoVisitante());
		}
		return res;
	}
}
