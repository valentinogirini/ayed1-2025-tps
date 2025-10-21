"""Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número
que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más."""

import random

def main() -> None:
    """
    Juega con el usuario a adivinar un número entre 1 y 500.

    Precondición: ninguna.

    Postcondición:
    - genera un número aleatorio entre 1 y 500.
    - cuenta los intentos, incluyendo entradas no numéricas.
    - informa si el número secreto es mayor o menor que el ingresado.
    - finaliza al adivinar el número, mostrando la cantidad de intentos.
    """
    numero_secreto = random.randint(1, 500)
    intentos = 0

    print("Adivina el número entre 1 y 500")
    while True:
        entrada = input("Ingrese su intento: ").strip()
        intentos += 1

        try:
            numero = int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero válido (se cuenta como intento).")
            continue

        if numero < numero_secreto:
            print("El número a adivinar es MAYOR.")
        elif numero > numero_secreto:
            print("El número a adivinar es MENOR.")
        else:
            print(f"\nCorrecto! El número era {numero_secreto}.")
            print(f"Lo adivinaste en {intentos} intento(s).")
            break


if __name__ == "__main__":
    main()
