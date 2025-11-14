"""Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna representa 
el día de la semana y cada fila a una de sus fábricas.

a. Crear una matriz con datos generados al azar para N fábricas durante una
semana, considerando que la capacidad máxima de fabricación es de 150
unidades por día y puede suceder que en ciertos días no se fabrique ninguna.

b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.

c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).

d. Cuál es el día más productivo, considerando todas las fábricas combinadas.

e. Crear una lista por comprensión que contenga la menor cantidad fabricada
por cada fábrica."""

import random
from typing import List, Tuple


def generar_matriz_produccion(fabricas: int, dias: List[str]) -> List[List[int]]:
    """
    Genera una matriz de producción aleatoria para N fábricas durante los días especificados.

    Precondición:
    - fabricas > 0
    - dias es una lista no vacía.

    Postcondición: retorna una matriz con valores entre 0 y 150 inclusive.
    """
    if not isinstance(fabricas, int) or fabricas <= 0:
        raise ValueError("El número de fábricas debe ser un entero positivo.")
    if not dias:
        raise ValueError("La lista de días no puede estar vacía.")

    return [[random.randint(0, 150) for _ in dias] for _ in range(fabricas)]


def mostrar_matriz(matriz: List[List[int]], dias: List[str]) -> None:
    """
    Muestra la matriz de producción en formato tabular.

    Precondición:
    - matriz rectangular.
    - dias tiene la misma longitud que las columnas de la matriz.

    Postcondición: imprime la matriz con encabezados.
    """
    print("\n--- Producción Semanal de Bicicletas ---")
    print(" " * 12 + "".join(f"{dia:>12}" for dia in dias))
    for i, fila in enumerate(matriz, start=1):
        print(f"Fábrica {i:<4} " + "".join(f"{valor:>12}" for valor in fila))
    print()


def total_por_fabrica(matriz: List[List[int]]) -> List[int]:
    """
    Calcula la cantidad total producida por cada fábrica.

    Precondición: matriz válida.

    Postcondición: retorna una lista con el total por fila.
    """
    return [sum(fila) for fila in matriz]


def fabrica_mas_productiva_en_dia(matriz: List[List[int]], dias: List[str]) -> Tuple[int, str, int]:
    """
    Determina la fábrica y el día de mayor producción individual.

    Precondición: matriz no vacía.

    Postcondición: retorna (nro_fabrica, dia, maximo).
    """
    maximo = max(max(fila) for fila in matriz)
    for i, fila in enumerate(matriz):
        if maximo in fila:
            dia = dias[fila.index(maximo)]
            return i + 1, dia, maximo
    raise ValueError("No se pudo determinar el máximo.")


def dia_mas_productivo(matriz: List[List[int]], dias: List[str]) -> Tuple[str, int]:
    """
    Calcula el día más productivo sumando todas las fábricas.

    Precondición: matriz y días válidos.

    Postcondición: retorna total producido y nombre del día.
    """
    totales = [sum(col) for col in zip(*matriz)]
    indice_max = totales.index(max(totales))
    return dias[indice_max], totales[indice_max]


def menores_por_fabrica(matriz: List[List[int]]) -> List[int]:
    """
    Devuelve una lista con la menor cantidad fabricada por cada fábrica.

    Precondición: matriz válida.

    Postcondición: retorna una lista de mínimos por fila.
    """
    return [min(fila) for fila in matriz]


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: imprime todos los resultados.
    """
    print("--- Fábrica de Bicicletas ---\n")
    try:
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        n = int(input("Ingrese la cantidad de fábricas: "))

        matriz = generar_matriz_produccion(n, dias)
        mostrar_matriz(matriz, dias)

        totales = total_por_fabrica(matriz)
        print("Total producido por cada fábrica:")
        for i, total in enumerate(totales, start=1):
            print(f"  Fábrica {i}: {total} bicicletas")
        print()

        fabrica, dia, maximo = fabrica_mas_productiva_en_dia(matriz, dias)
        print(f"La fábrica más productiva en un solo día fue la Fábrica {fabrica}, el {dia}, con {maximo} bicicletas.\n")

        dia_top, total_dia = dia_mas_productivo(matriz, dias)
        print(f"El día más productivo fue el {dia_top} con un total de {total_dia} bicicletas.\n")

        minimos = menores_por_fabrica(matriz)
        print("Menor producción por fábrica:")
        print(minimos)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
