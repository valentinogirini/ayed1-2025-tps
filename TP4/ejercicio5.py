"""Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo
una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más
caracteres de la cadena original. Escribir también un programa para verificar el
comportamiento de la misma. Hacer tres versiones de la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter"""

import re

def extraer_palabras(frase: str) -> list[str]:
    """
    Extrae solo las palabras de una frase, ignorando signos de puntuación y números.

    Precondición: frase es una cadena no vacía.

    Postcondición: retorna una lista con las palabras encontradas.
    """
    return re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+", frase)

def filtrar_palabras_a(frase: str, n: int) -> str:
    """
    Devuelve una nueva cadena con las palabras que tienen N o más caracteres, utilizando ciclos normales.

    Precondición:
    - frase es una cadena no vacía.
    - n es un entero mayor o igual a 1.
    
    Postcondición: retorna una cadena con las palabras filtradas separadas por espacios.
    """
    frase = extraer_palabras(frase)
    resultado = []
    for palabra in frase:
        if len(palabra) >= n:
            resultado.append(palabra)
            
    if len(resultado) == 0:
        return f"No hay palabras con {n} o más caracteres."
            
    return " ".join(resultado)


def filtrar_palabras_b(frase: str, n: int) -> str:
    """
    Devuelve una nueva cadena con las palabras que tienen N o más caracteres, utilizando listas por comprensión.

    Precondición: 
    - frase es una cadena no vacía.
    - n es un entero mayor o igual a 1.
    
    Postcondición: retorna una cadena con las palabras filtradas separadas por espacios.
    """
    frase = extraer_palabras(frase)
    resultado = [p for p in frase if len(p) >= n]

    if not resultado:
        return f"No hay palabras con {n} o más caracteres."
    
    return " ".join(resultado)


def filtrar_palabras_c(frase: str, n: int) -> str:
    """
    Devuelve una nueva cadena con las palabras que tienen N o más caracteres, utilizando la función filter().

    Precondición: 
    - frase es una cadena no vacía.
    - n es un entero mayor o igual a 1.
    
    Postcondición: retorna una cadena con las palabras filtradas separadas por espacios.
    """
    frase = extraer_palabras(frase)
    resultado = list(filter(lambda p: len(p) >= n, frase))

    if not resultado:
        return f"No hay palabras con {n} o más caracteres."
    
    return " ".join(resultado)


def main() -> None:
    """
    Lee una frase y un número entero N, valida los datos, y muestra los resultados de las tres versiones de filtrado.

    Precondición: ninguna.
    
    Postcondición: imprime por pantalla las frases filtradas o un mensaje de error si los datos no son válidos.
    """
    try:
        frase = input("Ingrese una frase: ").strip()
        if frase == "":
            raise ValueError("La frase no puede estar vacía.")
        
        n_str = input("Ingrese un número entero N: ").strip()
        if not n_str.isdigit():
            raise ValueError("Debe ingresar un número entero.")
        n = int(n_str)

        if n < 1:
            raise ValueError("N debe ser mayor o igual a 1.")

        print("\n--- Resultados ---")
        print(f"a) Ciclos normales: {filtrar_palabras_a(frase, n)}")
        print(f"b) Listas por comprensión: {filtrar_palabras_b(frase, n)}")
        print(f"c) Función filter: {filtrar_palabras_c(frase, n)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
