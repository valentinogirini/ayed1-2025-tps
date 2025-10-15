"""Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los
caracteres de la subcadena no necesariamente deben estar en forma consecutiva
dentro de la cadena, pero sí respetando el orden de los mismos."""

def contar_subcadena(cadena: str, subcadena: str) -> int:
    """
    Cuenta cuántas veces se encuentra la subcadena dentro de la cadena,
    sin diferenciar mayúsculas y minúsculas. Los caracteres de la subcadena
    no necesariamente deben ser consecutivos pero sí respetar el orden.

    Precondición: cadena y subcadena son cadenas no vacías.

    Postcondición: retorna un entero con la cantidad de veces que se puede formar la subcadena
    dentro de la cadena, en orden.
    """
    cadena = cadena.lower()
    subcadena = subcadena.lower()
    cantidad_encontradas = 0
    posicion_cadena = 0

    while posicion_cadena < len(cadena):
        posicion_subcadena = 0
        encontro_coincidencia = False

        for indice in range(posicion_cadena, len(cadena)):
            if cadena[indice] == subcadena[posicion_subcadena]:
                posicion_subcadena += 1
                if posicion_subcadena == len(subcadena):
                    cantidad_encontradas += 1
                    posicion_cadena = indice + 1
                    encontro_coincidencia = True
                    break

        if not encontro_coincidencia:
            break

    return cantidad_encontradas


def main() -> None:
    """
    Solicita una cadena y una subcadena, y muestra la cantidad de coincidencias encontradas.

    Precondición: ninguna.
    
    Postcondición: imprime la cantidad de veces que aparece la subcadena en orden.
    """
    try:
        cadena = input("Ingrese la cadena principal: ").strip()
        subcadena = input("Ingrese la subcadena a buscar: ").strip()

        if not cadena or not subcadena:
            raise ValueError("Ninguna de las cadenas puede estar vacía.")

        cantidad = contar_subcadena(cadena, subcadena)
        print(f"\nCantidad encontrada: {cantidad}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
