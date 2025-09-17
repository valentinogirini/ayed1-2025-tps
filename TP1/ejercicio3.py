"""Una persona desea llevar el control de los gastos realizados al viajar en el
subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un
esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita
desarrollar una función que reciba como parámetro la cantidad de viajes realizados
en un determinado mes y devuelva el total gastado en viajes.
Realizar también un programa para verificar el comportamiento de la función.
Cantidad de viajes Valor del pasaje
1 a 20 Averiguar en Internet el valor actualizado
21 a 30 20% de descuento sobre tarifa máxima
31 a 40 30% de descuento sobre tarifa máxima
Más de 40 40% de descuento sobre tarifa máxima"""

def calcular_gasto_subte(viajes: int, tarifa_max: int) -> int | float:
    """
    Calcula el total gastado en subte según la cantidad de viajes y tarifa máxima.

    Precondiciones: viajes es un entero >= 0, tarifa_max es un entero positivo.
    
    Postcondiciones: Devuelve el total gastado como int o float.
    """
    if viajes <= 20:
        total = viajes * tarifa_max
    elif viajes <= 30:
        total = 20 * tarifa_max + (viajes - 20) * tarifa_max * 0.8
    elif viajes <= 40:
        total = 20 * tarifa_max + 10 * tarifa_max * 0.8 + (viajes - 30) * tarifa_max * 0.7
    else:
        total = 20 * tarifa_max + 10 * tarifa_max * 0.8 + 10 * tarifa_max * 0.7 + (viajes - 40) * tarifa_max * 0.6
    return total

def main() -> None:
    while True:
        tarifa_max = int(input("Ingrese el valor de la tarifa máxima: "))
        if tarifa_max > 0:
            break
        print("La tarifa debe ser un número positivo.")

    while True:
        viajes = int(input("Ingrese la cantidad de viajes realizados: "))
        if viajes >= 0:
            break
        print("La cantidad de viajes no puede ser negativa.")
    
    
    total = calcular_gasto_subte(viajes, tarifa_max)
    print(f"Total gastado en subte: ${round(total, 2)}")

if __name__ == "__main__":
    main()
