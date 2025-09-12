"""Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función."""

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si los valores día, mes y año corresponden a una fecha válida.
    
    Precondiciones: dia, mes y anio son enteros positivos.
    
    Postcondiciones: Devuelve True si la fecha es válida, False si no lo es.
    """
    if anio < 1 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
        return False
    
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        meses[1] = 29
        
    if dia > meses[mes - 1]:
        return False
    return True

def main() -> None:
    """
    Solicita día, mes y año al usuario y muestra si la fecha es válida.
    
    Precondiciones: El usuario ingresa números enteros positivos.
    
    Postcondiciones: Muestra por pantalla un mensaje indicando la validez de la fecha.
    """
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    
    if validar_fecha(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")
    

if __name__ == "__main__":
    main()