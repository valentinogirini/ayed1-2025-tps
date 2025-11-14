"""Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:

GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta.

GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas,
leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes.

MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo"""

def GrabarRangoAlturas(nombre_archivo: str) -> None:
    """
    Permite ingresar las alturas de atletas por disciplina y las guarda en un archivo.

    Precondición: nombre_archivo es una cadena válida.

    Postcondición: crea o sobrescribe el archivo con los nombres de los deportes y alturas
    en líneas separadas.
    """
    print("\n--- CARGA DE ALTURAS POR DEPORTE ---")
    print("Ingrese 'FIN' como nombre de deporte para finalizar.\n")

    try:
        with open(nombre_archivo, "at", encoding="utf-8-sig") as archivo:
            while True:
                deporte = input("Ingrese el nombre del deporte (o 'FIN' para terminar): ").strip()
                if deporte.upper() == "FIN":
                    break

                if not deporte:
                    print("Error: el nombre del deporte no puede estar vacío.")
                    continue

                archivo.write(f"{deporte}\n")

                while True:
                    entrada = input("Ingrese la altura del atleta en cm (ENTER para cambiar de deporte): ").strip()
                    if not entrada:
                        break
                    try:
                        altura = float(entrada)
                        if altura <= 0:
                            print("Error: la altura debe ser positiva.")
                            continue
                        archivo.write(f"{altura}\n")
                    except ValueError:
                        print("Error: debe ingresar un número válido.")
        print(f"\nDatos grabados correctamente en '{nombre_archivo}'.\n")

    except OSError as e:
        print(f"Error al grabar el archivo: {e}")


def GrabarPromedio(archivo_alturas: str, archivo_promedios: str) -> None:
    """
    Lee un archivo con alturas por deporte y graba otro con los promedios por disciplina.

    Precondición:
    - archivo_alturas existe y tiene datos en el formato correcto.
    - cada bloque comienza con el nombre del deporte y sigue con alturas (float) hasta el siguiente deporte.

    Postcondición: crea un nuevo archivo con pares de líneas: deporte, promedio.
    """
    try:
        with open(archivo_alturas, "rt", encoding="utf-8-sig") as origen, \
             open(archivo_promedios, "wt", encoding="utf-8-sig") as destino:

            deporte_actual = None
            alturas = []

            for linea in origen:
                linea = linea.strip()
                if not linea:
                    continue

                try:
                    altura = float(linea)
                    alturas.append(altura)
                except ValueError:
                    if deporte_actual and alturas:
                        promedio = sum(alturas) / len(alturas)
                        destino.write(f"{deporte_actual}\n{promedio:.2f}\n")
                    deporte_actual = linea
                    alturas = []

            if deporte_actual and alturas:
                promedio = sum(alturas) / len(alturas)
                destino.write(f"{deporte_actual}\n{promedio:.2f}\n")

        print(f"\nArchivo de promedios generado correctamente en '{archivo_promedios}'.\n")

    except FileNotFoundError:
        print(f"Error: el archivo '{archivo_alturas}' no existe.")
    except OSError as e:
        print(f"Error al procesar archivos: {e}")


def MostrarMasAltos(archivo_promedios: str) -> None:
    """
    Muestra los deportes cuyos promedios de altura superan el promedio general.

    Precondición: archivo_promedios existe y contiene pares de líneas: deporte, promedio.

    Postcondición: muestra los deportes con promedio superior al general.
    """
    try:
        with open(archivo_promedios, "rt", encoding="utf-8-sig") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]

        if len(lineas) % 2 != 0:
            print("Error: formato inválido en el archivo de promedios.")
            return

        deportes = []
        promedios = []

        for i in range(0, len(lineas), 2):
            deporte = lineas[i]
            promedio = float(lineas[i + 1])
            deportes.append(deporte)
            promedios.append(promedio)

        promedio_general = sum(promedios) / len(promedios)
        print(f"\nPromedio general de alturas: {promedio_general:.2f} cm\n")
        print("Deportes con promedio superior al general:")

        encontrados = False
        for deporte, promedio in zip(deportes, promedios):
            if promedio > promedio_general:
                print(f"  - {deporte}: {promedio:.2f} cm")
                encontrados = True

        if not encontrados:
            print("  Ninguno supera el promedio general.")

    except FileNotFoundError:
        print(f"Error: el archivo '{archivo_promedios}' no existe.")
    except ValueError:
        print("Error: el archivo contiene datos no numéricos.")
    except OSError as e:
        print(f"Error al leer el archivo: {e}")


def main() -> None:
    """
    Función principal del programa.
    
    Precondición: ninguna.
    
    Postcondición: se ejecuta el menú y la opción seleccionada.
    """
    archivo_alturas = "alturas.txt"
    archivo_promedios = "promedios.txt"

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Grabar alturas por deporte")
        print("2. Calcular promedios por deporte")
        print("3. Mostrar deportes con atletas más altos que el promedio general")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            GrabarRangoAlturas(archivo_alturas)
        elif opcion == "2":
            GrabarPromedio(archivo_alturas, archivo_promedios)
        elif opcion == "3":
            MostrarMasAltos(archivo_promedios)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()