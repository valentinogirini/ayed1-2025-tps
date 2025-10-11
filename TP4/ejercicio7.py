"""Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""

def eliminar_subcadena_a(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Elimina una subcadena usando rebanadas.
    
    Precondición:
    - cadena es una cadena no vacía ni compuesta solo por espacios.
    - inicio es un entero >= 1 y <= longitud de la cadena.
    - cantidad es un entero > 0 y no excede los caracteres disponibles desde 'inicio'.
    
    Postcondición: retorna la cadena resultante tras eliminar la subcadena.
    """
    inicio -= 1
    return cadena[:inicio] + cadena[inicio + cantidad:]


def eliminar_subcadena_b(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Elimina una subcadena sin usar rebanadas, mediante un ciclo.
    
    Precondición:
    - cadena es una cadena no vacía ni compuesta solo por espacios.
    - inicio es un entero >= 1 y <= longitud de la cadena.
    - cantidad es un entero > 0 y no excede los caracteres disponibles desde 'inicio'.
    
    Postcondición: retorna la cadena resultante tras eliminar la subcadena.
    """
    resultado = ""
    inicio -= 1
    fin = inicio + cantidad
    
    for i, c in enumerate(cadena):
        if i < inicio or i >= fin:
            resultado += c

    return resultado


def main() -> None:
    """
    Lee una cadena, posición y cantidad, valida los datos, y muestra los resultados.
    
    Precondición: ninguna.
    
    Postcondición: imprime por pantalla la cadena resultante o un mensaje de error si los datos son inválidos.
    """
    try:
        cadena = input("Ingrese una cadena: ").strip()
        if cadena == "":
            raise ValueError("La cadena no puede estar vacía o solo contener espacios.")

        inicio_str = input("Ingrese la posición inicial (comenzando en 1): ").strip()
        cantidad_str = input("Ingrese la cantidad de caracteres a eliminar: ").strip()

        if not inicio_str.isdigit() or not cantidad_str.isdigit():
            raise ValueError("Debe ingresar números enteros positivos sin signos ni decimales.")

        inicio = int(inicio_str)
        cantidad = int(cantidad_str)

        if inicio < 1 or inicio > len(cadena):
            raise ValueError(f"La posición inicial debe estar dentro del rango de la cadena (entre 1 y {len(cadena)}).")
        if cantidad <= 0:
            raise ValueError("La cantidad de caracteres debe ser mayor que 0.")
        if inicio - 1 + cantidad > len(cadena):
            raise ValueError("La cantidad excede los caracteres disponibles desde la posición inicial.")

        print("\n--- Resultados ---")
        print(f"a) Con rebanadas: {eliminar_subcadena_a(cadena, inicio, cantidad)}")
        print(f"b) Sin rebanadas: {eliminar_subcadena_b(cadena, inicio, cantidad)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
