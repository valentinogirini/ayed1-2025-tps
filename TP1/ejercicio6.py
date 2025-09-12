"""Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567.
No se permite utilizar facilidades de Python no vistas en clase.
"""

def pedir_positivo(mensaje: str) -> int:
    """
    Solicita al usuario un número entero positivo y lo devuelve.
    
    Precondiciones: El usuario debe ingresar un entero mayor o igual a 1.
    
    Postcondiciones: Devuelve un entero positivo.
    """
    while True:
        num = int(input(mensaje))
        if num >= 1:
            break
        print("Error. El número debe ser positivo.")
    return num

def concatenar_num(num1: int, num2: int) -> int:
    """
    Devuelve la concatenación de dos enteros positivos.
    
    Precondiciones: num1 y num2 deben ser enteros positivos.
    
    Postcondiciones: Retorna un entero formado por num1 seguido de num2.
    """
    return int(str(num1) + str(num2))

def main() -> None:
    """
    Solicita dos números positivos, los concatena y muestra el resultado.
    
    Precondiciones: El usuario debe ingresar dos enteros positivos.
    
    Postcondiciones: Muestra por pantalla el número concatenado.
    """
    num1 = pedir_positivo("Ingrese el primer número: ")
    num2 = pedir_positivo("Ingrese el segundo número: ")
    resultado = concatenar_num(num1, num2)
    print(f"El número concatenado es: {resultado}")

main()

