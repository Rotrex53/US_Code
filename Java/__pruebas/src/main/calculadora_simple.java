package main;

import java.util.Scanner;
import java.util.Stack;

public class calculadora_simple {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce la operación:");
        String operacion = scanner.nextLine();

        try {
            double resultado = evaluarOperacion(operacion);
            System.out.println("Resultado: " + resultado);
        } catch (Exception e) {
            System.out.println("Operación inválida.");
        }
        scanner.close();
    }

    public static double evaluarOperacion(String expresion) {
        Stack<Double> numeros = new Stack<>();
        Stack<Character> operadores = new Stack<>();
        StringBuilder numero = new StringBuilder();

        for (int i = 0; i < expresion.length(); i++) {
            char c = expresion.charAt(i);

            if (Character.isDigit(c) || c == '.') {
                numero.append(c);
            } else if (c == ' ') {
                continue;
            } else {
                if (numero.length() > 0) {
                    numeros.push(Double.parseDouble(numero.toString()));
                    numero.setLength(0);
                }
                while (!operadores.isEmpty() && prioridad(operadores.peek()) >= prioridad(c)) {
                    double b = numeros.pop();
                    double a = numeros.pop();
                    char op = operadores.pop();
                    numeros.push(operar(a, b, op));
                }
                operadores.push(c);
            }
        }
        if (numero.length() > 0) {
            numeros.push(Double.parseDouble(numero.toString()));
        }

        while (!operadores.isEmpty()) {
            double b = numeros.pop();
            double a = numeros.pop();
            char op = operadores.pop();
            numeros.push(operar(a, b, op));
        }

        return numeros.pop();
    }

    public static int prioridad(char operador) {
        if (operador == '+' || operador == '-') return 1;
        if (operador == '*' || operador == '/') return 2;
        return 0;
    }

    public static double operar(double a, double b, char operador) {
        switch (operador) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return a / b;
            default: throw new IllegalArgumentException("Operador inválido: " + operador);
        }
    }
}
