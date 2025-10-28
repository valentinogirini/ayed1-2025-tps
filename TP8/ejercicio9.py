"""Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado.
"""

def generar_tabla_multiplicar(n: int) -> dict[int, int]:
    """
    Genera un diccionario con la tabla de multiplicar del número dado.

    Precondición: n es un número entero.

    Postcondición: retorna un diccionario donde las claves son los números del 1 al 12,
    y los valores son los productos de n por dichas claves.
    """
    return {i: n * i for i in range(1, 13)}


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición:
    - solicita un número entero al usuario.
    - muestra la tabla de multiplicar del número ingresado con formato claro.
    """
    try:
        n = int(input("Ingrese un número entero: "))
    except ValueError:
        print("Error: debe ingresar un número entero válido.")
        return

    tabla = generar_tabla_multiplicar(n)
    
    ancho_valor = len(str(n * 12))
    ancho_factor = len(str(12))

    print(f"\nTabla de multiplicar del {n}:")
    for clave, valor in tabla.items():
        print(f"{n} x {clave:>{ancho_factor}} = {valor:>{ancho_valor}}")


if __name__ == "__main__":
    main()
    
    