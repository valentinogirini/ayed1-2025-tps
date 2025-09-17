"""Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas
que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]."""

from typing import List

def normalizar(lista: List[int]) -> List[float]:
    """
    Normaliza los elementos de la lista para que su suma sea 1.0, respetando las proporciones.
    
    Precondiciones: La lista debe contener al menos un elemento.
    
    Postcondiciones: Devuelve una nueva lista de floats cuya suma es 1.0 y mantiene las proporciones relativas de los elementos originales.
    """
    total = sum(lista)
    return [x / total for x in lista]


if __name__ == "__main__":
    lista_original = [1, 1, 2, 4]
    print(f"Lista original: {lista_original}")

    lista_normalizada = normalizar(lista_original)
    print(f"Lista normalizada: {lista_normalizada}")
    print(f"Suma de la lista normalizada: {sum(lista_normalizada)}")
