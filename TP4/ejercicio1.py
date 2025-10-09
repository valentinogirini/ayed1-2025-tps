"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento."""

def es_capicua(cadena: str) -> bool:
    """
    Determina si una cadena es capicúa.
    
    Precondición: cadena es una cadena de caracteres.
    
    Postcondición: retorna True si la cadena es capicúa, False en caso contrario.
    """
    n = len(cadena)
    for i in range(n // 2):
        if cadena[i] != cadena[n - 1 - i]:
            return False
    return True


def main() -> None:
    """
    Permite verificar el funcionamiento de la función es_capicua.
    
    Precondición: ninguna.
    
    Postcondición: muestra por pantalla si la cadena ingresada es capicúa o no.
    """
    texto = input("Ingrese una cadena: ")
    if es_capicua(texto):
        print("Es capicúa")
    else:
        print("No es capicúa")


if __name__ == "__main__":
    main()
