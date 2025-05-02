package fp.lexico;

import java.util.*;

public class Lexico {
	private SortedSet<String> palabras;
	private Integer total_palabras;
	
	public Lexico() {
		this.palabras = new TreeSet<>();
		this.total_palabras = 0;
	}
	
	public Lexico(Collection<String> c) {
		
		this.palabras = new TreeSet<>(minuscula(c));
		this.total_palabras = this.palabras.size();
	}
	
	public Collection<String> minuscula(Collection<String> l){
		Collection<String> res = new ArrayList<>();
		for(String i: l) {
			res.add(i.toLowerCase());
		}
		return res;
	}
	
	
	public SortedSet<String> getPalabras(){
		return new TreeSet<String>(this.palabras);		//Para que se haga una copia y no se modifique el original
	}
	
	public Integer getTotalPalabras() {
		return total_palabras;
	}
	
	
	public boolean equals(Object o) {
		if(this == o) return true;
		if(o instanceof Lexico) {
			Lexico oParse = (Lexico) o;
			return this.palabras.equals(oParse.palabras);
		}
		return false;
	}

	
	@Override
	public String toString() {
		return "Lexico [palabras=" + palabras + ", total_palabras=" + total_palabras + ", getPalabras()="
				+ getPalabras() + ", getTotalPalabras()=" + getTotalPalabras() + ", getClass()=" + getClass()
				+ ", hashCode()=" + hashCode() + ", toString()=" + super.toString() + "]";
	}
	
	
	//Otras operaciones
	public void agregarPalabras(String palabra) {
		palabras.add(palabra.toLowerCase());
	}
	
	public void agregarPalabras(Collection<String> palabras) {
		palabras.addAll(minuscula(palabras));
	}
	
	public Set<String> getPalabrasComunes(Lexico lexico) {
	    Set<String> res = getPalabras();
	    res.retainAll(lexico.getPalabras());
	    return res;
	}
	
	public Set<String> getTodasPalabras(Lexico lexico){
		Set<String> res = getPalabras();
		res.addAll(lexico.getPalabras());
		return res;
	}
	
	public Set<String> getDiferenciaPalabras(Lexico lexico){
		Set<String> res = getPalabras();
	    res.retainAll(lexico.getPalabras());
	    
	    Set<String> dif = lexico.getPalabras();
	    dif.removeAll(res);
	    return dif;
	}
	
	
}
