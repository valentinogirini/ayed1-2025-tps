"""Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas."""


def producto(a: int, b: int) -> int:
    """
    Calcula el producto de dos números enteros mediante sumas sucesivas.

    Precondición: a y b deben ser números enteros.

    Postcondición: devuelve el producto de a y b sin utilizar el operador *.
    """
    if b == 0:
        return 0

    if b < 0:
        return -producto(a, -b)

    return a + producto(a, b - 1)


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se muestra por pantalla el resultado del producto entre ambos números.
    """
    try:
        a = int(input("Ingrese el primer número (a): "))
        b = int(input("Ingrese el segundo número (b): "))
        resultado = producto(a, b)
        print(f"\nEl producto de {a} y {b} es: {resultado}")
    except ValueError:
        print("Error: debe ingresar números enteros válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()