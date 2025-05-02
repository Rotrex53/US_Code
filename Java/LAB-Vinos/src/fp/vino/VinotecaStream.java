package fp.vino;

import java.util.*;

public class VinotecaStream implements Vinoteca{
	private Set<Vino> vinos;

	public VinotecaStream(){
		this.vinos = null;
	}
	
	public VinotecaStream(Collection<Vino> coleccion) {
		this.vinos = new HashSet<>(coleccion);
	}
	
	@Override
	public void agregarVino(Vino v) {
		vinos.add(v);
	}

	@Override
	public void eliminarVino(Vino v) {
		vinos.remove(v);
	}

	@Override
	public Integer obtenerNumeroVinos() {
		return vinos.size();
	}

	@Override
	public Boolean contieneVino(Vino v) {
		return vinos.contains(v);
	}

	@Override
	public void agregarVinos(Collection<Vino> v) {
		vinos.addAll(v);		
	}

	@Override
	public Boolean contieneVinos(Collection<Vino> v) {
		return vinos.containsAll(v);
	}

	@Override
	public Integer calcularVinosDePais(String pais) {
		return null;
	}

	@Override
	public List<Vino> obtenerVinoRangoPuntos(Integer inf, Integer sup) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Set<Vino> obtenerVinosBaratos(Double precio) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Boolean existeVinoDeUvaRegion(String region, String uva) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Set<String> calcularUvasDeRegion(String region) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Integer calcularTotalPuntosVinosDeRegion(String region) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Double calcularMediaPuntosVinosDeUva(String uva) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Vino obtenerVinoMejorPuntuado() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Vino obtenerVinoMejorPuntuadoDePais(String pais) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public List<Vino> obtenerNVinosRegionOrdenadosPrecio(Integer n, String region) {
		// TODO Auto-generated method stub
		return null;
	}
	
	
	
	public String toString() {
		return obtenerNumeroVinos().toString();
	}
	
	public boolean equals(Object o) {
		if(this==o) return true;
		if(o instanceof Vinoteca) {
			Vinoteca vinoteca = (Vinoteca) o;
			return vinoteca.contieneVinos(vinos);
		}
		return false;
	}
}
