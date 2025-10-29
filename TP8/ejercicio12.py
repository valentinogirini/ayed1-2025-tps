"""Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio."""

def incrementar_cuadernos(precios: dict[str, float], porcentaje: float) -> None:
    """
    Incrementa el precio de los ítems que contienen 'cuaderno' en su nombre.

    Precondición:
    - precios es un diccionario con nombres de ítems como claves y precios como valores.
    - porcentaje es un número que indica el incremento (ej: 15 para 15%).

    Postcondición: modifica el diccionario aumentando los precios de los cuadernos.
    """
    for item in precios:
        if "cuaderno" in item.lower():
            precios[item] *= 1 + porcentaje / 100

def imprimir_lista(precios: dict[str, float]) -> None:
    """
    Imprime los ítems y sus precios.

    Precondición: precios es un diccionario válido.
    
    Postcondición: muestra los ítems y precios.
    """
    ancho_item = max(len(item) for item in precios)
    ancho_precio = max(len(f"{precio:.2f}") for precio in precios.values())
    print("\n--- Lista de precios ---")
    for item, precio in precios.items():
        print(f"{item:<{ancho_item}} : ${precio:>{ancho_precio}.2f}")

def item_mas_caro(precios: dict[str, float]) -> tuple[str, float]:
    """
    Retorna el ítem más costoso y su precio.

    Precondición: precios es un diccionario no vacío.
    
    Postcondición: retorna una tupla (max_item, precio).
    """
    max_item = max(precios, key=precios.get)
    return max_item, precios[max_item]

def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.
    
    Postcondición:
    - crea un diccionario de precios.
    - incrementa el precio de los cuadernos en 15%.
    - imprime la lista de precios.
    - indica cuál es el ítem más costoso.
    """
    precios = {
        "Cuaderno A4": 150.0,
        "Cuaderno A5": 100.0,
        "Lápiz": 20.0,
        "Borrador": 15.0,
        "Marcador": 50.0,
        "Resaltador": 40.0,
        "Regla": 30.0,
        "Mochila": 500.0
    }
    
    incrementar_cuadernos(precios, 15)
    imprimir_lista(precios)

    item, precio = item_mas_caro(precios)
    print(f"\nEl ítem más costoso es '{item}' con un precio de ${precio:.2f}.")


if __name__ == "__main__":
    main()

