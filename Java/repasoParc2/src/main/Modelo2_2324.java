package main;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.*;
import java.util.stream.Collectors;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.Objects;
import java.util.function.Function;
import java.util.function.Predicate;

public class Modelo2_2324 {

	public enum Estado {
		ARCHIVADO, EN_DESARROLLO, EN_MANTENIMIENTO, ACTIVO
	}

	public static class Commit implements Comparable<Commit> {
		private final String codigo;
		private final String mensaje;
		private final LocalDateTime fechaHora;

		private static final Pattern CODIGO_VALIDO = Pattern.compile("^[a-z0-9]{7}$");

		public Commit(String codigo, String mensaje, LocalDateTime fechaHora) {
			if (!CODIGO_VALIDO.matcher(codigo).matches()) {
				throw new IllegalArgumentException("Código inválido: debe tener 7 caracteres alfanuméricos minúsculos");
			}
			this.codigo = codigo;
			this.mensaje = mensaje;
			this.fechaHora = fechaHora;
		}

		public String getCodigo() {
			return codigo;
		}

		public String getMensaje() {
			return mensaje;
		}

		public LocalDateTime getFechaHora() {
			return fechaHora;
		}

		@Override
		public int compareTo(Commit otro) {
			int comparacion = this.fechaHora.compareTo(otro.fechaHora);
			return comparacion != 0 ? comparacion : this.codigo.compareTo(otro.codigo);
		}

		@Override
		public boolean equals(Object o) {
			if (this == o)
				return true;
			if (!(o instanceof Commit))
				return false;
			Commit commit = (Commit) o;
			return codigo.equals(commit.codigo);
		}

		@Override
		public int hashCode() {
			return Objects.hash(codigo);
		}

		@Override
		public String toString() {
			return String.format("Commit[codigo=%s, mensaje=%s, fechaHora=%s]", codigo, mensaje, fechaHora);
		}
	}

	public static class Repositorio {
		private final String nombre;
		private String propietario;
		private final Set<String> lenguajes;
		private boolean privado;
		private double calificacion;
		private Estado estado;
		private final List<Commit> commits;

		public Repositorio(String nombre, String propietario) {
			this.nombre = nombre;
			this.propietario = propietario;
			this.lenguajes = new HashSet<>();
			this.privado = true;
			this.calificacion = 0.0;
			this.estado = Estado.EN_DESARROLLO;
			this.commits = new ArrayList<>();
		}

		public String getNombre() {
			return nombre;
		}

		public String getPropietario() {
			return propietario;
		}

		public void setPropietario(String propietario) {
			this.propietario = propietario;
		}

		public Set<String> getLenguajes() {
			return Collections.unmodifiableSet(lenguajes);
		}

		public boolean esPrivado() {
			return privado;
		}

		public boolean esPublico() {
			return !privado;
		}

		public void setPrivado(boolean privado) {
			this.privado = privado;
		}

		public double getCalificacion() {
			return calificacion;
		}

		public void setCalificacion(double calificacion) {
			if (calificacion < 0 || calificacion > 10) {
				throw new IllegalArgumentException("La calificación debe estar entre 0 y 10");
			}
			this.calificacion = calificacion;
		}

		public Estado getEstado() {
			return estado;
		}

		public void setEstado(Estado estado) {
			this.estado = estado;
		}

		public List<Commit> getCommits() {
			return Collections.unmodifiableList(commits);
		}

		public void añadirCommit(Commit commit) {
			this.commits.add(commit);
		}

		public int getNumeroCommits() {
			return commits.size();
		}

		public LocalDateTime getUltimaActualizacion() {
			return commits.stream().map(Commit::getFechaHora).max(Comparator.naturalOrder()).orElse(null);
		}

		public void añadirLenguaje(String lenguaje) {
			this.lenguajes.add(lenguaje);
		}

		@Override
		public boolean equals(Object o) {
			if (this == o)
				return true;
			if (!(o instanceof Repositorio))
				return false;
			Repositorio that = (Repositorio) o;
			return nombre.equals(that.nombre) && propietario.equals(that.propietario);
		}

		@Override
		public int hashCode() {
			return Objects.hash(nombre, propietario);
		}

		@Override
		public String toString() {
			return String.format(
					"Repositorio[nombre=%s, propietario=%s, privado=%b, calificacion=%.2f, estado=%s, lenguajes=%s, numCommits=%d]",
					nombre, propietario, privado, calificacion, estado, lenguajes, getNumeroCommits());
		}
		
	}
	
	public static class GitRepos {
        private List<Repositorio> repositorios;

        // Constructor vacío inicializa lista vacía
        public GitRepos() {
            this.repositorios = new ArrayList<>();
        }

        // Constructor con lista inicial
        public GitRepos(List<Repositorio> repositorios) {
            this.repositorios = repositorios != null ? repositorios : new ArrayList<>();
        }

        // Getter
        public List<Repositorio> getRepositorios() {
            return repositorios;
        }

        // Setter
        public void setRepositorios(List<Repositorio> repositorios) {
            this.repositorios = repositorios;
        }

        // Método para añadir un repositorio
        public void addRepositorio(Repositorio repo) {
            if (repo != null) {
                repositorios.add(repo);
            }
        }

