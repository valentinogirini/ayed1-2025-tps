"""Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo
números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""

def sumar_cadenas_numericas(cadena_a: str, cadena_b: str) -> float | int:
    """
    Suma dos números reales representados como cadenas de caracteres.

    Precondición: cadena_a y cadena_b son cadenas no vacías.

    Postcondición:
    - retorna la suma como número real si ambas cadenas son válidas.
    - retorna -1 si alguna de las cadenas no representa un número real válido.
    """
    try:
        numero_a = float(cadena_a)
        numero_b = float(cadena_b)
        return numero_a + numero_b
    except ValueError:
        return -1


def main() -> None:
    """
    Solicita al usuario dos números reales en formato de cadena y muestra su suma.

    Precondición: ninguna.

    Postcondición:
    - imprime el resultado de la suma si los valores son válidos.
    - imprime un mensaje de error si alguna entrada no es válida.
    """
    cadena_a = input("Ingrese el primer número real: ").strip()
    cadena_b = input("Ingrese el segundo número real: ").strip()

    resultado = sumar_cadenas_numericas(cadena_a, cadena_b)

    if resultado == -1:
        print("Error: una o ambas cadenas no son números reales válidos.")
    else:
        if resultado.is_integer():
            print(f"Resultado de la suma: {int(resultado)}")
        else:
            print(f"Resultado de la suma: {resultado}")


if __name__ == "__main__":
    main()

