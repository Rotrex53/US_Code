package comparadores;

public class Comparadores implements Comparable<Comparadores>{
	private Integer int1;
	private Integer int2;
	
	public Comparadores(Integer int1, Integer int2) {
		this.int1=int1;
		this.int2=int2;
		
	}
	
	public Integer getInt1() {
		return int1;
	}
	
	public void setInt1(Integer i) {
		int1 = i;
	}
	
	public Integer getInt2() {
		return int2;
	}
	
	public void setInt2(Integer i) {
		int2 = i;
	}
	
	
	public Integer sumaDatos(Integer int1, Integer int2) {
		return int1+int2;
	}
	
	public int compareTo(Comparadores c) {
		int res = getInt1().compareTo(c.getInt1());
		if(res==0) {
			res = getInt2().compareTo(c.getInt2());
		}
		return res;
	}
	
	public String toString() {
		return int1 + ", " + int2;
	}
}
