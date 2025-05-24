package main.metodos;

import java.util.*;

public class Metodos {
	private Map<String, Integer> map = new LinkedHashMap<>();

	
	public Metodos() {
		this.map = map;
	}

	public Map<String, Integer> getMap() {
		return map;
	}

	public void setMap(Map<String, Integer> map) {
		this.map = map;
	}



	public Map<String, Integer> MapClaveValorPorComas(String c){
		String [] trozos = c.split(",");
		
		for(int i = 0; i < trozos.length-1; i+=2) {
			String clave = trozos[i].trim();
			String valorStr = trozos[i+1].trim();
			
			try {
	            Integer valor = Integer.parseInt(valorStr);    // Convierte a Integer
	            map.put(clave, valor);                          // Añade al mapa
	        } catch (NumberFormatException e) {
	            System.out.println("Valor inválido: " + valorStr);
	        }
		}
		return map;
	}
	
	public String toString() {
		return map.toString();
	}
	
	
	

	public static void main(String[] args) {
		//Sección de Datos / INPUT
		Metodos m = new Metodos();
		Map<String, Integer> miMapa = m.MapClaveValorPorComas("clave1 , 10, clave2, 20 , clave3 ,30,clave4, 85, clave5, 94, clave6, 100, claveE, 00");
		
		Metodos mapa = new Metodos();
		Map<String, Integer> MapCompleto = mapa.MapClaveValorPorComas("clave1 , 10, clave2, 20 , clave3 ,30,clave4, 85, clave5, 94, clave6, 100");
		
//		Map<String, Integer> map1 = new HashMap<String, Integer>();
//		map1.put("0", 1);
		
		
		
		
		//Sección de OUTPUT
//		System.out.println(map1);
//		System.out.println(miMapa);
//		miMapa.clear();		
//		System.out.println(miMapa);
//		System.out.println(miMapa.containsKey("clave1"));
//		System.out.println(miMapa.containsValue(11));
//		System.out.println(miMapa.get("clave1"));
//		System.out.println(miMapa.isEmpty());
//		miMapa.clear();
//		System.out.println(miMapa.isEmpty());
//		System.out.println(miMapa.keySet());
//		System.out.println(mapa);
//		System.out.println(MapCompleto);
//		System.out.println(MapCompleto.remove("clave1", 10));
//		System.out.println(MapCompleto);
//		System.out.println(MapCompleto.size());
//		System.out.println(MapCompleto.values());
//		System.out.println(MapCompleto.entrySet());
//		System.out.println(MapCompleto.toString());
//		MapCompleto.putAll(miMapa);
//		System.out.println(MapCompleto);
		

	}

}
