"""Escribir un programa para crear una lista por comprensión con los naipes de la baraja española.
La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla. """

from typing import List

def crear_baraja() -> List[str]:
    """
    Crea una lista con todos los naipes de la baraja española.

    Precondición: ninguna.

    Postcondición: retorna una lista de cadenas con todos los naipes (formato número-palo).
    """
    numeros = [str(n) for n in range(1, 13) if n != 8 and n != 9]
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    return [f"{numero} {palo}" for palo in palos for numero in numeros]


def main() -> None:
    """
    Crea la baraja española y la imprime por pantalla.

    Precondición: ninguna.

    Postcondición: imprime la lista completa de naipes.
    """
    baraja = crear_baraja()
    for naipe in baraja:
        print(naipe)

if __name__ == "__main__":
    main()
