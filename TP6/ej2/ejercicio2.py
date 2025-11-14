"""Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse
después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria."""


def dividir_archivo(nombre_archivo: str, tamaño_max: int) -> None:
    """
    Divide un archivo de texto en varias partes sin romper líneas.

    Precondición:
    - nombre_archivo existe y es un archivo de texto accesible.
    - tamaño_max es un entero positivo (expresado en bytes).

    Postcondición:
    - Crea archivos con el mismo nombre base y un sufijo.
    - No se rompe ninguna línea entre archivos.
    - Muestra un mensaje de error si el proceso falla.
    """

    try:
        with open(nombre_archivo, "rt", encoding="utf-8-sig") as origen:
            contenido_valido = False
            for linea in origen:
                if linea.strip():
                    contenido_valido = True
                    break

            if not contenido_valido:
                print(f"Error: el archivo '{nombre_archivo}' está vacío.")
                return
            
            origen.seek(0)
            
            if "." in nombre_archivo:
                base = nombre_archivo[:nombre_archivo.rfind(".")]
                ext = nombre_archivo[nombre_archivo.rfind("."):]
            else:
                base = nombre_archivo
                ext = ".txt"

            parte_num = 1
            tamaño_actual = 0
            salida = open(f"{base}_parte{parte_num}{ext}", "wt", encoding="utf-8-sig")

            for linea in origen:
                bytes_linea = len(linea.encode("utf-8-sig"))

                if tamaño_actual + bytes_linea > tamaño_max:
                    salida.close()
                    parte_num += 1
                    tamaño_actual = 0
                    salida = open(f"{base}_parte{parte_num}{ext}", "wt", encoding="utf-8-sig")

                salida.write(linea)
                tamaño_actual += bytes_linea

            salida.close()

        print(f"\nArchivo dividido correctamente en {parte_num} parte(s).")

    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
    except OSError as e:
        print(f"Error al procesar el archivo: {e}")


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.
    
    Postcondición:
    - Solicita al usuario el nombre de un archivo y el tamaño máximo.
    - Divide el archivo sin cargarlo completamente en memoria.
    """
    print("--- DIVISOR DE ARCHIVOS DE TEXTO ---\n")

    nombre_archivo = input("Ingrese el nombre del archivo a dividir (por ejemplo 'numeros.txt'): ").strip()
    if not nombre_archivo:
        print("Error: debe ingresar un nombre de archivo válido.")
        return

    try:
        tamaño_max = int(input("Ingrese el tamaño máximo de cada parte (en bytes): "))
        if tamaño_max <= 0:
            raise ValueError
    except ValueError:
        print("Error: el tamaño máximo debe ser un número entero mayor que 0.")
        return

    dividir_archivo(nombre_archivo, tamaño_max)


if __name__ == "__main__":
    main()


