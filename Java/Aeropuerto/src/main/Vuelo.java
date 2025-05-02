package main;

import java.time.Duration;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;


import utiles.Checkers;
//import utiles.Validators;

public class Vuelo implements Comparable<Vuelo> {
	private Trayecto trayecto;
	private Double precio;
	private Integer numPasajeros;
	private Integer numPlazas;
	private String codigo;
	private LocalDate fecha;
	private Duration duracion;
	private List<String> tripulacion;

	public Vuelo(Trayecto trayecto, Double precio, Integer numPasajeros, Integer numPlazas, String codigo,
			LocalDate fecha, Duration duracion, List<String> tripulacion) {
		
		Checkers.check("Vuelo::El precio no es mayor que cero", precio > 0);
		Checkers.check("Vuelo::Numero de plazas menor que cero", numPlazas >= 0);
		checkNumPlazasNumPasajeros(numPlazas, numPasajeros);
		Checkers.check("Vuelo::Numero de pasajeros menor que cero", numPasajeros >= 0);
		Checkers.check("Vuelo::Duracion inferior a un minuto", duracion.toMinutes() >= 1);
		checkTripulacion(tripulacion);
		
		
		
		this.trayecto = trayecto;
		this.precio = precio;
		this.numPasajeros = numPasajeros;
		this.numPlazas = numPlazas;
		this.codigo = codigo;
		this.fecha = fecha;
		this.duracion = duracion;
		this.tripulacion = new ArrayList<>(tripulacion);
	}

	private void checkTripulacion(List<String> tripulacion) {
		Checkers.check("No hay más de 2 tripulantes", tripulacion.size() >= 3);
		Checkers.check("Vuelo::Al menos un código de la tripulación no tiene el formato correcto",
				Validators.sonCodigosTripulacionValidos(tripulacion));
		Checkers.check("Vuelo::Composición tripulación no válida",
				Validators.esComposicionTripulacionValida(tripulacion));
	}

	public Trayecto getTrayecto() {
		return trayecto;
	}

	public void setTrayecto(Trayecto trayecto) {
		this.trayecto = trayecto;
	}

	public Double getPrecio() {
		return precio;
	}

	public void setPrecio(Double precio) {
		Checkers.check("Vuelo::El precio no es mayor que cero", precio > 0);
		this.precio = precio;
	}

	public Integer getNumPlazas() {
		return numPlazas;
	}

	public void setNumPlazas(Integer numPlazas) {
		Checkers.check("Vuelo::Numero de plazas menor que cero", numPlazas >= 0);
		checkNumPlazasNumPasajeros(numPlazas, getNumPasajeros());
		this.numPlazas = numPlazas;
	}

	private void checkNumPlazasNumPasajeros(Integer numPlazas, Integer numPasajeros) {
		Checkers.check("Vuelo::Numero de plazas no es superior o igual al numero de pasajeros",
				numPlazas >= numPasajeros);
	}

	public Integer getNumPasajeros() {
		return numPasajeros;
	}

	public void setNumPasajeros(Integer numPasajeros) {
		Checkers.check("Vuelo::Numero de pasajeros menor que cero", numPasajeros >= 0);
		checkNumPlazasNumPasajeros(getNumPlazas(), numPasajeros);
		this.numPasajeros = numPasajeros;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public LocalDate getFecha() {
		return fecha;
	}

	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}

	public Duration getDuracion() {
		return duracion;
	}

	public void setDuracion(Duration duracion) {
		Checkers.check("Vuelo::Duracion inferior a un minuto", duracion.toMinutes() >= 1);
		this.duracion = duracion;
	}

	public List<String> getTripulacion() {
		return new ArrayList<>(tripulacion);
	}

	// Propiedades derivadas
	public String getOrigen() {
		return trayecto.origen();
	}

	public String getDestino() {
		return trayecto.destino();
	}

	public Long getDuracionMinutos() {
		return duracion.toMinutes();
	}

	public Boolean estaCompleto() {
		return getNumPlazas().equals(getNumPasajeros());
	}

	public Double getPorcentajeOcupacion() {
		return getNumPasajeros() * 100. / getNumPlazas();
	}

	@Override
	public int hashCode() {
		return Objects.hash(codigo, fecha);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Vuelo other = (Vuelo) obj;
		return Objects.equals(codigo, other.codigo) && Objects.equals(fecha, other.fecha);
	}

	public int compareTo(Vuelo v) {
		int res = this.fecha.compareTo(v.getFecha());
		if (res == 0) {
			res = this.codigo.compareTo(v.getCodigo());
		}
		return res;
	}

	public String toString() {
		return "Vuelo [Trayecto=" + trayecto + ", codigo=" + codigo + ", fecha=" + fecha + "]";
	}

	//Otras operaciones
	
	/**
	 * @param porcentaje Porcentaje de incremento del precio
	 * Incrementa el precio del vuelo en el porcentaje dado como parámetro.
	 */
	public void incrementaPrecioPorcentaje(Double porcentaje) {
		Double nuevoPrecio = getPrecio() * (1 + porcentaje / 100);
		setPrecio(nuevoPrecio);
	}

}
