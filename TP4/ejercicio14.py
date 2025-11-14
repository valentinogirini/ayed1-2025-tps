"""Se solicita crear un programa para leer direcciones de correo electrónico y verificar
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que
una dirección sea considerada válida el nombre de usuario debe poseer solamente
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
tener al menos un carácter y tiene que finalizar con .com o .com.ar.
Repetir el proceso de validación hasta ingresar una cadena vacía.
Al finalizar mostrar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente,
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas."""


import re

def es_correo_valido(correo: str) -> bool:
    """
    Verifica si una dirección de correo electrónico es válida según las siguientes reglas:
    - Contiene exactamente un '@'.
    - El nombre de usuario solo posee caracteres alfanuméricos.
    - El dominio tiene al menos un carácter.
    - Finaliza con '.com' o '.com.ar'.

    Precondición: correo es una cadena no vacía.

    Postcondición: retorna True si el correo es válido, False en caso contrario.
    """
    correo = correo.strip().lower()
    if correo == "":
        return False

    patron = r"^[a-z0-9]+@[a-z0-9]+\.(com|com\.ar)$"

    if not re.match(patron, correo):
        return False
    return True

def obtener_dominio(correo: str) -> str:
    """
    Extrae el dominio de una dirección de correo válida.

    Precondición: correo es válido.

    Postcondición: retorna el dominio en minúsculas.
    """
    correo = correo.strip().lower()
    _, dominio = correo.split("@")
    return dominio


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: muestra los dominios válidos ordenados alfabéticamente.
    """
    print("--- Validador de correos electrónicos ---\n")
    dominios = set()

    while True:
        try:
            correo = input("Ingrese una dirección de correo (Enter para finalizar): ").strip()

            if correo == "":
                break

            if es_correo_valido(correo):
                dominio = obtener_dominio(correo)
                dominios.add(dominio)
                print(f"Dirección válida: {correo.lower()}")
            else:
                print(f"Dirección inválida: {correo}")

        except Exception as e:
            print(f"Error inesperado: {e}")

    if dominios:
        print("\n--- Dominios válidos ingresados ---")
        for d in sorted(dominios):
            print(f"- {d}")
    else:
        print("\nNo se ingresaron direcciones válidas.")


if __name__ == "__main__":
    main()
