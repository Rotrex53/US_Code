package main;

import java.time.*;
import java.util.*;

public interface TrayectoTren {
	String getCodigoTren();
	String getNombre();
	List<String> getEstaciones();
	List<LocalTime> getHorasSalida();
	List<LocalTime> getHorasLlegada();
	LocalTime getHoraSalida(String estacion);
	LocalTime getHoraLlegada(String estacion);
	Duration getDuracionTrayecto();
	void anadirEstacionIntermedia(Integer posicion, String estacion, LocalTime horaLlegada, LocalTime horaSalida);
	void eliminarEstacionIntermedia(String estacion);
}
