"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C."""

def main() -> None:
    """
    Imprime los números enteros del 1 al 100.000 y maneja la interrupción por Ctrl-C.

    Precondición: ninguna.

    Postcondición:
    - imprime los números del 1 al 100.000.
    - si el usuario presiona Ctrl-C, solicita confirmación antes de detener el programa.
    """
    for numero in range(1, 100_001):
        try:
            print(numero)
        except KeyboardInterrupt:
            respuesta = input("\n¿Desea detener el programa? (s/n): ").strip().lower()
            if respuesta == "s":
                print("Programa detenido por el usuario.")
                break
            else:
                print("Continuando la ejecución...")

if __name__ == "__main__":
    main()
