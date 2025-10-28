"""Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido
del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes."""

def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición:
    - solicita números al usuario para eliminarlos del conjunto.
    - imprime el conjunto luego de cada eliminación.
    - finaliza al ingresar -1.
    - maneja errores si se intenta eliminar un elemento que no está en el conjunto.
    """

    numeros = set(range(10))
    print(f"Conjunto inicial: {numeros}")

    while True:
        try:
            entrada = input("\nIngrese un número a eliminar (-1 para salir): ").strip()
            numero = int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue

        if numero == -1:
            print("Fin del programa.")
            break

        try:
            numeros.remove(numero)
            if not numeros:
                print("El conjunto ha quedado vacío. Fin del programa.")
                break
            print(f"Conjunto actualizado: {numeros}")
        except KeyError:
            print(f"Error: el número {numero} no está en el conjunto.")
        


if __name__ == "__main__":
    main()