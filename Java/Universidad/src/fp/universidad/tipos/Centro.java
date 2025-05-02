package fp.universidad.tipos;
import java.util.*;

public class Centro {
	private String nombre;
	private String direccion;
	private Integer planta;
	private Integer sotano;
	private Set<Espacio> espacio;
	
	public Centro(String nombre, String direccion, Integer planta, Integer sotano) {
		this.espacio = null;
		ComprobarPlantaSotano(planta, sotano);
		
	}
	
	private void ComprobarPlantaSotano(Integer planta, Integer sotano) {
		if(getPlanta()<=0) {
			throw new IllegalArgumentException("La planta tiene que ser mayor que cero");
		}
		if(getSotano()<0) {
			throw new IllegalArgumentException("El sótano tiene que ser mayor o igual que cero");
		}
	}

	public String getNombre() {
		return nombre;
	}

	public String getDireccion() {
		return direccion;
	}

	public Integer getPlanta() {
		return planta;
	}

	public Integer getSotano() {
		return sotano;
	}

	public Set<Espacio> getEspacio() {
		return espacio;
	}
	
	public void setEspacio(Set<Espacio> espacio) {
		nuevoEspacio(espacio);
		eliminaEspacio(espacio);
	}
	
	private void nuevoEspacio(Set<Espacio> e) {
		espacio.addAll(e);
	}
	
	private void eliminaEspacio(Set<Espacio> e) {
		espacio.removeAll(e);
	}
	
	public String toString() {
		return nombre;
	}
	
	public int hashCode() {
		return getNombre().hashCode();
	}
	
	public boolean equals(Object o) {
		if(this == o) return true;
		if(o instanceof Centro) {
			Centro centro = (Centro) o;
			return getNombre().equals(centro.getNombre());
		}
		return false;
	}
	
	public int compareTo(Centro o) {
		int res = getNombre().compareTo(o.getNombre());
		return res;
	}
	
	
	public ArrayList<Integer> getConteosEspacios(Centro c){
		//TODO
		return null;
	}
	
	public Set<Despacho> getDespachos(Integer d){
		//TODO
		return null;
	}
	
	public Set<String> getProfesores(Integer d){
		//TODO
		return null;
	}
	
	public Espacio getEspacioMayorCapacidad (Espacio espacio) {
		//TODO
		return null;
	}
}
