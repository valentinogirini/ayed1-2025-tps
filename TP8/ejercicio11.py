"""Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

import re

def normalizar_vocales(texto: str) -> str:
    """
    Reemplaza las vocales con tilde o diéresis por su versión sin tilde/diéresis.

    Precondición: texto es una cadena de caracteres.

    Postcondición: retorna el texto con las vocales normalizadas.
    """
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ä": "a", "ë": "e", "ï": "i", "ö": "o", "ü": "u"
    }
    return "".join(reemplazos.get(c, c) for c in texto)


def contar_vocales(palabra: str) -> dict[str, int]:
    """
    Cuenta cuántas vocales contiene una palabra.

    Precondición: palabra es una cadena de caracteres.

    Postcondición: retorna un diccionario con la cantidad de cada vocal encontrada.
    """
    palabra = normalizar_vocales(palabra.lower())
    vocales = "aeiou"
    conteo = {v: 0 for v in vocales}

    for letra in palabra:
        if letra in conteo:
            conteo[letra] += 1

    return {v: c for v, c in conteo.items() if c > 0}


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: muestra cada palabra de la frase con la cantidad de vocales que contiene.
    """
    frase = input("Ingrese una frase: ").strip()
    if not frase:
        print("Error: la frase no puede estar vacía.")
        return

    frase_limpia = re.sub(r'[^A-Za-záéíóúÁÉÍÓÚñÑäÄëËïÏöÖüÜ\s]', ' ', frase)
    palabras = frase_limpia.split()

    for palabra in palabras:
        conteo = contar_vocales(palabra)
        total = sum(conteo.values())
        print(f"{palabra:<15} -> Total: {total} | {conteo}")


if __name__ == "__main__":
    main()
