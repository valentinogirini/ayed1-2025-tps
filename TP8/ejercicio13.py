"""Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario.
Comprobar el comportamiento de la función mediante un programa apropiado."""

def buscar_clave(diccionario: dict[str, any], valor_buscado: any) -> list[str]:
    """
    Devuelve una lista con todas las claves del diccionario
    que mapean al valor indicado.

    Precondición: diccionario es un diccionario válido.

    Postcondición: retorna una lista con las claves correspondientes.
    """
    return [clave for clave, valor in diccionario.items() if valor == valor_buscado]


def main() -> None:
    """
    Función principal del programa.
    
    Precondición: ninguna.

    Postcondición: muestra las claves que mapean a ese valor si existen.
    """
    inventario = {
        "manzana": 10,
        "banana": 5,
        "durazno": 10,
        "frutilla": 8,
        "pera": 5
    }
    
    print("--- Inventario ---")
    for k, v in inventario.items():
        print(f"{k:<10} -> {v:>3}")

    valor_ingresado = input("\nIngrese el valor a buscar: ").strip()

    if valor_ingresado.isdigit():
        valor_buscar = int(valor_ingresado)
    else:
        valor_buscar = valor_ingresado

    claves = buscar_clave(inventario, valor_buscar)

    if claves:
        print(f"\nClaves que tienen el valor {valor_buscar}: {', '.join(claves)}")
    else:
        print(f"\nNo se encontraron claves con el valor {valor_buscar}.")


if __name__ == "__main__":
    main()
