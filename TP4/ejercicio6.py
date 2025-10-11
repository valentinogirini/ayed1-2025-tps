"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma.
Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la subcadena que comienza
en la posición 25 y tiene 9 caracteres, resultando la subcadena "4356-7890".
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""

def extraer_subcadena_a(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Extrae una subcadena usando rebanadas.
    
    Precondición:
    - cadena es una cadena no vacía ni compuesta solo por espacios.
    - inicio es un entero mayor o igual a 1 y menor o igual a la longitud de la cadena.
    - cantidad es un entero mayor que 0 y no excede los caracteres restantes.
    
    Postcondición: retorna la subcadena formada por 'cantidad' caracteres a partir de 'inicio'.
    """
    inicio -= 1
    return cadena[inicio:inicio + cantidad]


def extraer_subcadena_b(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Extrae una subcadena sin utilizar rebanadas, mediante un ciclo.
    
    Precondición:
    - cadena es una cadena no vacía ni compuesta solo por espacios.
    - inicio es un entero mayor o igual a 1 y menor o igual a la longitud de la cadena.
    - cantidad es un entero mayor que 0 y no excede los caracteres restantes.
    
    Postcondición: retorna la subcadena formada por 'cantidad' caracteres a partir de 'inicio'.
    """
    resultado = ""
    inicio -= 1
    fin = inicio + cantidad

    while inicio < fin:
        resultado += cadena[inicio]
        inicio += 1

    return resultado


def main() -> None:
    """
    Lee una cadena, la posición inicial y la cantidad de caracteres.
    Muestra los resultados de ambas funciones.

    Precondición: ninguna.
    
    Postcondición: imprime por pantalla las subcadenas o un mensaje de error.
    """
    try:
        cadena = input("Ingrese una cadena: ")
        if cadena.strip() == "":
            raise ValueError("La cadena no puede estar vacía o compuesta solo por espacios.")
        
        inicio_str = input("Ingrese la posición inicial (comenzando en 1): ").strip()
        cantidad_str = input("Ingrese la cantidad de caracteres: ").strip()

        if not inicio_str.isdigit() or not cantidad_str.isdigit():
            raise ValueError("Debe ingresar números enteros positivos sin signos ni decimales.")

        inicio = int(inicio_str)
        cantidad = int(cantidad_str)

        if inicio < 1 or inicio > len(cadena):
            raise ValueError(f"La posición inicial debe estar dentro del rango de la cadena (entre 1 y {len(cadena)}).")
        if cantidad <= 0:
            raise ValueError("La cantidad de caracteres debe ser mayor que 0.")
        if inicio - 1 + cantidad > len(cadena):
            raise ValueError("La cantidad excede los caracteres disponibles desde esa posición.")

        print("\n--- Resultados ---")
        print(f"a) Con rebanadas: {extraer_subcadena_a(cadena, inicio, cantidad)}")
        print(f"b) Sin rebanadas: {extraer_subcadena_b(cadena, inicio, cantidad)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
