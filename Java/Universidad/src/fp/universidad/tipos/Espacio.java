package fp.universidad.tipos;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

import fp.utiles.*;

public class Espacio {
	//Atributos
	private TipoEspacio tipo;
	private String nombre;
	private Integer capacidad;
	private Integer planta;
	
	//Métodos
		//Constructor
	//Canónico
	public Espacio(TipoEspacio tipo, String nombre, Integer capacidad) {
		setTipo(tipo);
		setNombre(nombre);
		setCapacidad(capacidad);
		
		//TODO: Restricciones
		
	}
	
	public Espacio(String c) {
		String [] trozos = c.split(",");
		Checkers.check("cadena no trozeada", trozos.length==4);
		this.nombre = trozos[0].strip();
		this.planta = Integer.parseInt(trozos[1].strip());
		this.capacidad = Integer.parseInt(trozos[2].strip());
		this.tipo = TipoEspacio.valueOf(trozos[3].strip());
	}

		//Getters & Setters
	public TipoEspacio getTipo() {
		return tipo;
	}
	public void setTipo(TipoEspacio tipo) {
		this.tipo = tipo;
	}
	

	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	

	public Integer getCapacidad() {
		return capacidad;
	}
	public void setCapacidad(Integer capacidad) {
		Checkers.check("Capacidad debe ser mayor que 0", capacidad>0);
		this.capacidad = capacidad;
	}
	
	public Integer getPlanta() {
		return planta;
	}

	
		//toString
		//"A3.10 (planta 3)"
	@Override
	public String toString() {
		return nombre + " (planta " + planta + ") ";
	}
	
	
	public int hashCode() {
		return getNombre().hashCode() + 31*planta.hashCode();
	}
	
	
	public boolean equals(Object o) {
		if(this == o) return true;
		if(o instanceof Espacio) {
			Espacio espacio = (Espacio) o;
			return getNombre().equals(espacio.getNombre()) && planta.equals(espacio.planta);
		}
		return false;
	}
	
	
	public int compareTo(Espacio o) {
		int res = planta.compareTo(o.planta);
		if(res == 0) {
			res = getNombre().compareTo(o.getNombre());
		}
		return res;
	}
}