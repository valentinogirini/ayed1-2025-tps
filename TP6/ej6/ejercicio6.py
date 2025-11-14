"""Un hotel necesita un programa para gestionar la operación de sus habitaciones. El hotel
cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo familiar que se 
aloja en el mismo se registra la siguiente información:
· DNI del cliente (número entero)
· Apellido y Nombre
· Fecha de ingreso (DDMMAAAA)
· Fecha de egreso (DDMMAAAA)
· Cantidad de ocupantes
Se solicita desarrollar un programa para realizar las siguientes tareas:
· Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de DNI -1.
Esta información deberá grabarse en un archivo CSV donde cada registro incluirá todos
los campos indicados más arriba. Tener en cuenta que los números de DNI no pueden
repetirse y que la fecha de salida debe ser mayor a la de entrada.
Finalizado el ingreso de huéspedes se solicita:
a. Leer el archivo de huéspedes y asignar la habitaciones a cada uno. El piso y
habitación son asignados arbitrariamente, y no puede asignarse una habitación ya
otorgada.
b. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
c. Mostrar cuántas habitaciones vacías hay en todo el hotel.
d. Mostrar el piso con mayor cantidad de personas.
e. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se ingresa
por teclado. Mostrar todas las que correspondan.
f. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado por
cantidad de días de alojamiento."""

from typing import List, Dict
import random
from datetime import datetime


def validar_fecha(fecha: str) -> bool:
    """
    Verifica que una fecha tenga formato DDMMAAAA válido.

    Precondición: fecha debe ser una cadena de 8 caracteres numéricos.

    Postcondición: devuelve True si la fecha es válida; False en caso contrario.
    """
    if len(fecha) != 8 or not fecha.isdigit():
        return False
    try:
        datetime.strptime(fecha, "%d%m%Y")
        return True
    except ValueError:
        return False


def dias_entre(fecha1: str, fecha2: str) -> int:
    """
    Calcula la cantidad de días entre dos fechas en formato DDMMAAAA.

    Precondición: ambas fechas deben tener formato DDMMAAAA válido.

    Postcondición: devuelve el número de días entre fecha1 y fecha2 (entero positivo o negativo).
    """
    try:
        d1 = datetime.strptime(fecha1, "%d%m%Y")
        d2 = datetime.strptime(fecha2, "%d%m%Y")
        return (d2 - d1).days
    except ValueError:
        return -1


def registrar_huespedes(ruta_archivo: str) -> None:
    """
    Registra huéspedes hasta ingresar DNI -1. Valida datos y graba en archivo CSV.

    Precondición: el archivo indicado por ruta_archivo debe ser accesible para escritura.

    Postcondición: se crea o sobrescribe el archivo CSV con los huéspedes válidos.
    """
    print("\n--- Registro de huéspedes ---\n")
    dnis_registrados = set()

    try:
        with open(ruta_archivo, "wt", encoding="utf-8-sig") as archivo:
            archivo.write("DNI,ApellidoNombre,Ingreso,Egreso,Personas\n")

            while True:
                dni = input("DNI del huésped (-1 para finalizar): ").strip()
                if dni == "-1":
                    break
                if not dni.isdigit():
                    print("DNI inválido (debe ser numérico).")
                    continue
                if dni in dnis_registrados:
                    print("DNI duplicado, ya registrado.")
                    continue

                nombre = input("Apellido y Nombre: ").strip().title()
                ingreso = input("Fecha de ingreso (DDMMAAAA): ").strip()
                egreso = input("Fecha de egreso (DDMMAAAA): ").strip()
                personas = input("Cantidad de ocupantes: ").strip()

                if not (validar_fecha(ingreso) and validar_fecha(egreso)):
                    print("Fechas inválidas.")
                    continue
                if dias_entre(ingreso, egreso) <= 0:
                    print("La fecha de egreso debe ser posterior a la de ingreso.")
                    continue
                if not personas.isdigit() or int(personas) <= 0:
                    print("Cantidad de personas inválida.")
                    continue

                dnis_registrados.add(dni)
                archivo.write(f"{dni},{nombre},{ingreso},{egreso},{personas}\n")

        print(f"\nDatos grabados correctamente en '{ruta_archivo}'.\n")

    except Exception as e:
        print(f"Error al registrar huéspedes: {e}")


def leer_huespedes(ruta_archivo: str) -> List[Dict[str, str]]:
    """
    Lee un archivo CSV de huéspedes y devuelve una lista de registros.

    Precondición: el archivo debe existir y tener un encabezado válido.

    Postcondición: devuelve una lista de diccionarios con las claves:
    dni, nombre, ingreso, egreso, personas.
    """
    huespedes = []
    try:
        with open(ruta_archivo, "rt", encoding="utf-8-sig") as archivo:
            next(archivo)
            for linea in archivo:
                campos = linea.strip().split(",")
                if len(campos) == 5:
                    dni, nombre, ingreso, egreso, personas = campos
                    huespedes.append({
                        "dni": dni,
                        "nombre": nombre,
                        "ingreso": ingreso,
                        "egreso": egreso,
                        "personas": int(personas)
                    })
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_archivo}'.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return huespedes


