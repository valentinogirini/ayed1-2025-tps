"""Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada."""

from typing import List

def eliminar_valores(lista: List[int], valores: List[int]) -> None:
    """
    Elimina de 'lista' todos los elementos que se encuentren en 'valores'.
    
    Precondiciones: 'lista' y 'valores' pueden estar vacías o contener cualquier número de enteros.
    
    Postcondiciones: La lista original queda modificada, sin elementos que estén en 'valores'.
    """
    i = 0
    while i < len(lista):
        if lista[i] in valores:
            lista.pop(i)
        else:
            i += 1


if __name__ == "__main__":
    lista_original = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    lista_a_eliminar = [2, 3, 5]

    print(f"Lista original: {lista_original}")
    print(f"Valores a eliminar: {lista_a_eliminar}")

    eliminar_valores(lista_original, lista_a_eliminar)
    print(f"Lista resultante: {lista_original}")
