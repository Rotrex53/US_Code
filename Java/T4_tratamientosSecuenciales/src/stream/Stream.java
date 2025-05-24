package stream;

import java.util.*;

public class Stream {
	private Integer edad;
	private Double altura;
	private String nombre;
	private String DNI;
	
	public Stream(Integer edad, Double altura, String nombre, String DNI) {
		this.edad=edad;
		this.altura=altura;
		this.nombre=nombre;
		this.DNI=DNI;
		
	}

	public Integer getEdad() {
		return edad;
	}

	public void setEdad(Integer edad) {
		this.edad = edad;
	}

	public Double getAltura() {
		return altura;
	}

	public void setAltura(Double altura) {
		this.altura = altura;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDNI() {
		return DNI;
	}

	public void setDNI(String DNI) {
		DNI = DNI;
	}
	
	
	public int hashCode() {
		return getEdad().hashCode() + 31*getAltura().hashCode() + 31*31*getNombre().hashCode() + 31*31*31*getDNI().hashCode();
	}
	
	public int compareTo(Stream s) {
		int res = getEdad().compareTo(s.getEdad());
		if(res == 0) {
			res = getAltura().compareTo(s.getAltura());
		}
		if(res == 0) {
			res = getNombre().compareTo(s.getNombre());
		}
		if(res == 0) {
			res = getDNI().compareTo(s.getDNI());
		}
		return res;
	}
	
	public String toString() {
		return getNombre() + ": Edad = " + getEdad() + ", Altura = " + getAltura() + "m, DNI = " + getDNI();
	}
	
}
