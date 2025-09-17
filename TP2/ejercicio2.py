"""Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa."""

import random
from typing import List

def generar_lista(n: int) -> List[int]:
    """
    Genera una lista con n números aleatorios del 1 al 100.
    
    Precondiciones: n debe ser un entero positivo.
    
    Postcondiciones: Devuelve una lista de longitud n con enteros entre 1 y 100.
    """
    return [random.randint(1, 100) for _ in range(n)]


def tiene_repetidos(lista: List[int]) -> bool:
    """
    Verifica si la lista contiene algún elemento repetido.
    
    Precondiciones: La lista puede estar vacía o contener cualquier número de enteros.
    
    Postcondiciones: Devuelve True si hay elementos repetidos, False en caso contrario.
    """
    for i, elem in enumerate(lista):
        if elem in lista[i+1:]:
            return True
    return False


def elementos_unicos(lista: List[int]) -> List[int]:
    """
    Devuelve una nueva lista con los elementos únicos de la lista original, sin importar el orden.
    
    Precondiciones: La lista puede estar vacía o contener cualquier número de enteros.
    
    Postcondiciones: Devuelve una lista con los elementos sin repeticiones.
    """
    lista_unicos = []
    for elem in lista:
        if elem not in lista_unicos:
            lista_unicos.append(elem)
    return lista_unicos


if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números para la lista: "))
    lista = generar_lista(n)
    print(f"Lista generada: {lista}")

    if tiene_repetidos(lista):
        print("La lista contiene elementos repetidos.")
    else:
        print("La lista no contiene elementos repetidos.")

    lista_sin_repetidos = elementos_unicos(lista)
    print(f"Lista con elementos únicos: {lista_sin_repetidos}")
