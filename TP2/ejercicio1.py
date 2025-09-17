"""Desarrollar cada una de las siguientes funciones y escribir un programa que permita
verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos
también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""

import random
from typing import List
from functools import reduce

def cargar_lista() -> List[int]:
    """
    Genera una lista con números de 4 dígitos. La cantidad de elementos es aleatoria entre 10 y 99.
    
    Precondiciones: Ninguna.
    
    Postcondiciones: Devuelve una lista de enteros con longitud entre 10 y 99, cada elemento entre 1000 y 9999.
    """
    cantidad = random.randint(10, 99)
    return [random.randint(1000, 9999) for _ in range(cantidad)]


def producto(lista: List[int]) -> int:
    """
    Calcula el producto de todos los elementos de la lista.
    
    Precondiciones: La lista debe contener al menos un elemento.
    
    Postcondiciones: Devuelve un número entero que representa el producto acumulado.
    """
    return reduce(lambda x, y: x * y, lista)


def eliminar(lista: List[int], valor: int) -> None:
    """
    Elimina todas las apariciones de valor de la lista.
    
    Precondiciones: La lista puede estar vacía o contener cualquier número de enteros.
    
    Postcondiciones: La lista queda modificada, sin apariciones de valor.
    """
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            lista.pop(i)
        else:
            i += 1

def es_capicua(lista: List[int]) -> bool:
    """
    Determina si la lista es capicúa.
    
    Precondiciones: La lista puede estar vacía o tener cualquier longitud.
    
    Postcondiciones: Devuelve True si la lista es igual a su reverso, False en caso contrario.
    """
    return lista == lista[::-1]


if __name__ == "__main__":
    lista = cargar_lista()
    print(f"Lista cargada: {lista}")

    print(f"Producto de los elementos: {producto(lista)}")

    valor = int(input("Ingrese un valor a eliminar: "))
    eliminar(lista, valor)
    print(f"Lista luego de eliminar: {lista}")
    
    lista_capicua = [50, 17, 91, 17, 50]
    if es_capicua(lista_capicua):
        print("La lista es capicúa.")
    else:
        print("La lista no es capicúa.")