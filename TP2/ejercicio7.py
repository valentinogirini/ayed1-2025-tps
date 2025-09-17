"""Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes."""

from typing import List

def intercalar_elementos_listas(lista1: List[int], lista2: List[int]) -> None:
    """
    Intercala los elementos de lista2 dentro de lista1 usando slicing.

    Precondiciones: lista1 y lista2 son listas de enteros.

    Postcondiciones: Modifica lista1. No devuelve nada.
    """
    for i in range(len(lista2)):
        lista1[i*2+1:i*2+1] = lista2[i:i+1]

if __name__ == "__main__":
    lista1 = [8, 1, 3, 2, 3]
    lista2 = [5, 9, 6, 3, 4, 2, 1]
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    intercalar_elementos_listas(lista1, lista2)
    print(f"Lista intercalada: {lista1}")
