package fp.sevici;

import java.util.*;

public class RedEstaciones {
	private String nombre;
	private SortedSet<Estacion> estaciones;

	public RedEstaciones(String nombre) {
		this.nombre = nombre;
		this.estaciones = null;
	}
	
	public RedEstaciones() {
		this("");
	}
	
	public RedEstaciones(String nombre, Set<Estacion> estaciones) {
		this.nombre = nombre;
		this.estaciones = new TreeSet<Estacion>(estaciones);
	}
}
