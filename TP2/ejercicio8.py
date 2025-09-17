"""Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
"""

from typing import List

def impares_100_al_200() -> List[int]:
    """
    Genera una lista con todos los números impares entre 100 y 200 inclusive.
    
    Precondiciones: Ninguna.
    
    Postcondiciones: Devuelve una lista de enteros que son todos los números impares en el rango 100 a 200.
    """
    return [x for x in range(100, 201) if x % 2 != 0]


if __name__ == "__main__":
    lista_impares = impares_100_al_200()
    print(f"Números impares entre 100 y 200: {lista_impares}")
