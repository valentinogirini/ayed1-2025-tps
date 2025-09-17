"""Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha,
considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo. """

import random
from typing import List, Tuple

def generar_pesos(n: int) -> List[int]:
    """
    Genera pesos aleatorios de naranjas entre 150 y 350 gramos.

    Precondiciones: n es un entero > 0.
    
    Postcondiciones: Devuelve una lista de n enteros correspondientes al peso de cada naranja.
    """
    return [random.randint(150, 350) for _ in range(n)]

def separar_aptas_y_jugo(pesos: List[int]) -> Tuple[List[int], int]:
    """
    Separa las naranjas aptas (200-300 g) y cuenta las destinadas a jugo.

    Precondiciones: pesos es una lista de enteros.
    
    Postcondiciones: Devuelve una lista de pesos aptos y un entero con la cantidad para jugo.
    """
    aptas = [p for p in pesos if p >= 200 and p <= 300]
    jugo = len([p for p in pesos if p < 200 or p > 300])
    return aptas, jugo

def formar_cajones(aptas: List[int]) -> Tuple[List[int], int]:
    """
    Forma cajones de 100 naranjas y calcula sobrantes.

    Precondiciones: aptas es una lista de enteros.
    
    Postcondiciones: Devuelve una lista con pesos totales de cada cajón y el número de naranjas sobrantes.
    """
    total_cajones = [sum(aptas[i*100:(i+1)*100]) for i in range(len(aptas)//100)]
    sobrantes = len(aptas) % 100
    return total_cajones, sobrantes

def calcular_camiones(cajones: List[int]) -> int:
    """
    Calcula la cantidad de camiones necesarios considerando ocupación mínima del 80%.

    Precondiciones: cajones es una lista de enteros (peso en gramos).
    
    Postcondiciones: Devuelve un entero con la cantidad de camiones despachables.
    """
    capacidad_max = 500_000
    ocupacion_min = 400_000
    camiones = 0
    peso_actual = 0

    for peso in cajones:
        if peso_actual + peso <= capacidad_max:
            peso_actual += peso
        else:
            if peso_actual >= ocupacion_min:
                camiones += 1
            peso_actual = peso
    if peso_actual >= ocupacion_min:
        camiones += 1
    return camiones

def main() -> None:
    while True:
        naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
        if naranjas > 0:
            break
        print("Debe ingresar un número positivo de naranjas.")

    pesos = generar_pesos(naranjas)
    aptas, jugo = separar_aptas_y_jugo(pesos)
    cajones, sobrantes = formar_cajones(aptas)
    camiones = calcular_camiones(cajones)

    print(f"\nNaranjas para jugo: {jugo}")
    print(f"Cajones llenos: {len(cajones)}")
    print(f"Naranjas sobrantes: {sobrantes}")
    print(f"Camiones despachables: {camiones}")

if __name__ == "__main__":
    main()
