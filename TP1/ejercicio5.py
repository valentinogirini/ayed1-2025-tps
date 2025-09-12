"""5. Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo
porque resulta de multiplicar 2 * 3.
b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1.
Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False.
No se permite utilizar ayudas externas a las mismas."""

def main():
    """
    Solicita un número entero positivo al usuario e informa si es oblongo y si es triangular.
    
    Precondiciones: El usuario ingresa un número entero positivo.
    
    Postcondiciones: Muestra por pantalla si el número es oblongo y si es triangular.
    """
    es_oblongo = lambda num: ((-1 + (1 + 4 * num) ** 0.5) / 2) == ((-1 + (1 + 4 * num) ** 0.5) // 2)

    es_triangular = lambda num: ((-1 + (1 + 8 * num) ** 0.5) / 2) == ((-1 + (1 + 8 * num) ** 0.5) // 2)
    
    while True:
        num = int(input("Ingrese un número: "))
        if num > 0:
            break
        print("Error. El número debe ser entero positivo")
        
    if es_oblongo(num):
        print(f"{num} es oblongo!")
    else:
        print(f"{num} no es oblongo.")
        
    if es_triangular(num):
        print(f"{num} es triangular!")
    else:
        print(f"{num} no es triangular")

main()