"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones."""

def obtener_mes(numero_mes: int) -> str:
    """
    Devuelve el nombre del mes correspondiente al número recibido.

    Precondición: numero_mes es un entero.

    Postcondición:
    - retorna una cadena con el nombre del mes si el número es válido (1-12).
    - retorna una cadena vacía si el número no corresponde a un mes.
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    try:
        if numero_mes < 1:
            raise IndexError
        return meses[numero_mes - 1]
    except IndexError:
        return ""


def main() -> None:
    """
    Solicita al usuario un número de mes y muestra el nombre correspondiente.

    Precondición: ninguna.

    Postcondición:
    - imprime el nombre del mes si el número es válido.
    - imprime un mensaje de error si el número es inválido.
    """
    try:
        numero_str = input("Ingrese el número del mes (1-12): ").strip()
        numero_mes = int(numero_str)

        nombre_mes = obtener_mes(numero_mes)
        if nombre_mes == "":
            print("Número de mes inválido.")
        else:
            print(f"El mes correspondiente es: {nombre_mes}")

    except ValueError:
        print("Error: debe ingresar un número entero.")


if __name__ == "__main__":
    main()
