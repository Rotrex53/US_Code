package main;

import java.util.*;

public class MainSortedSet {
	private TreeSet<Integer> n1;
	private TreeSet<Integer> n2;
	
	public MainSortedSet(TreeSet<Integer> n1, TreeSet<Integer> n2) {
		this.n1 = n1;
		this.n2 = n2;
		
	}
	
	public Integer numFibonacci(Integer n) {
		if (n <= 0) return 0;
        if (n == 1) return 1;
        return numFibonacci(n - 1) + numFibonacci(n - 2);
	}
	
	public TreeSet<Integer> numFibonacci1(){
		for (int i = 0; i<10; i++) {
			n1.add(numFibonacci(i));
		}
		return n1;
	}
	
	public TreeSet<Integer> numFibonacci2(){
		for (int i = 0; i<10; i++) {
			Integer sumatorio = numFibonacci(i) + 1;
			n2.add(sumatorio);
		}
		return n2;
	}
	
	public Set<Integer> subConj(){
		return null;
	}
	
	public String toString() {
		return numFibonacci1().getFirst() + ", " + numFibonacci2().getLast();
	}
}
