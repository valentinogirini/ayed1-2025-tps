"""Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función. """

from typing import List, Any

def ordenada(lista: List[Any]) -> bool:
    """
    Verifica si la lista está ordenada en forma ascendente.
    
    Precondiciones: La lista puede estar vacía o contener elementos comparables entre si.
    
    Postcondiciones: Devuelve True si la lista está ordenada de forma ascendente, False en caso contrario.
    """
    return lista == sorted(lista)


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4]
    lista2 = ['b', 'a', 'c']

    print(f"Lista: {lista1} \nOrdenada: {ordenada(lista1)}")
    print()
    print(f"Lista: {lista2} \nOrdenada: {ordenada(lista2)}")

