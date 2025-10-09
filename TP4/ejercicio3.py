"""Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89."""

from typing import Tuple

def separar_claves(clave_maestra: str) -> Tuple[str, str]:
    """
    Separa la clave maestra en dos claves: una con los dígitos en posiciones impares
    y otra con los dígitos en posiciones pares.
    
    Precondición: clave_maestra es una cadena que contiene sólo dígitos y no es vacía.
    
    Postcondición: retorna una tupla (clave1, clave2) donde cada elemento es la cadena
                    formada por los dígitos correspondientes.
    """
    impares = []
    pares = []
    for pos, dig in enumerate(clave_maestra, start=1):
        if pos % 2 == 1:
            impares.append(dig)
        else:
            pares.append(dig)
    return ("".join(impares), "".join(pares))


def main() -> None:
    """
    Lee la clave maestra desde entrada y muestra las dos claves resultantes.
    
    Precondición: ninguna.
    
    Postcondición: imprime por pantalla la clave 1 (dígitos en posiciones impares)
                    y la clave 2 (dígitos en posiciones pares) o un mensaje de error
                    si la entrada no es válida.
    """
    clave = input("Ingrese la clave maestra: ")
    try:
        if clave.isdigit():
            c1, c2 = separar_claves(clave)
            print(f"Clave 1: {c1}")
            print(f"Clave 2: {c2}")
        else:
            raise ValueError
    except ValueError:
        print("Entrada inválida. Debe ingresar sólo números positivos sin signos.")



if __name__ == "__main__":
    main()
