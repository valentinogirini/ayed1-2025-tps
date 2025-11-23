"""Escribir una función que devuelva la suma de los N primeros números naturales."""


def suma_naturales(n: int) -> int:
    """
    Calcula la suma de los N primeros números naturales.

    Precondición: n debe ser un entero mayor o igual que 1.

    Postcondición: devuelve la suma total de los N primeros números naturales.
    """
    if n < 1:
        raise ValueError("El número debe ser mayor o igual que 1.")

    if n == 1:
        return 1

    return n + suma_naturales(n - 1)


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se muestra por pantalla la suma de los N primeros números naturales.
    """
    try:
        n = int(input("Ingrese un número entero positivo: "))
        resultado = suma_naturales(n)
        print(f"\nLa suma de los {n} primeros números naturales es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()