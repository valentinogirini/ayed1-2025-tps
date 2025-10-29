"""Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

def eliminar_claves(diccionario: dict[str, any], claves: list[str]) -> tuple[int, list[str]]:
    """
    Elimina del diccionario todas las claves contenidas en la lista.

    Precondición:
    - diccionario es un diccionario válido.
    - claves es una lista de posibles claves a eliminar.

    Postcondición:
    - modifica el diccionario original eliminando las claves válidas.
    - retorna una tupla con la cantidad de claves eliminadas y la lista de claves inválidas.
    """
    eliminadas = 0
    claves_invalidas = []

    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            eliminadas += 1
        else:
            claves_invalidas.append(clave)

    return eliminadas, claves_invalidas


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.
    
    Postcondición: muestra el diccionario modificado solo si se eliminaron claves válidas.
    """
    datos = {
        "nombre": "Juan",
        "edad": 43,
        "ciudad": "Buenos Aires",
        "profesion": "Ingeniero en sistemas"
    }

    print("--- Diccionario original ---")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

    claves_eliminar = input("\nIngrese las claves a eliminar separadas por espacios: ").lower().split()

    cantidad, invalidas = eliminar_claves(datos, claves_eliminar)

    if cantidad == 0:
        print("\nNo se eliminaron claves válidas. Ningún cambio realizado.")
    else:
        print(f"\nSe eliminaron {cantidad} clave(s) válida(s).")
        if datos:
            print("\n--- Diccionario modificado ---")
            for clave, valor in datos.items():
                print(f"{clave}: {valor}")
        else:
            print("El diccionario ha quedado vacío.")

        if invalidas:
            print(f"\nLas siguientes claves no existen: {', '.join(invalidas)}")


if __name__ == "__main__":
    main()
