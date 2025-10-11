"""Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros."""

def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    Devuelve una subcadena con los últimos N caracteres de una cadena dada.
    
    Precondición:
    - cadena es una cadena no vacía.
    - n es un entero mayor o igual a 1.
    
    Postcondición:
    - retorna una subcadena con los últimos N caracteres de la cadena original.
    - si N es mayor que la longitud de la cadena, se devuelve la cadena completa.
    """
    if n > len(cadena):
        return cadena
    else:
        return cadena[-n:]


def main() -> None:
    """
    Lee una cadena y un número entero N, valida los datos, y muestra los últimos N caracteres de la cadena.
    
    Precondición: ninguna.
    
    Postcondición: imprime el resultado o un mensaje de error si los datos no son válidos.
    """
    try:
        cadena = input("Ingrese una cadena: ").strip()
        if cadena == "":
            raise ValueError("La cadena no puede estar vacía.")
        
        n_str = input("Ingrese la cantidad de caracteres a extraer: ").strip()
        if not n_str.isdigit():
            raise ValueError("Debe ingresar un número entero positivo.")
        n = int(n_str)

        if n < 1:
            raise ValueError("N debe ser mayor o igual a 1.")

        resultado = ultimos_caracteres(cadena, n)
        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

