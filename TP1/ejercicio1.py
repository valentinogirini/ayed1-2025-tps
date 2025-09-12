"""Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
"""

def pedir_numero(mensaje: str) -> int:
    """
    Solicita al usuario que ingrese un número entero positivo y lo devuelve.
    
    Precondiciones: El usuario debe ingresar un entero mayor o igual a 1.
    
    Postcondiciones: Devuelve un entero positivo.
    """
    while True:
        num = int(input(mensaje))
        if num < 1:
            print("Error. El número debe ser positivo.")
        else:
            return num

def mayor_estricto(num1: int, num2: int, num3: int) -> int:
    """
    Determina el mayor estricto entre tres enteros positivos.
    
    Precondiciones: num1, num2 y num3 deben ser enteros positivos.
    
    Postcondiciones:
    .Retorna el mayor si es único.
    .Devuelve -1 si hay empate.
    """
    mayor = max(num1, num2, num3)
    apariciones = (num1 == mayor) + (num2 == mayor) + (num3 == mayor)
    if apariciones == 1:
        return mayor
    else:
        return -1

def main() -> None:
    """
    Solicita tres números positivos, obtiene el mayor estricto y lo muestra.
    
    Precondiciones: El usuario debe ingresar tres enteros positivos.
    
    Postcondiciones: Muestra por pantalla el mayor estricto o un mensaje si no existe.
    """
    num1 = pedir_numero("Ingrese el primer número: ")
    num2 = pedir_numero("Ingrese el segundo número: ")
    num3 = pedir_numero("Ingrese el tercer número: ")
    
    resultado = mayor_estricto(num1, num2, num3)
    if resultado == -1:
        print("No hay un máximo estricto")
    else:
        print(f"El máximo estricto es {resultado}")
    
main() 