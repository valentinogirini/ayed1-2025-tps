"""Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. 
Tener en cuenta que los comentarios comienzan con el signo # (siempre que éste no se encuentre encerrado 
entre comillas simples o dobles) y que también se considera comentario a las cadenas de documentación
(docstrings).
"""

def eliminar_comentarios_y_docstrings(nombre_entrada: str, nombre_salida: str) -> None:
    """
    Elimina todos los comentarios y docstrings de un archivo Python.

    Precondición:
    - nombre_entrada es el nombre de un archivo .py existente.
    - nombre_salida es el nombre del nuevo archivo a guardar sin comentarios/docstrings.

    Postcondición: crea un nuevo archivo con el código limpio (sin comentarios ni docstrings).
    """
    try:
        with open(nombre_entrada, "rt", encoding="utf-8-sig") as archivo:
            lineas = archivo.readlines()

        nuevo_codigo = []
        dentro_de_docstring = False
        delimitador_docstring = ""

        for linea in lineas:
            linea_strip = linea.strip()

            if not dentro_de_docstring and (linea_strip.startswith('"""') or linea_strip.startswith("'''")):
                if linea_strip.count('"""') == 2 or linea_strip.count("'''") == 2:
                    continue
                dentro_de_docstring = True
                delimitador_docstring = linea_strip[:3]
                continue
            elif dentro_de_docstring:
                if delimitador_docstring in linea_strip:
                    dentro_de_docstring = False
                continue

            nueva_linea = ""
            dentro_cadena = False
            i = 0
            while i < len(linea):
                if linea[i] in ("'", '"'):
                    if dentro_cadena == False:
                        dentro_cadena = linea[i]
                    elif dentro_cadena == linea[i]:
                        dentro_cadena = False
                    nueva_linea += linea[i]
                elif linea[i] == "#" and not dentro_cadena:
                    break 
                else:
                    nueva_linea += linea[i]
                i += 1

            if nueva_linea.strip(): 
                nuevo_codigo.append(nueva_linea.rstrip())

        with open(nombre_salida, "wt", encoding="utf-8-sig") as archivo:
            for linea in nuevo_codigo:
                archivo.write(linea + "\n")

        print(f"\nArchivo limpio guardado como '{nombre_salida}'.")
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_entrada}' no existe.")
    except OSError as e:
        print(f"Error al procesar archivos: {e}")


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.
    
    Postcondición: solicita nombres de archivo al usuario, limpia los comentarios y guarda el resultado.
    """
    print("--- ELIMINADOR DE COMENTARIOS Y DOCSTRINGS DE CÓDIGO PYTHON ---")
    entrada = input("Ingrese el nombre del archivo .py a procesar: ").strip()
    salida = input("Ingrese el nombre del nuevo archivo limpio: ").strip()


    if not entrada or not salida:
        print("Error: los nombres no pueden estar vacíos.")
        return

    eliminar_comentarios_y_docstrings(entrada, salida)


if __name__ == "__main__":
    main()
