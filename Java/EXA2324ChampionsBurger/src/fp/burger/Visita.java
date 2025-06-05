package fp.burger;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.Period;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;


import java.time.format.DateTimeFormatter;

public class Visita {
	private String email;
	private String ciudad;
	private String codigoPostal;
	private LocalDateTime entrada;
	private LocalDateTime salida;
	private Double temperatura;
	private List<Evaluacion> evaluaciones;
	
	public Visita(String email, String ciudad, String codigoPostal,
			LocalDateTime entrada, LocalDateTime salida, Double temperatura, List<Evaluacion> evaluaciones) {
		checkSalida(salida);
		checkEmail(email);
		checkEvaluaciones(evaluaciones);
		checkDias(entrada, salida);
		this.email = email;
		this.ciudad = ciudad;
		this.codigoPostal = codigoPostal;
		this.entrada = entrada;
		this.salida = salida;
		this.temperatura = temperatura;
		this.evaluaciones = evaluaciones;
		
	}
	
	public Visita(String l) {
		String [] trozos = l.split(";");
		this.email = trozos[0].strip();
		this.ciudad = trozos[1].strip();
		this.codigoPostal = trozos[2].strip();
		this.entrada = LocalDateTime.parse(trozos[3].strip(), DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
		this.temperatura = Double.parseDouble(trozos[4].strip());
		this.salida = LocalDateTime.parse(trozos[5].strip(), DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
		this.evaluaciones = parseaEvaluaciones(trozos[6].strip());
	}

	private List<Evaluacion> parseaEvaluaciones(String trozo) {
		String clean = trozo.replace("[", "").replace("]", "");
		String [] trozos = clean.split("-");
		List<Evaluacion> lista = new ArrayList<>();
		for(String evaluacion: trozos) {
			lista.add(parseaEvaluacion(evaluacion.strip()));
		}
		return lista;
	}

	private Evaluacion parseaEvaluacion(String evaluacion) {
		String clean = evaluacion.replace("(", "").replace(")", "");
		String [] trozos = clean.split(":");
		String hamburgueseria = trozos[0].strip();
		String [] puntuacionesStr = trozos[1].split(",");
		Integer presentacion = Integer.parseInt(puntuacionesStr[0].strip());
		Integer ptoDeCarne = Integer.parseInt(puntuacionesStr[1].strip());
		Integer calidadIngredientes = Integer.parseInt(puntuacionesStr[2].strip());
		Integer calidadPan = Integer.parseInt(puntuacionesStr[3].strip());
		return new Evaluacion(hamburgueseria, presentacion, ptoDeCarne,
				calidadIngredientes, calidadPan);
	}
	

	private void checkSalida(LocalDateTime salida) {
		if(salida.isBefore(entrada)) {
			throw new IllegalArgumentException("la salida tiene que ser posterior a la entrada");
		}
	}
	
	private void checkEmail(String email) {
		if(!email.contains("@")) {
			throw new IllegalArgumentException("el email debe contener @");
		}
	}
	
	private void checkEvaluaciones(List<Evaluacion> evaluaciones) {
		if(evaluaciones.isEmpty()) {
			throw new IllegalArgumentException("la lista debe contener al menos un elemento");
		}
	}
	
	private void checkDias(LocalDateTime entrada, LocalDateTime salida) {
		if(entrada.getDayOfMonth()!=salida.getDayOfMonth()) {
			throw new IllegalArgumentException("el dia de entrada deber ser el mismo que el de salida");
		}
	}

	
	public LocalDateTime getSalida() {
		return salida;
	}

	public void setSalida(LocalDateTime salida) {
		this.salida = salida;
	}

	public Double getTemperatura() {
		return temperatura;
	}

	public void setTemperatura(Double temperatura) {
		this.temperatura = temperatura;
	}

	public String getEmail() {
		return email;
	}

	public String getCiudad() {
		return ciudad;
	}

	public String getCodigoPostal() {
		return codigoPostal;
	}

	public LocalDateTime getEntrada() {
		return entrada;
	}

	public List<Evaluacion> getEvaluaciones() {
		return evaluaciones;
	}
	
	public Duration getTiempoTranscurrido() {
		return Duration.between(entrada, salida);
	}
	
	public Integer getNumEvaluaciones() {
		return evaluaciones.size();
	}
	
	public Paladar getPaladar() {
		Double sum = 0.;
		for(Evaluacion e: evaluaciones) {
			sum += e.getPuntuacionFinal();
		}
		Double media = sum/getNumEvaluaciones();
		if(media>=9) {
			return Paladar.BAJO;
		}
		if(media<=6) {
			return Paladar.ALTO;
		}
		else {
			return Paladar.MEDIO;
		}
	}


	@Override
	public String toString() {
		return "Visita [email=" + email + ", ciudad=" + ciudad + ", codigoPostal=" + codigoPostal + ", entrada="
				+ entrada + ", salida=" + salida + ", temperatura=" + temperatura + ", evaluaciones=" + evaluaciones
				+ "]";
	}

	@Override
	public int hashCode() {
		return Objects.hash(email, entrada, salida);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Visita other = (Visita) obj;
		return Objects.equals(email, other.email) && Objects.equals(entrada, other.entrada)
				&& Objects.equals(salida, other.salida);
	}
	
	
	public int compareTo(Visita v) {
		int res = getEntrada().compareTo(v.getEntrada());
		if(res==0) {
			res = getSalida().compareTo(v.getSalida());
		} if(res==0) {
			res = getEmail().compareTo(v.getEmail());
		}
		return res;
	}
}
