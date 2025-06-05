package fp.examenes;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Examen {
	private String asignatura;
	private Integer curso;
	private LocalDateTime fechaHora;
	private Duration duracion;
	private TipoExamen tipo;
	private Integer asistentes;
	private Boolean inscripcion;
	private List<Aula> aulas;	
	
	public Examen(String asignatura, Integer curso, LocalDateTime fechaHora, Duration duracion, TipoExamen tipo,
			Integer asistentes, Boolean inscripcion, List<Aula> aulas) {

		checkAsistentes(asistentes);
		checkDuracion(duracion);
		this.asignatura = asignatura;
		this.curso = curso;
		this.fechaHora = fechaHora;
		this.duracion = duracion;
		this.tipo = tipo;
		this.asistentes = asistentes;
		this.inscripcion = inscripcion;
		this.aulas = aulas;
	}
	
	//Constructor a partir de String
	public Examen(String l) {
		String [] trozos = l.split(",");
		this.asignatura = trozos[0].strip();
		this.curso = Integer.parseInt(trozos[1].strip());
		this.fechaHora = LocalDateTime.of(LocalDate.parse(trozos[2].strip(), DateTimeFormatter.ofPattern("dd/MM/yyyy")), 
											LocalTime.parse(trozos[3].strip(), DateTimeFormatter.ofPattern("HH:mm")));
		this.duracion = Duration.ofMinutes(Long.parseLong(trozos[4].strip()));
		this.tipo = TipoExamen.valueOf(trozos[5].strip().toUpperCase());
		this.asistentes = Integer.parseInt(trozos[6].strip());
		this.inscripcion = Boolean.parseBoolean(trozos[7].strip());
		this.aulas = parsearAulas(trozos[8].strip());
	}

	private List<Aula> parsearAulas(String trozo) {
		List<Aula> aulas = new ArrayList<>();
		String [] trozos = trozo.split(";");
		for(String a: trozos) {
			aulas.add(parsearAula(a));
		}
		return aulas;
	}

	private Aula parsearAula(String a) {
		String [] trozos = a.split("-");
		String nombre = trozos[0].strip();
		Integer capacidad = Integer.parseInt(trozos[1].strip());
		return new Aula(nombre, capacidad);
	}

	private void checkDuracion(Duration duracion) {
		if(duracion.toMinutes()<60) {
			throw new IllegalArgumentException("La duración debe ser de al menos 1 hora");
		}
		
	}

	private void checkAsistentes(Integer asistentes) {
		if(asistentes<=0) {
			throw new IllegalArgumentException("El número de asistentes debe ser mayor que 0");
		}
		
	}

	public List<Integer> getPuestos(){
		List<Integer> res = new ArrayList<>();
		for(Aula a: aulas) {
			res.add(a.capacidad());
		}
		return res;
	}

	public Integer getCapacidadMaxima() {
		Integer res = 0;
		for(Integer i: getPuestos()) {
			res+=i;
		}
		return res;
	}
	
	public Double getPorcentajeAsistentes() {
		return getAsistentes()*100./getCapacidadMaxima();
	}

	public Duration getDuracion() {
		return duracion;
	}



	public void setDuracion(Duration duracion) {
		this.duracion = duracion;
	}



	public Integer getAsistentes() {
		return asistentes;
	}



	public void setAsistentes(Integer asistentes) {
		this.asistentes = asistentes;
	}



	public String getAsignatura() {
		return asignatura;
	}



	public Integer getCurso() {
		return curso;
	}



	public LocalDateTime getFechaHora() {
		return fechaHora;
	}



	public TipoExamen getTipo() {
		return tipo;
	}



	public Boolean getInscripcion() {
		return inscripcion;
	}



	public List<Aula> getAulas() {
		return aulas;
	}

	@Override
	public String toString() {
		return "Examen [asignatura=" + asignatura + ", curso=" + curso + ", fechaHora=" + fechaHora + ", duracion="
				+ duracion + ", tipo=" + tipo + ", asistentes=" + asistentes + ", inscripcion=" + inscripcion
				+ ", aulas=" + aulas + "]";
	}

	@Override
	public int hashCode() {
		return Objects.hash(asignatura, curso, fechaHora);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Examen other = (Examen) obj;
		return Objects.equals(asignatura, other.asignatura) && Objects.equals(curso, other.curso)
				&& Objects.equals(fechaHora, other.fechaHora);
	}
	
	public int compareTo(Examen e) {
		Integer res = getFechaHora().compareTo(e.getFechaHora());
		if(res==0) {
			res = getCurso().compareTo(e.getCurso());
		}
		if(res==0) {
			res = getAsignatura().compareTo(e.getAsignatura());
		}
		return res;
	}
	
	//Otras operaciones
	public Boolean usaAula(String nombreAula) {
		Boolean res = false;
		for(Aula a: getAulas()) {
			if(a.nombre()==nombreAula) {
				res = true;
			}
		}
		return res;
	}
}

