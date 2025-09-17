"""Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado. """

from typing import List, Tuple

def cargar_pacientes() -> Tuple[List[int], List[int]]:
    """
    Permite ingresar pacientes hasta que se ingrese -1 como número de afiliado.
    Separa pacientes por urgencia y por turno.

    Precondiciones: Ninguna.

    Postcondiciones: Devuelve dos listas: pacientes_urgencia y pacientes_turno.
    """
    pacientes_urgencia = []
    pacientes_turno = []

    while True:
        num_afiliado = int(input("Ingrese número de afiliado (4 dígitos, -1 para terminar): "))
        if num_afiliado == -1:
            break

        if num_afiliado < 1000 or num_afiliado > 9999:
            print("Número inválido. Debe tener exactamente 4 dígitos.")
            continue

        tipo = int(input("Ingrese 0 para urgencia o 1 para turno: "))
        if tipo == 0:
            pacientes_urgencia.append(num_afiliado)
        elif tipo == 1:
            pacientes_turno.append(num_afiliado)
        else:
            print("Tipo inválido, intente nuevamente.")

    return pacientes_urgencia, pacientes_turno

def mostrar_listado(pacientes_urgencia: List[int], pacientes_turno: List[int]) -> None:
    """
    Muestra los pacientes atendidos por urgencia y por turno.

    Precondiciones: pacientes_urgencia y pacientes_turno son listas de enteros.

    Postcondiciones: Se imprime por pantalla el listado de pacientes atendidos.
    """
    print("\nPacientes atendidos por urgencia:")
    for i, paciente in enumerate(pacientes_urgencia):
        print(f"{i + 1}. Afiliado {paciente}")

    print("\nPacientes atendidos por turno:")
    for i, paciente in enumerate(pacientes_turno):
        print(f"{i + 1}. Afiliado {paciente}")

def cant_atenciones_afiliado(num: int, urgencia: List[int], turno: List[int]) -> Tuple[int, int]:
    """
    Cuenta cuántas veces un afiliado fue atendido por urgencia y por turno.

    Precondiciones: num es un entero de 4 dígitos; urgencia y turno son listas de enteros.

    Postcondiciones: Devuelve una tupla con las atenciones del afiliado.
    """
    return urgencia.count(num), turno.count(num)

def buscar_paciente(pacientes_urgencia: List[int], pacientes_turno: List[int]) -> None:
    """
    Permite buscar pacientes por número de afiliado y muestra cuántas veces
    fueron atendidos por urgencia y por turno, o si no existen.

    Precondiciones: pacientes_urgencia y pacientes_turno son listas de enteros con números de afiliado de 4 dígitos.

    Postcondiciones: Muestra por pantalla la cantidad de atenciones por urgencia y turno de cada paciente buscado.
    """
    while True:
        num_busqueda = int(input("Ingrese número de afiliado para buscar (-1 para salir): "))
        if num_busqueda == -1:
            break
        if num_busqueda < 1000 or num_busqueda > 9999:
            print("Número inválido. Debe tener exactamente 4 dígitos.")
            continue
        urg, tur = cant_atenciones_afiliado(num_busqueda, pacientes_urgencia, pacientes_turno)
        if urg == 0 and tur == 0:
            print(f"El afiliado {num_busqueda} no ha sido atendido en la clínica.\n")
        else:
            print(f"El afiliado {num_busqueda} fue atendido {urg} veces por urgencia y {tur} veces por turno.\n")

def menu() -> None:
    """
    Muestra el menú de navegación principal para la clínica, permitiendo cargar pacientes,
    ver listado de pacientes y buscar pacientes.

    Precondiciones: Ninguna.

    Postcondiciones: Ejecuta la acción correspondiente según la opción elegida hasta que se salga del menú.
    """
    pacientes_urgencia = []
    pacientes_turno = []

    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1: Cargar pacientes")
        print("2: Ver listado de pacientes")
        print("3: Buscar paciente")
        print("-1: Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            urg, tur = cargar_pacientes()
            pacientes_urgencia.extend(urg)
            pacientes_turno.extend(tur)
        elif opcion == "2":
            mostrar_listado(pacientes_urgencia, pacientes_turno)
        elif opcion == "3":
            buscar_paciente(pacientes_urgencia, pacientes_turno)
        elif opcion == "-1":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
