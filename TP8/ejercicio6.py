"""Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""

import re

def procesar_frase(frase: str) -> list[str]:
    """
    Procesa una frase eliminando palabras repetidas y ordenándolas por longitud.

    Precondición: frase es una cadena de caracteres.

    Postcondición: retorna una lista de palabras únicas, sin signos de puntuación, ordenadas por longitud.
    """
    frase_limpia = re.sub(r'[^A-Za-záéíóúÁÉÍÓÚñÑüÜ\s]', ' ', frase).lower()
    
    palabras = frase_limpia.split()
    conjunto_palabras = set(palabras)
    palabras_ordenadas = sorted(conjunto_palabras, key=len)
    return palabras_ordenadas


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: imprime las palabras únicas ordenadas por longitud.
    """
    frase = input("Ingrese una frase: ").strip()
    if not frase:
        print("Error: la frase no puede estar vacía.")
        return
    palabras = procesar_frase(frase)
    
    if palabras:
        print("\nPalabras únicas ordenadas por longitud:")
        for palabra in palabras:
            print(palabra)
    else:
        print("\nError: no se encontraron palabras válidas en la frase.")


if __name__ == "__main__":
    main()
