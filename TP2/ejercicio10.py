""". Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla. """

import random
from typing import List

def generar_lista_aleatoria(n: int) -> List[int]:
    """
    Genera una lista con n números aleatorios entre 1 y 100.
    
    Precondiciones: n debe ser un entero positivo.
    
    Postcondiciones: Devuelve una lista de longitud n con enteros entre 1 y 100.
    """
    return [random.randint(1, 100) for _ in range(n)]

def filtrar_impares(lista: List[int]) -> List[int]:
    """
    Devuelve una nueva lista con los elementos impares de la lista original usando filter.
    
    Precondiciones: La lista puede estar vacía o contener cualquier número de enteros.
    
    Postcondiciones: Devuelve una lista con los elementos impares de la lista original.
    """
    return list(filter(lambda x: x % 2 != 0, lista))

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números para la lista: "))
    lista_original = generar_lista_aleatoria(n)
    print(f"Lista original: {lista_original}")

    lista_impares = filtrar_impares(lista_original)
    print(f"Lista con elementos impares: {lista_impares}")
