"""Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio."""

def encajan(ficha1: tuple[int, int], ficha2: tuple[int, int]) -> bool:
    """
    Determina si dos fichas de dominó encajan o no.

    Precondición: ficha1, ficha2: tuplas con dos valores enteros cada una, entre 0 y 6.
    
    Postcondición: retorna True si las fichas encajan (tienen al menos un número en común), false en caso contrario.
    """
    
    return bool(set(ficha1).intersection(set(ficha2)))


def pedir_ficha(numero_ficha: int) -> tuple[int, int]:
    """
    Pide al usuario los valores de una ficha de dominó.

    Precondición: numero_ficha: número de ficha (1 o 2).
    
    Postcondición: retorna una tupla con dos valores enteros entre 0 y 6.
    """

    print(f"\nFicha {numero_ficha}:")
    ficha = ()

    for i in range(2):
        while True:
            try:
                valor = int(input(f"Ingrese el número {i + 1}. (0 a 6): "))
                if valor < 0 or valor > 6:
                    print("Error: el valor debe estar entre 0 y 6.")
                else:
                    ficha += valor,
                    break
            except ValueError:
                print("Error: debe ingresar un número entero.")
    return ficha


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.
    
    Postcondición: imprime si las fichas encajan o no según sus valores.
    """

    ficha1 = pedir_ficha(1)
    ficha2 = pedir_ficha(2)

    if encajan(ficha1, ficha2):
        print(f"\nLas fichas {ficha1} y {ficha2} encajan!")
    else:
        print(f"\nLas fichas {ficha1} y {ficha2} no encajan!")


if __name__ == "__main__":
    main()
    
