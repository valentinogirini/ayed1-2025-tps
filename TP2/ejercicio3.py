"""Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. """

from typing import List

def generar_cuadrados(n: int) -> List[int]:
    """
    Genera una lista con los cuadrados de los números del 1 al n.
    
    Precondiciones: n debe ser un entero positivo.
    
    Postcondiciones: Devuelve una lista de longitud n donde cada elemento es el cuadrado
    del número correspondiente de 1 a n.
    """
    return [i**2 for i in range(1, n+1)]


def ultimos_valores(lista: List[int], cantidad: int) -> List[int]:
    """
    Devuelve los últimos 'cantidad' elementos de la lista.
    
    Precondiciones: 'cantidad' debe ser un entero positivo menor o igual a la longitud de la lista.
    
    Postcondiciones: Devuelve una lista con los últimos 'cantidad' elementos.
    """
    return lista[-cantidad:]


if __name__ == "__main__":
    n = int(input("Ingrese un número N: "))
    lista_cuadrados = generar_cuadrados(n)
    print(f"Lista de cuadrados del 1 al {n}: {lista_cuadrados}")

    ultimos_10 = ultimos_valores(lista_cuadrados, 10)
    print(f"Últimos 10 valores de la lista: {ultimos_10}")