"""Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones 
que generen cada una de ellas sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. El tamaño de las matrices debe establecerse 
como N x N, donde N se ingresa a través del teclado."""

from typing import List


def generar_matriz_a(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada N×N con un patrón en la diagonal principal.

    Precondición: n es un entero positivo.

    Postcondición: retorna una matriz con el patrón definido.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    for i, fila in enumerate(matriz):
        fila[i] = 2 * i + 1 

    return matriz


def generar_matriz_b(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N donde la diagonal secundaria
    está formada por potencias de 3, y el resto de los elementos son ceros.

    Precondición: n es un número entero positivo.

    Postcondición: devuelve una matriz de tamaño N×N con la diagonal secundaria rellena con 
    potencias de 3 en orden ascendente desde abajo.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        j = n - 1 - i
        matriz[i][j] = 3 ** i

    return matriz


def generar_matriz_c(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N con un triángulo inferior
    de números enteros decrecientes desde N hasta 1.

    Precondición: n es un número entero positivo.

    Postcondición: devuelve una matriz de tamaño N×N con la parte inferior izquierda rellena 
    con números decrecientes y el resto con ceros.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            matriz[i][j] = n - i

    return matriz


def generar_matriz_d(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N donde cada fila contiene
    el mismo número, y dicho valor es una potencia de 2 decreciente
    desde la primera fila hasta la última.

    Precondición: n es un número entero positivo.

    Postcondición: devuelve una matriz de tamaño N×N con valores constantes por fila, 
    decrecientes según potencias de 2.
    """
    matriz = []
    for i in range(n):
        valor = 2 ** (n - 1 - i)
        matriz.append([valor] * n)
    return matriz


def generar_matriz_e(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N con un patrón alternado,
    colocando números consecutivos en las posiciones donde (i + j) es impar
    y ceros donde (i + j) es par.

    Precondición: n es un número entero positivo.

    Postcondición: devuelve una matriz de tamaño N×N con valores consecutivos en posiciones 
    impares y ceros en las pares.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    contador = 1

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 != 0:
                matriz[i][j] = contador
                contador += 1

    return matriz


def generar_matriz_f(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N siguiendo un patrón de relleno
    en diagonales desde la parte superior derecha hacia la inferior izquierda.

    Precondición: n es un número entero positivo.

    Postcondición: devuelve una matriz de tamaño N×N donde cada fila contiene una secuencia
    descendente de números consecutivos rellenada desde la derecha hacia la izquierda.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    contador = 1

    for i in range(n):
        for j in range(n - 1, n - 2 - i, -1):
            matriz[i][j] = contador
            contador += 1

    return matriz


def generar_matriz_g(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N con números consecutivos
    dispuestos en forma de espiral en sentido horario.

    Precondición: n es un número entero positivo.

    Postcondición: devuelve una matriz de tamaño N×N con los números del 1 al N² colocados en espiral.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    arriba, abajo = 0, n - 1
    izquierda, derecha = 0, n - 1
    contador = 1

    while contador <= n * n:
        for j in range(izquierda, derecha + 1):
            matriz[arriba][j] = contador
            contador += 1
        arriba += 1

        for i in range(arriba, abajo + 1):
            matriz[i][derecha] = contador
            contador += 1
        derecha -= 1

        if arriba <= abajo:
            for j in range(derecha, izquierda - 1, -1):
                matriz[abajo][j] = contador
                contador += 1
            abajo -= 1

        if izquierda <= derecha:
            for i in range(abajo, arriba - 1, -1):
                matriz[i][izquierda] = contador
                contador += 1
            izquierda += 1

    return matriz


def generar_matriz_h(n: int) -> List[List[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N donde los números se
    llenan por diagonales que ascienden hacia la derecha.

    Precondición: n es un número entero positivo.

    Postcondición: devuelve una matriz de tamaño N×N rellena con números 
    consecutivos por diagonales crecientes.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    valor = 1

    for j_inicio in range(n):
        i, j = 0, j_inicio
        while i < n and j >= 0:
            matriz[i][j] = valor
            valor += 1
            i += 1
            j -= 1

    for i_inicio in range(1, n):
        i, j = i_inicio, n - 1
        while i < n and j >= 0:
            matriz[i][j] = valor
            valor += 1
            i += 1
            j -= 1

    return matriz



def generar_matriz_i(n: int) -> list[list[int]]:
    """
    Genera una matriz cuadrada de tamaño N×N con números consecutivos
    dispuestos en un patrón zigzag diagonal.

    Precondición: n es un número entero positivo.

    Postcondición: devuelve una matriz de tamaño N×N con los números del 1 al N² organizados 
    en diagonales alternadas en zigzag.
    """
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    contador = 1

    for s in range(2 * n - 1):
        if s % 2 == 0:
            r = min(s, n - 1)
            c = s - r
            while r >= 0 and c < n:
                matriz[r][c] = contador
                contador += 1
                r -= 1
                c += 1
        else:
            c = min(s, n - 1)
            r = s - c
            while c >= 0 and r < n:
                matriz[r][c] = contador
                contador += 1
                r += 1
                c -= 1
                
    return matriz


def imprimir_matriz(matriz: List[List[int]]) -> None:
    """
    Imprime una matriz en formato compacto, sin separadores adicionales.

    Precondición: matriz válida.

    Postcondición: muestra la matriz en pantalla.
    """
    print()
    for fila in matriz:
        print("".join(f"{x:>4}" if x != 0 else "   0" for x in fila))
    print()


def main() -> None:
    """
    Función principal del programa.
    
    Precondición: ninguna.

    Postcondición: se imprimen por pantalla todas las matrices generadas, cada una correspondiente 
    a un patrón distinto.
    """
    print("--- Generador de Matriz con Patrón Diagonal ---\n")
    try:
        n = int(input("Ingrese el tamaño N de la matriz: "))
        if n <= 0:
            raise ValueError("N debe ser un entero positivo.")


        print("\nPatrón 1: Diagonal principal con números impares")
        matriz1 = generar_matriz_a(n)
        imprimir_matriz(matriz1)

        print("Patrón 2: Diagonal secundaria con potencias de 3")
        matriz2 = generar_matriz_b(n)
        imprimir_matriz(matriz2)

        print("Patrón 3: Triángulo inferior con números decrecientes")
        matriz3 = generar_matriz_c(n)
        imprimir_matriz(matriz3)

        print("Patrón 4: Filas constantes con potencias de 2 decrecientes")
        matriz4 = generar_matriz_d(n)
        imprimir_matriz(matriz4)

        print("Patrón 5: Matriz ajedrezada con números consecutivos")
        matriz5 = generar_matriz_e(n)
        imprimir_matriz(matriz5)

        print("Patrón 6: Diagonales desde la esquina superior derecha")
        matriz6 = generar_matriz_f(n)
        imprimir_matriz(matriz6)

        print("Patrón 7: Matriz en espiral")
        matriz7 = generar_matriz_g(n)
        imprimir_matriz(matriz7)

        print("Patrón 8: Matriz rellena por diagonales")
        matriz8 = generar_matriz_h(n)
        imprimir_matriz(matriz8)

        print("Patrón 9: Relleno diagonal zig-zag")
        matriz9 = generar_matriz_i(n)
        imprimir_matriz(matriz9)


    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
