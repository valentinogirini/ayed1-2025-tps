"""Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera."""

from typing import Tuple

def es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.
    
    Precondiciones: anio mayor a 0.
    
    Postcondiciones: True si es bisiesto, False en caso contrario.
    """
    return (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0)


def dias_en_mes(mes: int, anio: int) -> int:
    """
    Devuelve la cantidad de días del mes dado.
    
    Precondiciones: mes entre 1 y 12, anio mayor a 0.
    
    Postcondiciones: retorna la cantidad de días del mes.
    """
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si la fecha es válida.
    
    Precondiciones: recibe día, mes y anio como enteros.
    
    Postcondiciones: True si la fecha existe, False en caso contrario.
    """
    if anio < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_en_mes(mes, anio):
        return False
    return True


def diasiguiente(dia: int, mes: int, anio: int) -> Tuple[int, int, int]:
    """
    Calcula el día siguiente a la fecha dada.
    
    Precondiciones: fecha válida.
    
    Postcondiciones: retorna una tupla con el nuevo día, mes y anio.
    """
    if dia < dias_en_mes(mes, anio):
        return dia + 1, mes, anio
    else:
        dia = 1
        if mes == 12:
            return dia, 1, anio + 1
        else:
            return dia, mes + 1, anio


def fecha_menor(d1: int, m1: int, a1: int, d2: int, m2: int, a2: int) -> bool:
    """
    Compara dos fechas.
    
    Precondiciones: ambas fechas válidas.
    
    Postcondiciones: True si la primera es menor o igual a la segunda.
    """
    if a1 < a2:
        return True
    elif a1 > a2:
        return False
    else:
        if m1 < m2:
            return True
        elif m1 > m2:
            return False
        else:
            return d1 <= d2


def sumar_dias(dia: int, mes: int, anio: int, n: int) -> Tuple[int, int, int]:
    """
    Suma n días a una fecha.
    
    Precondiciones: fecha válida y n >= 0.
    
    Postcondiciones: retorna la nueva fecha como tupla (día, mes, anio).
    """
    for i in range(n):
        dia, mes, anio = diasiguiente(dia, mes, anio)
    return dia, mes, anio


def dias_entre(d1: int, m1: int, a1: int, d2: int, m2: int, a2: int) -> int:
    """
    Calcula los días entre dos fechas.
    
    Precondiciones: ambas fechas válidas.
    
    Postcondiciones: retorna un entero con la diferencia en días.
    """
    dias = 0
    if not fecha_menor(d1, m1, a1, d2, m2, a2):
        d1, m1, a1, d2, m2, a2 = d2, m2, a2, d1, m1, a1

    while (d1, m1, a1) != (d2, m2, a2):
        d1, m1, a1 = diasiguiente(d1, m1, a1)
        dias += 1
    return dias


def main() -> None:
    """
    Programa principal.
    
    Precondiciones: no recibe parámetros.
    
    Postcondiciones: ejecuta un menú para operar con fechas.
    """
    print("1. Calcular el día siguiente")
    print("2. Sumar N días a una fecha")
    print("3. Calcular días entre dos fechas")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        if not fecha_valida(dia, mes, anio):
            print("Fecha inválida")
        else:
            nuevo_dia, nuevo_mes, nuevo_anio = diasiguiente(dia, mes, anio)
            print(f"El día siguiente es: {nuevo_dia}/{nuevo_mes}/{nuevo_anio}")

    elif opcion == 2:
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        if not fecha_valida(dia, mes, anio):
            print("Fecha inválida")
        else:
            n = int(input("Cantidad de días a sumar: "))
            nuevo_dia, nuevo_mes, nuevo_anio = sumar_dias(dia, mes, anio, n)
            print(f"La nueva fecha es: {nuevo_dia}/{nuevo_mes}/{nuevo_anio}")

    elif opcion == 3:
        print("Ingrese la primera fecha:")
        d1 = int(input("Día: "))
        m1 = int(input("Mes: "))
        a1 = int(input("Año: "))
        if not fecha_valida(d1, m1, a1):
            print("Primera fecha inválida")
        else:
            print("Ingrese la segunda fecha:")
            d2 = int(input("Día: "))
            m2 = int(input("Mes: "))
            a2 = int(input("Año: "))
            if not fecha_valida(d2, m2, a2):
                print("Segunda fecha inválida")
            else:
                total = dias_entre(d1, m1, a1, d2, m2, a2)
                print(f"La cantidad de días entre ambas fechas es: {total}")

    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()