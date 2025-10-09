"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
"""

def centrar_cadena(cadena: str) -> str:
    """
    Centra una cadena en un ancho de 80 columnas.
    
    Precondición: cadena es una cadena de caracteres.
    
    Postcondición: retorna la cadena centrada en un ancho de 80 caracteres.
    """
    espacios = (80 - len(cadena)) // 2
    return " " * espacios + cadena


def main() -> None:
    """
    Permite verificar el funcionamiento de la función centrar_cadena.
    
    Precondición: ninguna.
    
    Postcondición: muestra por pantalla la cadena centrada en 80 columnas.
    """
    texto = input("Ingrese una cadena: ")
    print(centrar_cadena(texto))


if __name__ == "__main__":
    main()
