"""Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves."""

def generar_diccionario_cuadrados() -> dict[int, int]:
    """
    Genera un diccionario con los números del 1 al 20 y sus cuadrados.

    Precondición: ninguna.

    Postcondición: retorna un diccionario donde cada clave es un número entre 1 y 20,
    y su valor asociado es el cuadrado de dicha clave.
    """
    return {i: i ** 2 for i in range(1, 21)}


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: imprime el diccionario generado con los números del 1 al 20
    y sus cuadrados.
    """
    diccionario = generar_diccionario_cuadrados()
    print("Diccionario de cuadrados del 1 al 20:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()
