"""La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""

import math

def calcular_raiz_cuadrada(numero: float | int) -> float:
    """
    Calcula la raíz cuadrada de un número.

    Precondición: numero es un número real.

    Postcondición:
    - retorna la raíz cuadrada si numero >= 0.
    - lanza ValueError si numero es negativo.
    """
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(numero)


def main() -> None:
    """
    Solicita al usuario un número y muestra su raíz cuadrada.

    Precondición: ninguna.

    Postcondición:
    - imprime la raíz cuadrada si el número es válido.
    - imprime un mensaje de error si el número es negativo.
    - imprime un mensaje de error si la entrada no se puede convertir a número.
    """
    entrada = input("Ingrese un número: ").strip()

    try:
        numero = float(entrada)
    except ValueError:
        print("Error: la entrada no es un número válido.")
        return

    try:
        if numero.is_integer():
            numero = int(numero)
        resultado = calcular_raiz_cuadrada(numero)
        if resultado.is_integer():
            print(f"La raíz cuadrada de {numero} es {int(resultado)}")
        else:
            print(f"La raíz cuadrada de {numero} es {resultado}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
