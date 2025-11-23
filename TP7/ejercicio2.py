"""Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal."""


def binario_a_decimal(n: int) -> int:
    """
    Convierte un número binario a su equivalente decimal.

    Precondición:
    - n debe ser un número entero positivo o cero.
    - el número debe estar compuesto solo por dígitos 0 y 1.

    Postcondición: devuelve el valor decimal equivalente al número binario recibido.
    """
    if n < 2:
        return n

    return (n % 10) + 2 * binario_a_decimal(n // 10)


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se muestra por pantalla el número convertido a base decimal.
    """
    try:
        binario = input("Ingrese un número binario: ").strip()
        if not binario or any(c not in "01" for c in binario):
            print("Error: el número debe contener solo dígitos 0 y 1.")
            return

        numero = int(binario)
        resultado = binario_a_decimal(numero)
        print(f"\nEl número binario {binario} equivale a {resultado} en base decimal.")
    except ValueError:
        print("Error: debe ingresar un número binario válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()