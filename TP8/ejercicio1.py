"""Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios,
y luego escribir un programa que las vincule:

a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.

b. Sumar N días a una fecha.

c. Ingresar un horario desde teclado, verificando que sea correcto.

d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas."""


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


def fecha_valida(dia: int, mes: int, año: int) -> bool:
    """
    Verifica si una fecha es válida.

    Precondición: los tres valores son enteros positivos.
    
    Postcondición: retorna True si la fecha existe, False en caso contrario.
    """
    if año <= 0 or mes < 1 or mes > 12:
        return False
    return dia >= 1 and dia <= dias_en_mes(mes, año)


def ingresar_fecha() -> tuple[int, int, int]:
    """
    Solicita al usuario ingresar una fecha válida (día, mes, año).

    Precondición: ninguna.
    
    Postcondición: retorna una tupla (día, mes, año).
    """
    while True:
        try:
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes (1-12): "))
            año = int(input("Ingrese el año: "))
            if fecha_valida(dia, mes, año):
                return (dia, mes, año)
            else:
                print("Fecha inválida. Intente nuevamente.\n")
        except ValueError:
            print("Error: debe ingresar números enteros.\n")


def sumar_dias(fecha: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    """
    Suma N días a una fecha determinada.

    Precondición:
    - fecha es una tupla (día, mes, año) válida.
    - n es un entero (puede ser positivo o negativo).

    Postcondición: retorna una nueva tupla (día, mes, año) con la fecha resultante.
    """
    dia, mes, año = fecha
    dia += n

    while True:
        dias_mes = dias_en_mes(mes, año)
        if dia > dias_mes:
            dia -= dias_mes
            mes += 1
            if mes > 12:
                mes = 1
                año += 1
        elif dia < 1:
            mes -= 1
            if mes < 1:
                mes = 12
                año -= 1
            dia += dias_en_mes(mes, año)
        else:
            break

    return (dia, mes, año)


def horario_valido(h: int, m: int, s: int) -> bool:
    """
    Verifica si un horario (hora, minuto, segundo) es válido.

    Precondición: h, m, s son enteros.
    
    Postcondición: retorna True si el horario es correcto, False en caso contrario.
    """
    return (h >= 0 and h < 24) and (m >= 0 and m < 60) and (s >= 0 and s < 60)


def ingresar_horario() -> tuple[int, int, int]:
    """
    Solicita un horario válido (hora, minuto, segundo).

    Precondición: ninguna.
    
    Postcondición: retorna una tupla (h, m, s).
    """
    while True:
        try:
            h = int(input("Hora (0-23): "))
            m = int(input("Minutos (0-59): "))
            s = int(input("Segundos (0-59): "))
            if horario_valido(h, m, s):
                return (h, m, s)
            else:
                print("Horario inválido. Intente nuevamente.\n")
        except ValueError:
            print("Error: debe ingresar números enteros.\n")


def diferencia_horarios(h1: tuple[int, int, int], h2: tuple[int, int, int]) -> tuple[int, int, int]:
    """
    Calcula la diferencia entre dos horarios.

    Precondición: h1 y h2 son tuplas válidas (hora, minuto, segundo).
    
    Postcondición:
    - retorna una tupla con la diferencia.
    - si h1 > h2, se asume que h1 pertenece al día anterior (máx. 24 horas de diferencia).
    """
    seg1 = h1[0] * 3600 + h1[1] * 60 + h1[2]
    seg2 = h2[0] * 3600 + h2[1] * 60 + h2[2]

    if seg1 > seg2:
        seg2 += 24 * 3600 

    dif = seg2 - seg1

    horas = dif // 3600
    minutos = (dif % 3600) // 60
    segundos = dif % 60

    return (horas, minutos, segundos)


def main() -> None:
    """
    Función principal del programa.
    
    Precondición: ninguna.
    
    Postcondición: muestra un menú con opciones para manipular fechas y horarios.
    """
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar una fecha válida")
        print("2. Sumar N días a una fecha")
        print("3. Ingresar un horario válido")
        print("4. Calcular diferencia entre dos horarios")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            fecha = ingresar_fecha()
            print(f"Fecha ingresada correctamente: {fecha[0]:02d}/{fecha[1]:02d}/{fecha[2]}")
        elif opcion == "2":
            fecha = ingresar_fecha()
            try:
                n = int(input("Ingrese la cantidad de días a sumar (puede ser negativa): "))
                nueva = sumar_dias(fecha, n)
                print(f"Nueva fecha: {nueva[0]:02d}/{nueva[1]:02d}/{nueva[2]}")
            except ValueError:
                print("Error: debe ingresar un número entero.")
        elif opcion == "3":
            horario = ingresar_horario()
            print(f"Horario ingresado correctamente: {horario[0]:02d}:{horario[1]:02d}:{horario[2]:02d}")
        elif opcion == "4":
            print("Ingrese el primer horario:")
            h1 = ingresar_horario()
            print("Ingrese el segundo horario:")
            h2 = ingresar_horario()
            dif = diferencia_horarios(h1, h2)
            print(f"Diferencia: {dif[0]:02d}h {dif[1]:02d}m {dif[2]:02d}s")
        elif opcion == "5":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
