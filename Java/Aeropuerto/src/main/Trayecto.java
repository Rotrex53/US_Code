package main;

import utiles.Checkers;

public record Trayecto(String origen, String destino) {
	public Trayecto {
		Checkers.check("Trayecto.Trayecto::El origen y el destino no pueden ser el mismo", 
						!origen.equals(destino));
	}
}
