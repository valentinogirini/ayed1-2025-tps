"""Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?"""

def entero_a_romano(num: int) -> str:
    """
    Convierte un número entero (0-3999) a número romano.
    
    Precondición: num es un entero entre 0 y 3999.
    
    Postcondición: retorna la representación en números romanos como cadena.
    """
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""
    for i in range(len(valores)):
        while num >= valores[i]:
            resultado += simbolos[i]
            num -= valores[i]
    return resultado


def main() -> None:
    """
    Permite ingresar un número entre 0 y 3999 y mostrar su representación romana.
    
    Precondición: ninguna.
    
    Postcondición: imprime el número en su forma romana o un mensaje de error si es inválido.
    """
    try:
        numero = int(input("Ingrese un número entre 0 y 3999: "))
        if numero >= 0 and numero <= 3999:
            print(entero_a_romano(numero))
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")


if __name__ == "__main__":
    main()

