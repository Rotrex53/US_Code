package comparadores;

import java.util.Comparator;

public class Comparador2 implements Comparator<Comparadores>{

	@Override
	public int compare(Comparadores c1, Comparadores c2) {
		return c1.getInt2().compareTo(c2.getInt2());
	}
	
}
