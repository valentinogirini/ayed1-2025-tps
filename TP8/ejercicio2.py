"""Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado."""

def es_bisiesto(año: int) -> bool:
    """
    Determina si un año es bisiesto.
    
    Precondición: año es un número entero mayor que 0.
    
    Postcondición: retorna True si el año es bisiesto, False en caso contrario.
    """
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


def dias_en_mes(mes: int, año: int) -> int:
    """
    Retorna la cantidad de días válidos para un mes determinado.
    
    Precondición:
    - mes es un entero entre 1 y 12.
    - año es un entero mayor que 0.
    
    Postcondición: retorna un entero con la cantidad de días correspondiente al mes y año indicados.
    """
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if es_bisiesto(año):
            return 29
        return 28
    return 0


def formatear_fecha(fecha: tuple[int, int, int]) -> str:
    """
    Convierte una fecha (día, mes, año) en formato extendido.

    Precondición: fecha es una tupla de tres enteros: (día, mes, año). El año puede tener 2 o 4 dígitos.

    Postcondición:
    - retorna una cadena con la fecha en formato: "12 de octubre de 2030".
    - si la fecha es inválida, devuelve un mensaje de error.
    """
    dia, mes, año = fecha
    año_corte = 30

    nombres_meses = {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
        5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
        9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }

    if mes < 1 or mes > 12:
        return "Error: mes inválido."

    if año < 0:
        return "Error: año inválido"

    if año >= 0 and año <= 99:
        if año <= año_corte:
            año = 2000 + año
        else:
            año = 1900 + año

    max_dias = dias_en_mes(mes, año)
    if dia < 1 or dia > max_dias:
        return f"Error: el día {dia} no es válido para {nombres_meses[mes]} de {año}."
    return f"{dia} de {nombres_meses[mes]} de {año}"


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.
    
    Postcondición: solicita una fecha, invoca la función y muestra el resultado.
    """
    try:
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes (1-12): "))
        año = int(input("Ingrese el año (2 o 4 dígitos): "))
    except ValueError:
        print("Error: debe ingresar valores numéricos válidos.")
        return

    fecha = (dia, mes, año)
    resultado = formatear_fecha(fecha)
    print(f"\nFecha en formato extendido:\n{resultado}")


if __name__ == "__main__":
    main()


