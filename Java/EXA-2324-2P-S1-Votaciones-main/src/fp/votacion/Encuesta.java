package fp.votacion;

import java.time.*;
import java.util.*;
import fp.utiles.Checkers;

public class Encuesta {
	private String nombre;
	private LocalDate fecha_comienzo;
	private LocalDate fecha_fin;
	private Integer num_encuestados;
	private String pais;
	private TipoEncuesta tipo;
	private Double porcentaje_indecisos;
	private List<Resultado> resultados;
	
	public Encuesta(String l) {
		String [] trozos = l.split(",");
		String nombre = trozos[0].strip();
		LocalDate fecha_comienzo = LocalDate.parse(trozos[1].strip());
		LocalDate fecha_fin = LocalDate.parse(trozos[2].strip());
		String pais = trozos[3].strip();
		TipoEncuesta tipo = TipoEncuesta.valueOf(trozos[4].strip());
		Double porcentaje_indecisos = Double.valueOf(trozos[5].strip());
		List<Resultado> resultados = parseaResultados(trozos[7].strip());
		
		this.nombre = nombre;
		this.fecha_comienzo = fecha_comienzo;
		this.fecha_fin = fecha_fin;
		this.pais = pais;
		this.tipo = tipo;
		this.porcentaje_indecisos = porcentaje_indecisos;
		this.resultados = resultados;
	}
	
	private List<Resultado> parseaResultados(String cad) {
		String clear = cad.replace("'",	"").replace("(", "").replace(")", "");
		String [] trozos = clear.split(";");
		List<Resultado> res = new ArrayList<>();
		for(String trozo: trozos) {
			res.add(parseaResultado(trozo.strip()));
		}
		return res;
	}

	private Resultado parseaResultado(String trozo) {
		String [] trozos = trozo.split(":");
		Checkers.check("Formato resultado no válido", trozos.length == 2);
		String partido = trozos[0].strip();
		Double porcentaje = Double.valueOf(trozos[1].strip());
		return new Resultado(partido, porcentaje);
	}

	public Encuesta(String nombre, LocalDate fecha_comienzo, LocalDate fecha_fin, Integer num_encuestados, String pais, 
			TipoEncuesta tipo, Double porcentaje_indecisos, List<Resultado> resultados) {
		checkFechas(fecha_comienzo,fecha_fin);
		checkLista(resultados);
		checkNumEncuestados(num_encuestados);
		
		this.nombre=nombre;
		this.fecha_comienzo=fecha_comienzo;
		this.fecha_fin=fecha_fin;
		this.num_encuestados=num_encuestados;
		this.pais=pais;
		this.tipo=tipo;
		this.porcentaje_indecisos=porcentaje_indecisos;
		this.resultados=resultados;
		
		
	}

	private void checkNumEncuestados(Integer num_encuestados) {
		if(num_encuestados<0) {
			throw new IllegalArgumentException("El número de encuestados debe de ser mayor o igual a 0");
		}
		
	}

	private void checkLista(List<Resultado> resultados) {
		if(resultados.isEmpty()) {
			throw new IllegalArgumentException("La lista debe contener elementos");
		}
		
	}

	private void checkFechas(LocalDate fecha_comienzo, LocalDate fecha_fin) {
		if(fecha_comienzo.isAfter(fecha_fin)) {
			throw new IllegalArgumentException("La fecha de comienzo tiene que ser anterior a la de fin");
		}
	}

	public String getNombre() {
		return nombre;
	}

	public LocalDate getFecha_comienzo() {
		return fecha_comienzo;
	}

	public LocalDate getFecha_fin() {
		return fecha_fin;
	}

	public Integer getNum_encuestados() {
		return num_encuestados;
	}
	
	public void setNum_encuestados(Integer num_encuestados) {
		this.num_encuestados=num_encuestados;
	}

	public String getPais() {
		return pais;
	}

	public TipoEncuesta getTipo() {
		return tipo;
	}

	public Double getPorcentaje_indecisos() {
		return porcentaje_indecisos;
	}
	
	public void setPorcentaje_indecisos(Double porcentaje) {
		this.porcentaje_indecisos=porcentaje;
	}

	public List<Resultado> getResultados() {
		return resultados;
	}

	public Double getRatio_encuestados_diario() {
		Integer dias = Period.between(fecha_fin, fecha_comienzo).getDays();
		Double ratio = (double) (num_encuestados/dias);
		return ratio;
	}

	@Override
	public String toString() {
		return "Encuesta [nombre=" + nombre + ", fecha_comienzo=" + fecha_comienzo + ", fecha_fin=" + fecha_fin
				+ ", num_encuestados=" + num_encuestados + ", pais=" + pais + ", tipo=" + tipo
				+ ", porcentaje_indecisos=" + porcentaje_indecisos + ", resultados=" + resultados + "]";
	}
	
	
	@Override
	public int hashCode() {
		return Objects.hash(fecha_comienzo, fecha_fin, nombre, num_encuestados);
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Encuesta other = (Encuesta) obj;
		return Objects.equals(fecha_comienzo, other.fecha_comienzo) && Objects.equals(fecha_fin, other.fecha_fin)
				&& Objects.equals(nombre, other.nombre) && Objects.equals(num_encuestados, other.num_encuestados);
	}
	
	public int compareTo(Encuesta e) {
		int res = getFecha_comienzo().compareTo(e.getFecha_comienzo());
		if(res == 0) {
			res = getFecha_fin().compareTo(e.getFecha_fin());
		}
		if(res == 0) {
			res = getNombre().compareTo(e.getNombre());
		}
		if(res == 0) {
			res = getNum_encuestados().compareTo(e.getNum_encuestados());
		}
		
		return res;
	}
}
