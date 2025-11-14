"""Desarrollar un programa que permita realizar reservas en una sala de cine de N
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
en un mismo programa:

mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
se volverá a invocar luego de la misma con los estados actualizados.

reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
sala en caso de estar disponible dicha butaca. La función devolverá True/False
si logró o no reservar la butaca.

cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.

butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas desocupadas 
hay en la sala.

butacas_contiguas: Buscará la secuencia más larga de butacas libres contiguas en una misma fila y 
devolverá  las coordenadas de inicio de la misma. """


import random
from typing import List, Tuple, Optional


def cargar_sala(filas: int, columnas: int) -> List[List[int]]:
    """
    Carga una sala de cine de tamaño filas×columnas con valores aleatorios.

    Precondición: filas y columnas son enteros positivos.

    Postcondición: retorna una matriz representando el estado inicial de la sala.
    """
    if filas <= 0 or columnas <= 0:
        raise ValueError("Las dimensiones deben ser positivas.")

    return [[random.choice([0, 1]) for _ in range(columnas)] for _ in range(filas)]


def mostrar_butacas(sala: List[List[int]]) -> None:
    """
    Muestra el estado actual de las butacas:
    [0] = libre, [X] = ocupada.

    Precondición: sala es una lista bidimensional rectangular.

    Postcondición: imprime la representación visual de la sala.
    """
    print("\n--- Estado actual de la sala ---")
    print("   " + " ".join(f"{j+1:>3}" for j in range(len(sala[0]))))
    for i, fila in enumerate(sala, start=1):
        estados = ["[0]" if b == 0 else "[X]" for b in fila]
        print(f"F{i:>2} " + " ".join(estados))
    print()


def reservar(sala: List[List[int]], fila: int, col: int) -> bool:
    """
    Intenta reservar una butaca libre.

    Precondición: fila y col dentro del rango de la sala.

    Postcondición:
    - si la butaca estaba libre, se marca como ocupada y retorna True.
    - si estaba ocupada, retorna False.
    """
    try:
        if sala[fila][col] == 0:
            sala[fila][col] = 1
            return True
        else:
            return False
    except IndexError:
        print("Error: coordenadas fuera de rango.")
        return False


def butacas_libres(sala: List[List[int]]) -> int:
    """
    Cuenta cuántas butacas libres hay en toda la sala.

    Precondición: sala válida.

    Postcondición: devuelve el total de butacas con valor 0.
    """
    return sum(b == 0 for fila in sala for b in fila)


def butacas_contiguas(sala: List[List[int]]) -> Optional[Tuple[int, int, int]]:
    """
    Busca la secuencia más larga de butacas contiguas libres en una misma fila 
    y devuelve una tupla (fila, inicio, longitud).

    Precondición: sala válida.

    Postcondición: retorna (mejor_fila, mejor_inicio, mejor_longitud) o None si no hay libres.
    """
    mejor_fila, mejor_inicio, mejor_longitud = -1, -1, 0

    for i, fila in enumerate(sala):
        _, actual_longitud = 0, 0
        for j, butaca in enumerate(fila):
            if butaca == 0:
                actual_longitud += 1
            else:
                if actual_longitud > mejor_longitud:
                    mejor_longitud = actual_longitud
                    mejor_fila = i
                    mejor_inicio = j - actual_longitud
                actual_longitud = 0
        if actual_longitud > mejor_longitud:
            mejor_longitud = actual_longitud
            mejor_fila = i
            mejor_inicio = len(fila) - actual_longitud

    return (mejor_fila, mejor_inicio, mejor_longitud) if mejor_longitud > 0 else None


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se muestra el resultado de la reserva y el estado final de la sala.
    """
    print("--- Sistema de Reservas de Cine ---\n")
    try:
        n = int(input("Ingrese cantidad de filas: "))
        m = int(input("Ingrese cantidad de butacas por fila: "))

        sala = cargar_sala(n, m)
        mostrar_butacas(sala)

        fila = int(input("Ingrese número de fila para reservar: ")) - 1
        col = int(input("Ingrese número de butaca: ")) - 1

        if reservar(sala, fila, col):
            print("\nReserva realizada con éxito.")
        else:
            print("\nLa butaca seleccionada ya está ocupada o es inválida.")

        mostrar_butacas(sala)

        print(f"Total de butacas libres: {butacas_libres(sala)}")

        contiguas = butacas_contiguas(sala)
        if contiguas:
            f, c, l = contiguas
            print(f"La secuencia más larga de butacas libres está en fila {f+1}, desde la columna {c+1}, con longitud {l}.")
        else:
            print("No hay secuencias de butacas contiguas libres.")

    except ValueError:
        print("Error: Debe ingresar valores numéricos enteros.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
