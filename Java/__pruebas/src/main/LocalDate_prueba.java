package main;

import java.time.*;
import java.time.format.*;

public class LocalDate_prueba {
	private LocalDate fecha;
	
	public LocalDate_prueba(LocalDate fecha) {
		this.fecha = fecha;
	}
	
	public LocalDate getFecha() {
		return fecha;
	}
	
	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}
	
	public static void main(String[] args) {
		LocalDate_prueba fecha1 = new LocalDate_prueba(LocalDate.of(2020, 10, 13));
		System.out.println("Fecha original: " + fecha1.getFecha());
		
		String fechaForm_dd_mm_yyyy = fecha1.getFecha().format(DateTimeFormatter.ofPattern("dd-MM-yyyy"));
		System.out.println("fecha formateada: " + fechaForm_dd_mm_yyyy);
		
		System.out.println("fin del trayecto");
	}

}
