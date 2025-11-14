"""Se dispone de dos formatos diferentes de archivos de texto en los que se almacenan
datos de empleados, detallados más abajo. Desarrollar un programa para convertir cada
uno de los formatos suministrados, grabando los datos obtenidos en
otro archivo con formato CSV. Los archivos de entrada pueden generarse con Block
de Notas o cualquier otro editor, copiando y pegando los ejemplos proporcionados.
Ambos archivos tienen tres campos por registro: Apellido y Nombre, Fecha de alta
y Domicilio."""

from typing import List

def leer_formato1(ruta: str) -> List[List[str]]:
    """
    Lee un archivo de texto en formato fijo y devuelve los registros.

    Precondición: el archivo debe existir y tener el formato indicado.

    Postcondición: devuelve una lista de listas con los campos de cada empleado.
    """
    empleados = []
    try:
        with open(ruta, "rt", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                nombre = linea[0:20].strip()
                fecha = linea[20:29].strip()
                domicilio = linea[29:].strip()
                empleados.append([nombre, fecha, domicilio])
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
    except Exception as e:
        print(f"Error inesperado al leer formato 1: {e}")
    return empleados


def leer_formato2(ruta: str) -> List[List[str]]:
    """
    Lee un archivo en formato con longitudes prefijadas por dos dígitos.

    Precondición: el archivo debe existir y tener el formato correcto.

    Postcondición: devuelve una lista de listas con los campos de cada empleado.
    """
    empleados = []
    try:
        with open(ruta, "rt", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                campos = []
                i = 0
                linea = linea.strip()
                while i < len(linea):
                    longitud_str = linea[i:i+2]
                    if not longitud_str.isdigit():
                        raise ValueError(f"Longitud inválida en la posición {i}: '{longitud_str}'")
                    longitud = int(longitud_str)
                    i += 2
                    campo = linea[i:i+longitud]
                    campos.append(campo)
                    i += longitud
                empleados.append(campos)
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
    except Exception as e:
        print(f"Error inesperado al leer formato 2: {e}")
    return empleados


def escribir_csv(ruta_salida: str, registros: List[List[str]]) -> None:
    """
    Escribe los registros en un archivo CSV.

    Precondición: registros no debe estar vacío.

    Postcondición: se genera o sobrescribe el archivo CSV con los datos.
    """
    if not registros:
        print("No hay datos para escribir en el CSV.")
        return

    try:
        with open(ruta_salida, "wt", encoding="utf-8-sig") as archivo:
            archivo.write("Apellido y Nombre,Fecha de Alta,Domicilio\n")

            for fila in registros:
                fila_limpia = [campo.replace(",", " ") for campo in fila]
                linea = ",".join(fila_limpia)
                archivo.write(linea + "\n")

        print(f"\nArchivo CSV generado correctamente: {ruta_salida}\n")

    except PermissionError:
        print("Error: permisos insuficientes para escribir el archivo.")
    except Exception as e:
        print(f"Error inesperado al escribir el CSV: {e}")


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se convierte el archivo de entrada al formato CSV o se informa un error.
    """
    print("--- Conversor de archivos de empleados a CSV ---\n")
    print("Formatos disponibles:")
    print("1. Formato fijo (campos de longitud fija).")
    print("2. Formato con longitudes prefijadas (dos dígitos por campo).")

    try:
        formato = int(input("\nIngrese el formato del archivo (1 o 2): "))
        if formato not in (1, 2):
            print("Formato inválido. Debe ser 1 o 2.")
            return

        ruta_entrada = input("Ingrese la ruta del archivo de entrada: ").strip()
        ruta_salida = input("Ingrese el nombre del archivo CSV de salida: ").strip()

        if formato == 1:
            registros = leer_formato1(ruta_entrada)
        else:
            registros = leer_formato2(ruta_entrada)

        escribir_csv(ruta_salida, registros)

    except ValueError:
        print("Error: el formato debe ser 1 o 2.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
