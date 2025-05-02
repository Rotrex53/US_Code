package main;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

import java.util.Objects;
import java.util.Set;


public class Vuelos {

	private String nombre;
	private List<Vuelo> vuelos;

	public Vuelos(String nombre, Collection<Vuelo> vuelos) {
		this.nombre = nombre;
		this.vuelos = new ArrayList<Vuelo>(vuelos);
	}
	
	public String getNombre() {
		return nombre;
	}
	
	public List<Vuelo> getVuelos(){
		return new ArrayList<>(vuelos);
	}
	
	public Integer getNumVuelos() {
		return vuelos.size();
	}
	
	//Propiedades derivadas
	public Integer getNumPasajeros() {
		Integer suma=0;
		for(Vuelo v:vuelos) {
			suma+=v.getNumPasajeros();
		}
		return suma;
	}
	
	public Double getPrecioMedio() {
		Double suma=0.;
		Double res= null;
		for(Vuelo v:vuelos) {
			suma+=v.getPrecio();
		}
		if (getNumVuelos()>0) {
			res = suma/getNumVuelos();
		}
		return res;
	}
	public Integer getNumDestinosDistintos() {
		Set<String> conjdestinos=new HashSet<>();
		for(Vuelo v:vuelos) {
			conjdestinos.add(v.getDestino());
		}
		return conjdestinos.size();
	}

	public int hashCode() {
		return Objects.hash(vuelos, nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Vuelos other = (Vuelos) obj;
		return Objects.equals(vuelos, other.vuelos) && Objects.equals(nombre, other.nombre);
	}
	
	public String toString() {
		
		String s ="";	
		for (Vuelo v: vuelos) {
			s+=v + "\n";
		}
		return nombre + " -->\n\t" + s;
	}
	
	//Otras operaciones
	
	public Integer getNumPasajerosDestino(String destino) {
		Integer suma=0;
		for(Vuelo v:vuelos) {
			if (v.getDestino().equals(destino)) {
				suma+=v.getNumPasajeros();	
			}
		}
		return suma;
	}
	public void incorporaVuelo(Vuelo v) {
		vuelos.add(v);
	}
	public void incorporaVuelos(List<Vuelo> lv) {
		vuelos.addAll(lv);
	}
	public void eliminaVuelo(Vuelo v) {
		vuelos.remove(v);
	}
	public void ordena() {
		Collections.sort(vuelos);
	}
	
	public Boolean existeVueloDestino(String destino) {
		Boolean existe=false;
		for(Vuelo v:vuelos) {
			if (v.getDestino().equals(destino)) {
				existe=true;
				break;
			}
		}
		return existe;	
	}
	
}