def asignar_habitaciones(huespedes: List[Dict[str, str]],
                         pisos: int, habitaciones_por_piso: int) -> List[Dict[str, str]]:
    """
    Asigna aleatoriamente habitaciones disponibles a cada huésped.

    Precondición:
    - la lista de huéspedes no debe estar vacía.
    - pisos y habitaciones_por_piso deben ser enteros positivos.

    Postcondición: devuelve la misma lista de huéspedes con 'piso' y 'habitacion' asignados.
    """
    disponibles = [(p, h) for p in range(1, pisos + 1)
                   for h in range(1, habitaciones_por_piso + 1)]
    random.shuffle(disponibles)

    for i, h in enumerate(huespedes):
        if i < len(disponibles):
            piso, habitacion = disponibles[i]
            h["piso"] = piso
            h["habitacion"] = habitacion
        else:
            h["piso"] = None
            h["habitacion"] = None
    return huespedes


def piso_mas_ocupado(huespedes: List[Dict[str, str]], pisos: int) -> int:
    """
    Determina el piso con mayor cantidad de habitaciones ocupadas.

    Precondición: huespedes debe incluir claves 'piso' asignadas.

    Postcondición: devuelve el número del piso más ocupado.
    """
    conteo = {p: 0 for p in range(1, pisos + 1)}
    for h in huespedes:
        if h["piso"]:
            conteo[h["piso"]] += 1
    return max(conteo, key=conteo.get)


def habitaciones_vacias(huespedes: List[Dict[str, str]],
                        pisos: int, habitaciones_por_piso: int) -> int:
    """
    Calcula la cantidad de habitaciones vacías en el hotel.

    Precondición: huespedes debe contener habitaciones asignadas o None.

    Postcondición: devuelve la cantidad de habitaciones disponibles.
    """
    total = pisos * habitaciones_por_piso
    ocupadas = sum(1 for h in huespedes if h["piso"])
    return total - ocupadas


def piso_con_mas_personas(huespedes: List[Dict[str, str]], pisos: int) -> int:
    """
    Determina el piso con mayor cantidad total de personas alojadas.

    Precondición: huespedes debe incluir clave 'personas' numérica.

    Postcondición: devuelve el número del piso con más personas.
    """
    personas_por_piso = {p: 0 for p in range(1, pisos + 1)}
    for h in huespedes:
        if h["piso"]:
            personas_por_piso[h["piso"]] += h["personas"]
    return max(personas_por_piso, key=personas_por_piso.get)


def proximas_desocupaciones(huespedes: List[Dict[str, str]],
                            fecha_actual: str) -> List[Dict[str, str]]:
    """
    Devuelve los huéspedes que egresan en la fecha actual.

    Precondición: fecha_actual debe tener formato DDMMAAAA válido.

    Postcondición: devuelve una lista de huéspedes que finalizan su estadía ese día.
    """
    return [h for h in huespedes if h["egreso"] == fecha_actual]


def listar_por_dias_alojamiento(huespedes: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Ordena los huéspedes por duración de estadía descendente.

    Precondición: huespedes debe tener fechas válidas.

    Postcondición: devuelve una nueva lista ordenada.
    """
    return sorted(huespedes,
                  key=lambda h: dias_entre(h["ingreso"], h["egreso"]),
                  reverse=True)


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se ejecuta el flujo completo del sistema hotelero.
    """
    print("\n--- Sistema de Gestión Hotelera ---")
    ruta = "huespedes.csv"
    pisos = 10
    habitaciones_por_piso = 6

    registrar_huespedes(ruta)
    huespedes = leer_huespedes(ruta)
    if not huespedes:
        print("No hay huéspedes registrados.")
        return

    huespedes = asignar_habitaciones(huespedes, pisos, habitaciones_por_piso)

    print(f"\nPiso más ocupado: {piso_mas_ocupado(huespedes, pisos)}")
    print(f"Habitaciones vacías: {habitaciones_vacias(huespedes, pisos, habitaciones_por_piso)}")
    print(f"Piso con más personas: {piso_con_mas_personas(huespedes, pisos)}")

    fecha_actual = input("\nIngrese la fecha actual (DDMMAAAA): ").strip()
    if not validar_fecha(fecha_actual):
        print("Fecha inválida.")
    else:
        desocupan = proximas_desocupaciones(huespedes, fecha_actual)
        if desocupan:
            print("\nHabitaciones que se desocupan hoy:")
            for h in desocupan:
                print(f"- {h['nombre']} (Piso {h['piso']}, Habitación {h['habitacion']})")
        else:
            print("No hay desocupaciones en esta fecha.")

    print("\nListado ordenado por cantidad de días de alojamiento:")
    for h in listar_por_dias_alojamiento(huespedes):
        dias = dias_entre(h["ingreso"], h["egreso"])
        print(f"{h['nombre']:25} {dias:3} días (Piso {h['piso']}, Hab {h['habitacion']})")


if __name__ == "__main__":
    main()
