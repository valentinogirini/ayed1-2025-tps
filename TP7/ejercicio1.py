"""Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
utilizar cadenas de caracteres."""


def cantidad_digitos(n: int) -> int:
    """
    Calcula la cantidad de dígitos de un número entero.

    Precondición: n debe ser un número entero.

    Postcondición: devuelve la cantidad total de dígitos que componen el número.
    """
    n = abs(n)

    if n < 10:
        return 1

    return 1 + cantidad_digitos(n // 10)


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se muestra por pantalla la cantidad de dígitos del número.
    """
    try:
        numero = int(input("Ingrese un número entero: "))
        resultado = cantidad_digitos(numero)
        print(f"\nEl número {numero} tiene {resultado} dígito(s).")
    except ValueError:
        print("Error: debe ingresar un número entero válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
