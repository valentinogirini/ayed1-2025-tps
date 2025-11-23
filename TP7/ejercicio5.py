"""Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas."""

def resto(dividendo: int, divisor: int) -> int:
    """
    Calcula el resto de la división entre dos números enteros mediante restas sucesivas.

    Precondición:
    - divisor debe ser distinto de 0.
    - dividendo y divisor deben ser enteros.

    Postcondición: devuelve el resto entero de dividir dividendo por divisor.
    """
    if divisor == 0:
        raise ValueError("No se puede dividir por cero.")

    signo = -1 if dividendo < 0 else 1

    dividendo = abs(dividendo)
    divisor = abs(divisor)

    if dividendo < divisor:
        return signo * dividendo

    return resto(dividendo - divisor, divisor) * signo


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se muestra por pantalla el resto de la división.
    """
    try:
        dividendo = int(input("Ingrese el dividendo: "))
        divisor = int(input("Ingrese el divisor: "))

        resultado = resto(dividendo, divisor)
        print(f"\nEl resto de dividir {dividendo} entre {divisor} es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()