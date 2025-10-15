"""Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función. """

from typing import Tuple
import re

def limpiar_palabra(palabra: str) -> str:
    """
    Devuelve la palabra sin signos de puntuación.

    Precondición: palabra es una cadena no vacía.

    Postcondición: retorna la palabra solo con caracteres alfabéticos o numéricos.
    """
    return re.sub(r'[^A-Za-z0-9áéíóúÁÉÍÓÚñÑüÜ]', '', palabra)

def reemplazar_palabra(frase: str, palabra_antigua: str, palabra_nueva: str) -> Tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra completa por otra en la frase,
    ignorando signos de puntuación al comparar palabras, pero conservando la puntuación original.

    Precondición:
    - frase es una cadena no vacía.
    - palabra_antigua y palabra_nueva son cadenas no vacías.

    Postcondición: retorna una tupla (frase_modificada, contador) donde:
    - frase_modificada es la cadena con los reemplazos realizados.
    - contador es un entero con la cantidad de palabras reemplazadas.
    """
    palabras = frase.split()
    resultado = []
    contador = 0

    for palabra in palabras:
        if limpiar_palabra(palabra) == palabra_antigua:
            nueva = palabra.replace(limpiar_palabra(palabra), limpiar_palabra(palabra_nueva))
            resultado.append(nueva)
            contador += 1
        else:
            resultado.append(palabra)

    frase_modificada = " ".join(resultado)
    return frase_modificada, contador


def main() -> None:
    """
    Solicita una frase y palabras para reemplazar, valida la entrada y muestra
    la frase modificada y la cantidad de reemplazos.

    Precondición: ninguna.

    Postcondición: imprime por pantalla la frase con las palabras reemplazadas y la cantidad de reemplazos,
    o un mensaje de error si los datos no son válidos.
    """
    try:
        frase = input("Ingrese una frase: ").strip()
        if frase == "":
            raise ValueError("La frase no puede estar vacía.")

        palabra_antigua = input("Ingrese la palabra a reemplazar: ").strip()
        if palabra_antigua == "":
            raise ValueError("La palabra a reemplazar no puede estar vacía.")

        palabra_nueva = input("Ingrese la palabra nueva: ").strip()
        if palabra_nueva == "":
            raise ValueError("La palabra nueva no puede estar vacía.")

        frase_modificada, cantidad = reemplazar_palabra(frase, palabra_antigua, palabra_nueva)
        print(f"\nFrase modificada: {frase_modificada}")
        print(f"Cantidad de reemplazos: {cantidad}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

