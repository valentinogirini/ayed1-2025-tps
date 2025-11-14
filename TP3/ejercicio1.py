"""Desarrollar cada una de las siguientes funciones y escribir un programa que permita 
verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:

a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.

b. Ordenar en forma ascendente cada una de las filas de la matriz.

c. Intercambiar dos filas, cuyos números se reciben como parámetro.

d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.

e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)

f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.

g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.

h. Determinar si la matriz es simétrica con respecto a su diagonal principal.

i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.

j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.

NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado."""


from typing import List


def cargar_matriz(n: int) -> List[List[int]]:
    """
    Carga una matriz cuadrada N×N con números enteros ingresados por teclado.

    Precondición: n debe ser un entero positivo.

    Postcondición: retorna una matriz de tamaño N×N con valores enteros.
    """
    matriz = []
    print(f"\n--- Carga de matriz {n}x{n} ---")
    for i in range(n):
        fila = []
        for j in range(n):
            while True:
                try:
                    valor = int(input(f"Ingrese el valor [{i},{j}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Debe ingresar un número entero válido.")
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz: List[List[int]]) -> None:
    """
    Imprime una matriz en formato tabular.

    Precondición: la matriz debe ser una lista bidimensional cuadrada.

    Postcondición: muestra la matriz por consola.
    """
    print()
    for fila in matriz:
        print("\t".join(f"{num:5d}" for num in fila))
    print()


def ordenar_filas(matriz: List[List[int]]) -> None:
    """
    Ordena cada fila de la matriz en forma ascendente.

    Precondición: la matriz no debe estar vacía.

    Postcondición: las filas quedan ordenadas en orden ascendente.
    """
    for fila in matriz:
        fila.sort()


def intercambiar_filas(matriz: List[List[int]], f1: int, f2: int) -> None:
    """
    Intercambia dos filas dadas.

    Precondición: 0 <= f1, f2 < len(matriz)

    Postcondición: las filas f1 y f2 quedan intercambiadas.
    """
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]


def intercambiar_columnas(matriz: List[List[int]], c1: int, c2: int) -> None:
    """
    Intercambia dos columnas dadas.

    Precondición: 0 <= c1, c2 < len(matriz)

    Postcondición: las columnas c1 y c2 quedan intercambiadas.
    """
    for fila in matriz:
        fila[c1], fila[c2] = fila[c2], fila[c1]


def trasponer_matriz(matriz: List[List[int]]) -> None:
    """
    Transpone la matriz (intercambia A[i][j] por A[j][i]) sobre sí misma.

    Precondición: la matriz debe ser cuadrada.

    Postcondición: la matriz resulta traspuesta.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]



def promedio_fila(matriz: List[List[int]], fila: int) -> float:
    """
    Calcula el promedio de los elementos de una fila.

    Precondición: 0 <= fila < len(matriz)

    Postcondición: retorna el promedio de la fila indicada.
    """
    return sum(matriz[fila]) / len(matriz[fila])


def porcentaje_impares_columna(matriz: List[List[int]], col: int) -> float:
    """
    Calcula el porcentaje de elementos impares en una columna.

    Precondición: 0 <= col < len(matriz)

    Postcondición: retorna el porcentaje de elementos impares.
    """
    n = len(matriz)
    impares = sum(1 for i in range(n) if matriz[i][col] % 2 != 0)
    return (impares / n) * 100


def es_simetrica_principal(matriz: List[List[int]]) -> bool:
    """
    Determina si la matriz es simétrica respecto a su diagonal principal.

    Precondición: la matriz es cuadrada.

    Postcondición: retorna True si es simétrica, False en caso contrario.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


def es_simetrica_secundaria(matriz: List[List[int]]) -> bool:
    """
    Determina si la matriz es simétrica respecto a su diagonal secundaria.

    Precondición: la matriz es cuadrada.

    Postcondición: retorna True si es simétrica respecto a la diagonal secundaria.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - 1 - j][n - 1 - i]:
                return False
    return True


def columnas_palindromas(matriz: List[List[int]]) -> List[int]:
    """
    Determina qué columnas son palíndromas.

    Precondición: la matriz es cuadrada.

    Postcondición: retorna una lista con los índices de columnas palíndromas.
    """
    n = len(matriz)
    palindromas = []
    for col in range(n):
        columna = [matriz[i][col] for i in range(n)]
        if columna == columna[::-1]:
            palindromas.append(col)
    return palindromas



def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se muestran los resultados luego de cada operación.
    """
    try:
        n = int(input("Ingrese el tamaño N de la matriz cuadrada: "))
        if n <= 0:
            raise ValueError("El tamaño debe ser un número entero positivo.")

        matriz = cargar_matriz(n)
        print("\nMatriz original:")
        imprimir_matriz(matriz)

        ordenar_filas(matriz)
        print("Matriz con filas ordenadas ascendentemente:")
        imprimir_matriz(matriz)

        f1 = int(input("Ingrese el número de la primera fila a intercambiar: "))
        f2 = int(input("Ingrese el número de la segunda fila a intercambiar: "))
        intercambiar_filas(matriz, f1, f2)
        print(f"Matriz tras intercambiar filas {f1} y {f2}:")
        imprimir_matriz(matriz)

        c1 = int(input("Ingrese el número de la primera columna a intercambiar: "))
        c2 = int(input("Ingrese el número de la segunda columna a intercambiar: "))
        intercambiar_columnas(matriz, c1, c2)
        print(f"Matriz tras intercambiar columnas {c1} y {c2}:")
        imprimir_matriz(matriz)

        trasponer_matriz(matriz)
        print("Matriz traspuesta:")
        imprimir_matriz(matriz)

        fila = int(input("Ingrese el número de fila para calcular su promedio: "))
        print(f"Promedio de la fila {fila}: {promedio_fila(matriz, fila):.2f}")

        col = int(input("Ingrese el número de columna para calcular porcentaje de impares: "))
        print(f"Porcentaje de impares en columna {col}: {porcentaje_impares_columna(matriz, col):.2f}%")

        print(f"La matriz es simétrica respecto a la diagonal principal: {es_simetrica_principal(matriz)}")

        print(f"La matriz es simétrica respecto a la diagonal secundaria: {es_simetrica_secundaria(matriz)}")

        palindromas = columnas_palindromas(matriz)
        if palindromas:
            print(f"Columnas palíndromas: {palindromas}")
        else:
            print("No hay columnas palíndromas.")

    except ValueError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Error: el índice de fila o columna está fuera del rango.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
