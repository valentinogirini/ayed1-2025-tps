"""Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N²), de tal forma que ningún número se repita. 
Imprimir la matriz por pantalla."""

import random
from typing import List


def generar_matriz_aleatoria(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N con números enteros únicos al azar
    en el intervalo [0,N²), sin repeticiones.

    Precondición: n es un entero positivo.

    Postcondición: retorna una lista de listas de tamaño N×N con números aleatorios únicos.
    """
    if not isinstance(n, int):
        raise TypeError("El tamaño N debe ser un número entero.")
    if n <= 0:
        raise ValueError("El tamaño N debe ser un entero positivo.")

    numeros = random.sample(range(n * n), n * n)

    it = iter(numeros)
    matriz = [list(next(it) for _ in range(n)) for _ in range(n)]

    return matriz


def imprimir_matriz(matriz: List[List[int]]) -> None:
    """
    Imprime una matriz en formato tabular legible.

    Precondición: matriz es una lista bidimensional cuadrada.

    Postcondición: muestra la matriz en consola, formateada.
    """
    print()
    _ = [print("\t".join(f"{num:5d}" for num in fila)) for fila in matriz]
    print()


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se muestra una matriz N×N con números aleatorios únicos.
    """
    print("--- Generador de Matriz Aleatoria Única ---\n")
    try:
        entrada = input("Ingrese el tamaño N de la matriz cuadrada: ").strip()
        if not entrada.isdigit():
            raise ValueError("Debe ingresar un número entero positivo.")

        n = int(entrada)
        matriz = generar_matriz_aleatoria(n)

        print(f"\nMatriz {n}x{n} con números aleatorios únicos:")
        imprimir_matriz(matriz)

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
