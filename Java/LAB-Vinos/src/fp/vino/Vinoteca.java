package fp.vino;

import java.util.*;

public interface Vinoteca {
	void agregarVino(Vino v);
	void eliminarVino(Vino v);
	Integer obtenerNumeroVinos();
	Boolean contieneVino(Vino v);
	void agregarVinos(Collection<Vino> v);
	Boolean contieneVinos(Collection<Vino> v);
	
	Integer calcularVinosDePais(String pais);
	List<Vino> obtenerVinoRangoPuntos(Integer inf, Integer sup);
	Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral);
	Set<Vino> obtenerVinosBaratos(Double precio);
	Boolean existeVinoDeUvaRegion(String region, String uva);
	Set<String> calcularUvasDeRegion(String region);
	Integer calcularTotalPuntosVinosDeRegion(String region);
	Double calcularMediaPuntosVinosDeUva(String uva);
	Vino obtenerVinoMejorPuntuado();
	Vino obtenerVinoMejorPuntuadoDePais(String pais);
	List<Vino> obtenerNVinosRegionOrdenadosPrecio(Integer n,String region);
}
