"""Escribir un programa que lea un archivo de texto conteniendo un conjunto de
apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con
la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto."""

def clasificar_por_origen(nombre_archivo: str) -> None:
    """
    Clasifica apellidos según su terminación y los guarda en archivos separados.

    Precondición: nombre_archivo existe y contiene nombres en formato "Apellido, Nombre" (una persona por línea).

    Postcondición:
    - Crea o sobrescribe los archivos:
        - ARMENIA.TXT con apellidos terminados en "IAN"
        - ITALIA.TXT con apellidos terminados en "INI"
        - ESPAÑA.TXT con apellidos terminados en "EZ"
    - Descarta los registros con otros apellidos.
    """
    try:
        with open(nombre_archivo, "rt", encoding="utf-8-sig") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("El archivo está vacío.")
            return

        with open("ARMENIA.TXT", "wt", encoding="utf-8-sig") as armenia, \
             open("ITALIA.TXT", "wt", encoding="utf-8-sig") as italia, \
             open("ESPAÑA.TXT", "wt", encoding="utf-8-sig") as españa:

            contador = {"IAN": 0, "INI": 0, "EZ": 0, "DESCARTADOS": 0}

            for linea in lineas:
                registro = linea.strip()
                if not registro:
                    continue

                if "," not in registro:
                    print(f"Advertencia: formato inválido -> '{registro}' (se descarta)")
                    contador["DESCARTADOS"] += 1
                    continue

                apellido, nombre = map(str.strip, registro.split(",", 1))
                apellido_mayus = apellido.upper()

                if apellido_mayus.endswith("IAN"):
                    armenia.write(f"{registro}\n")
                    contador["IAN"] += 1
                elif apellido_mayus.endswith("INI"):
                    italia.write(f"{registro}\n")
                    contador["INI"] += 1
                elif apellido_mayus.endswith("EZ"):
                    españa.write(f"{registro}\n")
                    contador["EZ"] += 1
                else:
                    contador["DESCARTADOS"] += 1

        print("\nClasificación completada correctamente.\n")
        print("Resumen de registros procesados:")
        print(f"  ARMENIA.TXT -> {contador['IAN']} personas")
        print(f"  ITALIA.TXT  -> {contador['INI']} personas")
        print(f"  ESPAÑA.TXT  -> {contador['EZ']} personas")
        print(f"  Descartados -> {contador['DESCARTADOS']} personas")

    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
    except OSError as e:
        print(f"Error al procesar archivos: {e}")


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.
    
    Postcondición: solicita el nombre de un archivo y clasifica los registros según su origen.
    """
    print("--- CLASIFICADOR DE NOMBRES POR ORIGEN ---\n")

    nombre_archivo = input("Ingrese el nombre del archivo a procesar (por ejemplo, 'nombres.txt'): ").strip()

    if not nombre_archivo:
        print("Error: debe ingresar un nombre de archivo válido.")
        return

    clasificar_por_origen(nombre_archivo)


if __name__ == "__main__":
    main()