        // Método para eliminar un repositorio
        public boolean removeRepositorio(Repositorio repo) {
            return repositorios.remove(repo);
        }
        
        
        
//    	5. Suponga definido un tipo contenedor llamado GitRepos que tiene una propiedad de tipo List<Repositorio>
//    	llamada repositorios implemente los siguientes tratamientos secuenciales en ese contenedor.
//    	a) Método que devuelve un Map<Estado, Integer> en el que las claves son el estado del repositorio y el valor el
//    	número total de repositorios actualizados en el estado dado por la clave. Resuélvalo con stream. (2 ptos)
    	public Map<Estado, Integer> numRepositoriosPorEstado () {
    		return getRepositorios().stream()
    				.collect(Collectors.groupingBy(
    						Repositorio::getEstado,
    						Collectors.collectingAndThen(
    											Collectors.counting(), 
    											Long::intValue))
    						);			
    	}
    	
//    	b) Método que devuelve el commit más reciente de todos los repositorios privados. Si no se puede calcular,
//    	devuelve null. Resuélvalo con Streams. (2 ptos)
    	public Commit commitMasRecienteRepositorioPrivado() {
    		return getRepositorios().stream()
    				.filter(x -> x.esPrivado())
    				.flatMap(x -> x.getCommits().stream())
    				.max(Comparator.comparing(x -> x.getFechaHora()))
    				.orElse(null);
    	}
    	
//    	c) Método que devuelve un Map en el que la clave son los años de la última actualización, y los valores una lista
//    	con los nombres de los repositorios cuya fecha de actualización se ha realizado en el año dado por la clave.
//    	Resuélvalo con bucles. (2 ptos)
    	public Map<Integer,List<String>> repositoriosPorAnyo(){
    		Map<Integer, List<String>> map = new HashMap<>();
    		for(Repositorio r: repositorios) {
    			if(!map.containsKey(r.getUltimaActualizacion().getYear())) {
    				map.put(r.getUltimaActualizacion().getYear(), new ArrayList<>());
    			}
    			map.get(r.getUltimaActualizacion().getYear()).add(r.getNombre());
    		}
    		return map;
    	}
    }

	public static List<Character> f1(Set<String> c) {
		List<Character> res = c.stream().filter(s -> s.length() % 3 == 0).map(s -> s.charAt(0)).sorted().limit(2)
				.collect(Collectors.toList());
		return res; // ["A", "C"]
	}

	// Utils.f1 (Set.of("Pascal", "Java", "C", "C++", "Python", "Ada"))

	public static SortedSet<Integer> f2(Collection<Integer> c, Predicate<Integer> p, Function<Integer, Integer> f) {
		SortedSet<Integer> ss = new TreeSet<>();
		for (Integer n : c) {
			if (p.test(n)) {
				ss.add(f.apply(n));
			}
		}
		return ss; // {4, 64}
	}

	// Utils.f2(List.of(2, 3, 7, 8), e -> e%2 == 0, e -> e * e)

	public static SortedMap<String, Integer> f3() {
		Comparator<String> c = Comparator.comparing(String::length).reversed();
		SortedMap<String, Integer> sm = new TreeMap<String, Integer>(c);
		String s = "";
		String cad = "HOLA";
		for (int i = 1; i < 4; i++) {
			s = cad.substring(0, i);		//H			HO			HOL
			sm.put(s, i);					//("H", 1)	("HO", 2)	("HOL", 3)
		}
		sm.remove("H");
		return sm;							//{"HOL"=3, "HO"=2}
	}

	// Utils.f3 ()
	
	//4. Declare una variable (con su tipo) y defina los siguientes predicados, funciones y comparadores. (1 pto)
	
	//a) Predicado p1 que, dado un repositorio, indique si el año de su última actualización es el año en curso.
	Predicate<Repositorio> p1 = x -> x.getUltimaActualizacion().getYear()==LocalDate.now().getYear();
	
	//b) Predicado p3 que, dado un repositorio, indique si la última actualización NO ha sido en el año en curso y tiene
//	entre sus lenguajes de programación el lenguaje Java. Suponga definido un predicado p2 que indica si un
//	repositorio tiene entre sus lenguajes el lenguaje Java. Reutilice p1 y p2
	Predicate<Repositorio> p2 = x -> x.getLenguajes().contains("Java");
	Predicate<Repositorio> p3 = p2.and(p1.negate());
	
//	c) Función f1 que, dado un repositorio, devuelva una lista con los tres primeros commits de la lista de commits.
//	Suponga que todos los repositorios tienen más de tres commits
	Function<Repositorio, List<Commit>> f1 = x -> x.getCommits().subList(0, 3);
	
//	d) Función f3 que tome un repositorio, y devuelva una lista de los tres primeros commits, ordenada por fecha y
//	hora. Suponga definida una función f2 que toma una lista de commits, y devuelve otra lista de commits,
//	ordenada por fecha y hora. Reutilice f1 y f2.
	Function<List<Commit>, List<Commit>> f2 = x -> x.stream().sorted(Comparator.comparing(Commit::getFechaHora)).collect(Collectors.toList());
	Function<Repositorio, List<Commit>> f3 = f1.andThen(f2);
	
//	e) Comparador c1 que defina un criterio de orden para ordenar repositorios por la fecha de última actualización
//	(de más reciente a más antigua) y a igualdad de fecha, por número de commits. Nota: No se preocupe de los
//	posibles problemas que pueda tener el compilador a la hora de deducir los tipos.
	Comparator<Repositorio> c1 = Comparator.comparing(Repositorio::getUltimaActualizacion).reversed().thenComparing(Repositorio::getNumeroCommits);


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
