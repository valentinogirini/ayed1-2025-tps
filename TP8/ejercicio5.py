"""Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función."""

def son_ortogonales(v1: tuple[float, float], v2: tuple[float, float]) -> bool:
    """
    Determina si dos vectores en el plano son ortogonales.

    Precondición: v1 y v2 son tuplas de dos números reales, que representan
    las componentes de los vectores en el plano cartesiano.

    Postcondición: retorna True si el producto escalar entre ambos vectores es 0, False en caso contrario.
    """
    producto_escalar = v1[0] * v2[0] + v1[1] * v2[1]
    return producto_escalar == 0


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: solicita al usuario los componentes de dos vectores,
    invoca la función son_ortogonales() y muestra el resultado.
    """
    try:
        x1 = float(input("Ingrese la componente x del primer vector: "))
        y1 = float(input("Ingrese la componente y del primer vector: "))
        x2 = float(input("Ingrese la componente x del segundo vector: "))
        y2 = float(input("Ingrese la componente y del segundo vector: "))
    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")
        return

    v1 = (x1, y1)
    v2 = (x2, y2)

    if son_ortogonales(v1, v2):
        print(f"\nLos vectores {v1} y {v2} son ortogonales.")
    else:
        print(f"\nLos vectores {v1} y {v2} no son ortogonales.")


if __name__ == "__main__":
    main()
