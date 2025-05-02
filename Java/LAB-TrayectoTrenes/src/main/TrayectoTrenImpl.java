package main;

import java.time.Duration;
import java.time.LocalTime;
import java.util.List;

public class TrayectoTrenImpl implements TrayectoTren{
	private String CodigoTren;
	private String NombreTrayecto;
	private TipoTren Tipo;
	private List<String> Estaciones;
	private List<LocalTime> HorasSalidas;
	private List<LocalTime> HorasLlegadas;
	private LocalTime HoraSalida;
	private LocalTime HoraLlegada;
	private Duration DuracionTrayecto;
	
	public TrayectoTrenImpl(String CodigoTren, String NombreTrayecto, TipoTren Tipo, 
			String EstacionPrim, String EstacionUlt, LocalTime HoraSalida,
			LocalTime HoraLlegada) {
		Checkers();
		this.CodigoTren = CodigoTren;
		this.NombreTrayecto = NombreTrayecto;
		this.Tipo = Tipo;
		this.Estaciones.addFirst(EstacionPrim);
		this.Estaciones.addLast(EstacionUlt);
		this.HorasSalidas.add(HoraSalida);
		this.HorasLlegadas.add(null);
		this.HoraSalida = null;
		this.HoraLlegada = HoraLlegada;
		this.DuracionTrayecto = Duration.between(HoraSalida, HoraLlegada);
	}
	
	public void Checkers() {
		CheckCodigo(CodigoTren);
		CheckHorasSalidas(HorasSalidas);
		CheckHoraLlegada(HoraLlegada);
		CheckSalidaLlegada(HoraSalida, HoraLlegada);
	}
	
	private void CheckSalidaLlegada(LocalTime HoraSalida, LocalTime HoraLlegada) {
		if(HoraSalida.isAfter(HoraLlegada) || HoraLlegada.isBefore(HoraSalida)) {
			throw new IllegalArgumentException("Horas inválidas");
		}
	}
	
	private void CheckHorasSalidas(List<LocalTime> HorasSalidas) {
		if(HorasSalidas==null) {
			throw new IllegalArgumentException("Hora inválida");
		}
	}
	
	private void CheckHoraLlegada(LocalTime HoraLlegada) {
		if(HoraLlegada==null) {
			throw new IllegalArgumentException("Hora inválida");
		}
	}
	
	private void CheckCodigo(String codigoTren) {
		if(codigoTren.length()!=5 || !codigoTren.matches("\\d+")) {
			throw new IllegalArgumentException("Codigo inválido");
		}
	}
	
	
	
	public String getEstacionPrim(List<String> Estaciones) {
		String EstacionPrim = Estaciones.getFirst();
		return EstacionPrim;
	}
	
	public String getEstacionUlt(List<String> Estaciones) {
		String EstacionUlt = Estaciones.getFirst();
		return EstacionUlt;
	}
	
	@Override
	public String getCodigoTren() {
		// TODO Auto-generated method stub
		return CodigoTren;
	}

	@Override
	public String getNombre() {
		// TODO Auto-generated method stub
		return NombreTrayecto;
	}

	@Override
	public List<String> getEstaciones() {
		// TODO Auto-generated method stub
		return Estaciones;
	}

	@Override
	public List<LocalTime> getHorasSalida() {
		// TODO Auto-generated method stub
		return HorasSalidas;
	}

	@Override
	public List<LocalTime> getHorasLlegada() {
		// TODO Auto-generated method stub
		return HorasLlegadas;
	}

	@Override
	public LocalTime getHoraSalida(String estacion) {
		if(!Estaciones.contains(estacion) || Estaciones.getLast() == estacion) return null;
		return HoraSalida;
	}

	@Override
	public LocalTime getHoraLlegada(String estacion) {
		// TODO Auto-generated method stub
		return HoraLlegada;
	}

	@Override
	public Duration getDuracionTrayecto() {
		// TODO Auto-generated method stub
		return DuracionTrayecto;
	}

	@Override
	public void anadirEstacionIntermedia(Integer posicion, String estacion, LocalTime horaLlegada,
			LocalTime horaSalida) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void eliminarEstacionIntermedia(String estacion) {
		// TODO Auto-generated method stub
		
	}
	
}
