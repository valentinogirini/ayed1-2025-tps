"""Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final.
"""

import re

def longitud_sin_signos(palabra: str) -> int:
    """
    Calcula la longitud de una palabra ignorando los signos de puntuación.

    Precondición: palabra es una cadena no vacía.

    Postcondición: retorna un entero con la cantidad de caracteres alfabéticos o numéricos
    (sin contar signos).
    """
    limpia = re.sub(r'[^A-Za-z0-9áéíóúÁÉÍÓÚñÑüÜ]', '', palabra)
    return len(limpia)


def ordenar_por_longitud(frase: str) -> str:
    """
    Devuelve una nueva cadena con las palabras ordenadas por longitud, 
    ignorando los signos de puntuación al calcular la longitud, 
    pero conservándolos en el texto final.

    Precondición: frase es una cadena no vacía que contiene palabras separadas por uno o más espacios.

    Postcondición: retorna una cadena con las palabras ordenadas en orden creciente según su longitud 
    (sin contar la puntuación), separadas por un solo espacio.
    """
    palabras = frase.split()
    palabras_ordenadas = sorted(palabras, key=longitud_sin_signos)
    return " ".join(palabras_ordenadas)


def main() -> None:
    """
    Solicita una frase al usuario, valida la entrada y muestra las palabras
    ordenadas según su longitud.

    Precondición: ninguna.

    Postcondición: imprime por pantalla la frase con las palabras ordenadas, 
    o un mensaje de error si los datos no son válidos.
    """
    try:
        frase = input("Ingrese una frase: ").strip()
        if frase == "":
            raise ValueError("La frase no puede estar vacía.")
        
        resultado = ordenar_por_longitud(frase)
        print(f"Resultado: {resultado}")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
