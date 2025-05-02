package main;
import java.util.*;

public class Collections_test {
    public static void main(String[] args) {
        // Ejemplo de addAll
        List<String> lista = new ArrayList<>();
        Collections.addAll(lista, "Manzana", "Banana", "Cereza", "Durazno");
        System.out.println("addAll: " + lista);
        
        // Ejemplo de fill
        Collections.fill(lista, "Naranja");
        System.out.println("fill: " + lista);
        
        // Ejemplo de max
        List<Integer> numeros = Arrays.asList(10, 20, 5, 40, 30);
        Integer maxValor = Collections.max(numeros);
        System.out.println("max: " + maxValor);
        
        // Ejemplo de min
        Integer minValor = Collections.min(numeros);
        System.out.println("min: " + minValor);
        
        // Ejemplo de reverse
        Collections.reverse(numeros);
        System.out.println("reverse: " + numeros);
        
        // Ejemplo de shuffle
        Collections.shuffle(numeros);
        System.out.println("shuffle: " + numeros);
        
        // Ejemplo de sort
        Collections.sort(numeros);
        System.out.println("sort: " + numeros);
    }
}
