package fp.vino;

import java.util.*;

public class VinotecaBucles implements Vinoteca{
	private Set<Vino> vinos;
	
	public VinotecaBucles() {
		this.vinos = null;
	}
	
	public VinotecaBucles(Collection<Vino> coleccion) {
		this.vinos = new HashSet<>(coleccion);
	}
	
	public Integer calcularVinosDePais(String pais) {
		Integer res=0;
		for(Vino v:vinos) {
			if(v.pais().equals(pais)) {
				res+=1;
			}
		}
		return res;
	}

	public List<Vino> obtenerVinoRangoPuntos(Integer inf, Integer sup){
		List<Vino> res= new ArrayList<Vino>();
		for(Vino v : vinos) {
			if(v.puntos()>= inf && v.puntos()<=sup) {
				res.add(v);
			}if(inf>sup) {
				throw new IllegalArgumentException(
						"El límite inferior no puede ser mayor que el superior");
			}
		}return res;
	}
	public Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral) {
		Integer res=0;
		for(Vino v: vinos) {
			if(v.pais().equals(pais) && v.puntos()>umbral) {
				res+=1;
			}
		}return res;
	}
	public Set<Vino> obtenerVinosBaratos(Double precio){
		Set<Vino> res= new HashSet<Vino>();
		for(Vino v: vinos) {
			if(v.precio()<precio) {
				res.add(v);
			}
		}return res;
	}
	
	public Boolean existeVinoDeUvaRegion(String region, String uva) {
		Boolean res= false;
		for(Vino v:vinos) {
			if(v.region().equals(region) && v.uva().equals(uva)) {
				res=true;
			}
		}return res;
		
	}
	public Set<String> calcularUvasDeRegion(String region){
		Set<String> res= new HashSet<String>();
		for(Vino v:vinos) {
			if(v.region().equals(region)) {
				res.add(v.uva());
			}
		}return res;
	}
	public Integer calcularTotalPuntosVinosDeRegion(String region) {
		Integer res=0;
		for(Vino v: vinos) {
			if(v.region().equals(region)) {
				res+=v.puntos();
			}
		}return res;
	}

	public Double calcularMediaPuntosVinosDeUva(String uva) {
		Integer total=0;
		Integer contador=0;
		for(Vino v: vinos) {
			if(v.uva().equals(uva)) {
				total+=v.puntos();
				contador+=1;
			}
		}Double res=(double) (total/contador);
		return res;
	}
	public Vino obtenerVinoMejorPuntuado() {
		Vino res= null;
		for(Vino v:vinos) {
			if(res==null || v.puntos()>res.puntos()) {
				res=v;}
		}return res;

		
	}
	public Vino obtenerVinoMejorPuntuadoDePais(String pais) {
		Vino res=null;
		List<Vino> lista= new ArrayList<Vino>();
		for(Vino v:vinos) {
			if(v.pais().equals(pais) && res==null || v.puntos()>res.puntos()) {
				lista.add(v);
				res=v;
			}	
		}return res;
	}
	public List<Vino> obtenerNVinosRegionOrdenadosPrecio(Integer n,String region){
		List<Vino> lista= new ArrayList<Vino>();
		for(Vino v: vinos) {
			if(v.region().equals(region)) {
				lista.add(v);
			}
		}
		lista.sort(Comparator.comparing(Vino::precio).reversed());
		return lista.subList(0, Math.min(n, lista.size()));
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
