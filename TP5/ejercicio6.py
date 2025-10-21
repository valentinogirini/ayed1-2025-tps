"""El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

def main() -> None:
    """
    Carga una lista de números enteros ingresados por el usuario y permite buscar
    la posición de elementos utilizando el método index.

    Precondición: ninguna.

    Postcondición:
    - imprime la posición de los elementos buscados si existen en la lista.
    - imprime un mensaje de error si el elemento no existe.
    - detiene el programa al tercer error.
    """
    numeros = []
    print("Ingrese números enteros para la lista (terminar con -1):")
    while True:
        try:
            entrada = input("Número: ").strip()
            numero = int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue

        if numero == -1:
            break
        numeros.append(numero)
    
    if not numeros:
        print("No se ingresaron números en la lista. Fin del programa.")
        return
    
    errores = 0
    while errores < 3:
        try:
            entrada_buscar = input("Ingrese un número a buscar en la lista: ").strip()
            numero_buscar = int(entrada_buscar)
        except ValueError:
            print("Error: debe ingresar un número entero.")
            errores += 1
            continue

        try:
            posicion = numeros.index(numero_buscar)
            print(f"El número {numero_buscar} se encuentra en la posición {posicion}.")
        except ValueError:
            errores += 1
            print(f"Error: el número {numero_buscar} no se encuentra en la lista.")
    
    print("Se alcanzó el máximo de 3 errores. Fin del programa.")
            

if __name__ == "__main__":
    main()
