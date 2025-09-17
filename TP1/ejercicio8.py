"""La siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.
def diadelasemana(dia,mes,año):
 if mes < 3:
     mes = mes + 10
     año = año – 1
 else:
     mes = mes – 2
 siglo = año // 100
 año2 = año % 100
 diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
 if diasem < 0:
     diasem = diasem + 7
 return diasem
"""

def diadelasemana(dia: int, mes: int, anio: int) -> int:
    """
    Calcula el día de la semana para una fecha determinada.
    
    Precondiciones: dia, mes y año son enteros válidos de una fecha existente.
    
    Postcondiciones: Devuelve un entero 0-6 donde 0=domingo, 1=lunes, ..., 6=sábado.
    """
    if mes < 3:
        mes += 10
        anio -= 1
    else:
        mes -= 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10) + dia + anio2 + (anio2//4) + (siglo//4) - (2*siglo)) % 7
    if diasem < 0:
        diasem += 7
    return diasem

def dias_en_mes(mes: int, anio: int) -> int:
    """
    Devuelve la cantidad de días de un mes considerando años bisiestos.
    
    Precondiciones: mes y año son enteros válidos.
    
    Postcondiciones: Devuelve un entero con la cantidad de días del mes.
    """
    if mes == 2:
        return 29 if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) else 28
    if mes in [1,3,5,7,8,10,12]:
        return 31
    return 30

def imprimir_calendario(mes: int, anio: int) -> None:
    """
    Imprime por pantalla el calendario de un mes y año dados.
    
    Precondiciones: mes entre 1 y 12, año entre 1 y 9.999.
    
    Postcondiciones: Muestra por pantalla el calendario con la semana comenzando en domingo.
    """
    dias_mes = dias_en_mes(mes, anio)
    print(f"\nCalendario {mes}/{anio}")
    print("Do Lu Ma Mi Ju Vi Sa")
    
    primer_dia_sem = diadelasemana(1, mes, anio)
    for _ in range(primer_dia_sem):
        print("   ", end="")

    for dia in range(1, dias_mes + 1):
        print(f"{dia:2d} ", end="")
        if (primer_dia_sem + dia) % 7 == 0:
            print()
    print()

def main() -> None:
    while True:
        mes = int(input("Ingrese el mes (1-12): "))
        if mes >= 1 and mes <= 12:
            break
        print("El número del mes debe estar entre 1 y 12.")
        
    while True:
        anio = int(input("Ingrese el año (1-9999): "))
        if anio >= 1 and anio <= 9999:
            break
        print("El año debe ser un número entre 1 y 9999.")
        
    imprimir_calendario(mes, anio)

if __name__ == "__main__":
    main()

