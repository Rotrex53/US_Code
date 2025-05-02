package fp.sevici;

import java.util.Objects;

import fp.utiles.Checkers;

public class Estacion {
	private String id;
	private String nombre;
	private Integer numPuestos;
	private Integer bicisDisponibles;
	private Coordenadas ubicacion;
	
	public Estacion(String id,
					String nombre,
					Integer numPuestos,
					Integer bicisDisponibles,
					Coordenadas ubicacion){
		Checkers.check("Num puestos mayor que 0", numPuestos>0);
		Checkers.check("El num bicis debe ser >=0 y <= NumPuestos", 
						bicisDisponibles>=0 && bicisDisponibles<=numPuestos);
		this.id = id;
		this.nombre = nombre;
		this.numPuestos = numPuestos;
		this.bicisDisponibles = bicisDisponibles;
		this.ubicacion = ubicacion;
	}
	
	public Integer getBicisDisponibles() {
		return bicisDisponibles;
	}
	public void setBicisDisponibles(Integer bicisDisponibles) {
		this.bicisDisponibles = bicisDisponibles;
	}

	public String getId() {
		return id;
	}

	public String getNombre() {
		return nombre;
	}

	public Integer getNumPuestos() {
		return numPuestos;
	}

	public Coordenadas getUbicacion() {
		return ubicacion;
	}
	

	public Integer puestosVacios() {
		return numPuestos - bicisDisponibles;
	}
	
	public Boolean tieneBicisDisponibles() {
		return bicisDisponibles>0;
	}
	
	public Double ocupacion() {
		return Double.valueOf(bicisDisponibles/numPuestos *100);
	}

	
	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Estacion other = (Estacion) obj;
		return Objects.equals(id, other.id);
	}
	
	public Integer compareTo(Estacion e) {
		Integer res = getId().compareTo(e.getId());
		return res;
	}

	@Override
	public String toString() {
		return "Estacion [id=" + id + ", nombre=" + nombre + ", numPuestos=" + numPuestos + ", bicisDisponibles="
				+ bicisDisponibles + ", ubicacion=" + ubicacion + "]";
	}
}
