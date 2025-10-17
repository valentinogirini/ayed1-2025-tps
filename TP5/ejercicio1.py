"""Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""

def ingresar_numero_natural() -> int:
    """
    Solicita al usuario que ingrese un número entero mayor que 0.

    Precondición: ninguna.

    Postcondición:
    - retorna el número ingresado si es válido.
    - muestra mensajes de error específicos en caso de ingreso inválido.
    """
    while True:
        try:
            valor = input("Ingrese un número natural: ").strip()

            if valor == "":
                raise ValueError("No se ingresó ningún valor.")

            try:
                numero = float(valor)
            except ValueError:
                raise ValueError("Debe ingresar un número válido (solo dígitos).")

            if not numero.is_integer():
                raise ValueError("El número ingresado no es un entero.")

            numero = int(numero)

            if numero <= 0:
                raise ValueError("El número debe ser mayor que 0.")

            return numero

        except ValueError as error:
            print(f"Error: {error}")


def main() -> None:
    """
    Permite probar la función ingresar_numero_natural.

    Precondición: ninguna.

    Postcondición: imprime el número natural ingresado correctamente por el usuario.
    """
    valor = ingresar_numero_natural()
    print(f"Número ingresado correctamente: {valor}")


if __name__ == "__main__":
    main()
