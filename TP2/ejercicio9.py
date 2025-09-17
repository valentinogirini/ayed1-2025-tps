"""Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. """

from typing import List

def multiplos_7_no_5(a: int, b: int) -> List[int]:
    """
    Genera una lista con los números entre a y b que sean múltiplos de 7 pero no de 5.
    
    Precondiciones: a y b deben ser enteros.
    
    Postcondiciones: Devuelve una lista de enteros que cumplen la condición.
    """
    return [x for x in range(a, b+1) if x % 7 == 0 and x % 5 != 0]


if __name__ == "__main__":
    a = int(input("Ingrese A: "))
    b = int(input("Ingrese B: "))
    if a > b:
        aux = a
        a = b
        b = aux
    
    lista_resultante = multiplos_7_no_5(a, b)
    print(f"Números entre {a} y {b} múltiplos de 7 y no de 5: {lista_resultante}")
