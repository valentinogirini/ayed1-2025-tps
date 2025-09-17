"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10."""

from typing import List, Tuple

def calcular_vuelto(total: int, recibido: int) -> Tuple[List[int], List[int]] | None:
    """
    Calcula el cambio que debe entregarse al cliente minimizando la cantidad de billetes.

    Precondiciones: total y recibido son enteros positivos.

    Postcondiciones: Devuelve dos listas; denominaciones y cantidad de billetes de cada denominación,
                     o None si el dinero es insuficiente o el cambio no puede darse.
    """
    if recibido < total:
        return None

    vuelto = recibido - total
    if vuelto == 0:
        return [],[]

    denominaciones = [5000, 1000, 500, 200, 100, 50, 10]
    cantidades = []

    for billete in denominaciones:
        if vuelto >= billete:
            cantidad = vuelto // billete
            vuelto -= cantidad * billete
            cantidades.append(cantidad)
        else:
            cantidades.append(0)

    if vuelto != 0:
        return None

    return denominaciones, cantidades

def main() -> None:
    while True:
        total = int(input("Ingrese el total de la compra: "))
        if total > 0:
            break
        print("El total debe ser un número positivo.")
    
    while True:
        recibido = int(input("Ingrese el dinero recibido: "))
        if recibido > 0:
            break
        print("El dinero recibido debe ser un número positivo.")

    resultado = calcular_vuelto(total, recibido)

    if resultado is None:
        print("Error: Dinero insuficiente o no se puede entregar el cambio exacto.")
    else:
        denominaciones, cantidades = resultado
        if not denominaciones:
            print("No hay cambio que entregar.")
        else:
            print("Vuelto a entregar:")
            for billete, cantidad in zip(denominaciones, cantidades):
                if cantidad > 0:
                    print(f"{cantidad} billete(s) de ${billete}")

if __name__ == "__main__":
    main()

