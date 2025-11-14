"""Muchas aplicaciones financieras requieren que los números sean expresados también en letras.
Por ejemplo, el número 2153 puede escribirse como "dos mil ciento cincuenta y tres".
Escribir un programa que utilice una función para convertir un número entero entre 0 y 1 billón
(1.000.000.000.000) a letras. ¿En qué cambiaría la función si también aceptara números negativos?
¿Y números con decimales?"""

def unidades(n: int) -> str:
    """
    Convierte un número entre 0 y 9 a letras.

    Precondición: n es un entero entre 0 y 9 inclusive.

    Postcondición: retorna una cadena con el número en letras.
    """
    lista = [
        "cero", "uno", "dos", "tres", "cuatro",
        "cinco", "seis", "siete", "ocho", "nueve"
    ]
    return lista[n]


def especiales(n: int) -> str:
    """
    Convierte los números del 10 al 19 en letras.

    Precondición: n es un entero entre 10 y 19 inclusive.

    Postcondición: retorna el número en letras.
    """
    lista = [
        "diez", "once", "doce", "trece", "catorce",
        "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"
    ]
    return lista[n - 10]


def decenas(n: int) -> str:
    """
    Convierte un número entre 0 y 99 a letras.

    Precondición: n es un entero entre 0 y 99 inclusive.

    Postcondición: retorna la representación en letras.
    """
    if n < 10:
        return unidades(n)
    elif n >= 10 and n < 20:
        return especiales(n)
    else:
        decenas_lista = [
            "", "diez", "veinte", "treinta", "cuarenta",
            "cincuenta", "sesenta", "setenta", "ochenta", "noventa"
        ]
        d, u = divmod(n, 10)
        if u == 0:
            return decenas_lista[d]
        elif d == 2:
            return "veinti" + unidades(u)
        else:
            return f"{decenas_lista[d]} y {unidades(u)}"


def centenas(n: int) -> str:
    """
    Convierte un número entre 0 y 999 a letras.

    Precondición: n es un entero entre 0 y 999 inclusive.

    Postcondición: retorna el número expresado en letras.
    """
    if n < 100:
        return decenas(n)

    centenas_lista = [
        "", "ciento", "doscientos", "trescientos", "cuatrocientos",
        "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"
    ]
    c, resto = divmod(n, 100)
    if n == 100:
        return "cien"
    elif resto == 0:
        return centenas_lista[c]
    else:
        return f"{centenas_lista[c]} {decenas(resto)}"


def miles_y_mayores(n: int) -> str:
    """
    Convierte números de hasta 999,999,999,999 a letras.

    Precondición: n es un entero entre 0 y 999,999,999,999 inclusive.

    Postcondición: retorna el número expresado en letras en español.
    """
    if n < 1000:
        return centenas(n)

    grupos = [
        (1_000_000_000, "mil millones"),
        (1_000_000, "millón", "millones"),
        (1_000, "mil")
    ]

    partes = []
    for valor, *nombres in grupos:
        cantidad, n = divmod(n, valor)
        if cantidad == 0:
            continue
        if valor == 1_000_000:
            nombre = nombres[0] if cantidad == 1 else nombres[1]
            partes.append(f"{miles_y_mayores(cantidad)} {nombre}")
        else:
            partes.append(f"{miles_y_mayores(cantidad)} {nombres[0]}")
    if n > 0:
        partes.append(centenas(n))
    return " ".join(partes).replace("uno mil", "un mil").replace("uno millones", "un millón")


def numero_a_letras(n: int) -> str:
    """
    Convierte un número entero entre 0 y 1 billón a letras.

    Precondición: n es un entero entre 0 y 1 billón.

    Postcondición:
    - retorna una cadena con la representación del número en letras.
    - en caso de error, lanza una excepción controlada.
    """
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero.")
    if n < 0 or n > 1_000_000_000_000:
        raise ValueError("El número debe estar entre 0 y 1 billón inclusive.")

    if n == 0:
        return "cero"
    if n == 1_000_000_000_000:
        return "un billón"
    return miles_y_mayores(n).strip()


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición: se imprime en pantalla el número expresado en letras.
    """
    print("--- Conversor de Números a Letras ---\n")
    try:
        entrada = input("Ingrese un número entero entre 0 y 1 billón: ").strip()

        if not entrada.isdigit():
            raise ValueError("La entrada debe contener solo dígitos numéricos.")

        numero = int(entrada)
        resultado = numero_a_letras(numero)
        print(f"\n{numero} en letras es:\n {resultado}")

    except ValueError as e:
        print(f"\nError: {e}")
    except TypeError as e:
        print(f"\nError de tipo: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")


if __name__ == "__main__":
    main()
