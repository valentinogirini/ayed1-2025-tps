"""Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron.
"""

from typing import List

def cargar_ingresos() -> List[int]:
    """
    Permite ingresar los números de socios que visitan el club.
    Finaliza al ingresar 0.

    Precondiciones: Los números de socio deben ser enteros de 5 dígitos o 0 para terminar.

    Postcondiciones: Devuelve una lista con los números de socio que ingresaron al club.
    """
    ingresos = []
    while True:
        socio = int(input("Ingrese número de socio (5 dígitos, 0 para terminar): "))
        if socio == 0:
            break
        if socio < 10000 or socio > 99999:
            print("Número inválido. Debe tener exactamente 5 dígitos.")
            continue
        ingresos.append(socio)
    return ingresos

def mostrar_conteo(ingresos: List[int]) -> None:
    """
    Muestra cada socio una sola vez y cuántas veces ingresó.

    Precondiciones: ingresos es una lista de enteros de 5 dígitos.

    Postcondiciones: Se imprime por pantalla el listado de socios y su cantidad de ingresos.
    """
    if not ingresos:
        print("\nNo hay registros de ingresos aún.")
    else:
        socios_unicos = []
        for socio in ingresos:
            if socio not in socios_unicos:
                socios_unicos.append(socio)
                print(f"Socio {socio}: {ingresos.count(socio)} ingresos")

def eliminar_socio(ingresos: List[int], socio_baja: int) -> int:
    """
    Elimina todas las entradas de un socio dado de baja.

    Precondiciones: ingresos es una lista de enteros; socio_baja es un entero de 5 dígitos.

    Postcondiciones: Modifica la lista ingresos eliminando al socio dado de baja.
                     Devuelve la cantidad de ingresos eliminados.
    """
    eliminados = ingresos.count(socio_baja)
    for _ in range(eliminados):
        ingresos.remove(socio_baja)
    return eliminados

def procesar_baja(ingresos: List[int]) -> None:
    """
    Permite dar de baja a un socio y mostrar los ingresos antes y después de eliminarlo.

    Precondiciones: ingresos es una lista de enteros de 5 dígitos.

    Postcondiciones: Modifica la lista ingresos eliminando al socio dado de baja
                     y muestra por pantalla los registros antes y después.
    """
    if not ingresos:
        print("\nNo hay ingresos cargados.")
    else:
        socio_baja = int(input("Ingrese número de socio dado de baja: "))
        if socio_baja < 10000 or socio_baja > 99999:
            print("Número inválido. Debe tener exactamente 5 dígitos.")
        else:
            ingresos_antes = []
            ingresos_antes.extend(ingresos)
            eliminados = eliminar_socio(ingresos, socio_baja)

            if eliminados == 0:
                print(f"No se encontró al socio {socio_baja}.")
            else:
                print("\n--- Antes de eliminar ---")
                mostrar_conteo(ingresos_antes)

                print("\n--- Después de eliminar ---")
                mostrar_conteo(ingresos)
                print(f"\nSe eliminaron {eliminados} ingresos del socio {socio_baja}.")


def main() -> None:
    """
    Función principal que ejecuta el menú interactivo para el registro de socios.

    Precondiciones: Ninguna.

    Postcondiciones: Ejecuta las acciones correspondientes según la opción elegida hasta salir del programa.
    """
    ingresos = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Cargar ingresos de socios")
        print("2. Mostrar conteo de ingresos")
        print("3. Eliminar socio dado de baja")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo del programa...")
            break
        elif opcion == "1":
            ingresos.extend(cargar_ingresos())
        elif opcion == "2":
            mostrar_conteo(ingresos)
        elif opcion == "3":
            procesar_baja(ingresos)
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main()
