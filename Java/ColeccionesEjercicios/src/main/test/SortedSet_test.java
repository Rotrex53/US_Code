package main.test;

import java.util.*;

public class SortedSet_test {
	public static void main(String[] args) {
		SortedSet <Integer> conj1 = new TreeSet <Integer>();
		SortedSet <Integer> conj2 = new TreeSet <Integer>();

		int a = 0, b = 1;
		for(int i = 0; i<10; i++) {
			conj1.add(a);
			int next = a+b;
			b = next;
		}
		
		for (int n:conj1) {
			conj2.add(n+1);
		}
		System.out.println("Primer numero:" + conj1.first());
		System.out.println("Primer numero:" + conj2.first());
	}
}
