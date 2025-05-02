package fp.universidad.tipos.test;

import java.util.List;

import fp.universidad.tipos.Despacho;
import fp.universidad.tipos.Espacio;
import fp.universidad.tipos.FactoriaUniversidad;
import fp.universidad.tipos.TipoEspacio;

public class TestFactoriaUniversidad {

	public static void main(String[] args) {
		List<Espacio> e1 = FactoriaUniversidad.leeEspacios("src/data/espacios.csv");
		
		//System.out.println(e1);
		
		Espacio espacio1 = new Espacio(TipoEspacio.TEORIA, "biblio", 200);
		
		Despacho despacho1 = new Despacho(null);
		
		List<Despacho> d1 = FactoriaUniversidad.leeDespachos("src/data/despachos.csv");
		
		System.out.println(d1);

	}

}
