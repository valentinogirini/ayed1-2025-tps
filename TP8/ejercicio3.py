"""Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía."""

def separar_email(email: str) -> tuple[str, ...]:
    """
    Separa una dirección de correo electrónico en sus componentes.

    Precondición: email es una cadena de caracteres.

    Postcondición:
    - retorna una tupla con las partes del correo (usuario, dominio, subdominio, etc.)
    - retorna tupla vacía si el correo no tiene el formato correcto.
    """

    partes = email.strip().split("@")
    if len(partes) != 2:
        return ()
        
    usuario, resto = partes
    if not usuario:
        return ()
    for c in usuario:
        if not c.isalnum():
            return ()
        
    dominio_partes = resto.split(".")
    if len(dominio_partes) < 2:
        return ()
        
    for parte in dominio_partes:
        if parte == "" or parte.isdigit() or not parte.isalnum():
            return ()
        
    return (usuario, *dominio_partes)


def main() -> None:
    """
    Función principal del programa.

    Precondición: ninguna.

    Postcondición:
    - imprime cada parte del correo si es válido.
    - imprime un mensaje de error si el correo no es válido.
    """

    email = input("Ingrese un correo electrónico: ").strip()
    partes = separar_email(email)

    if partes:
        print("--- Partes del correo ---")
        for i, parte in enumerate(partes, start=1):
            print(f"Parte {i}: {parte}")
    else:
        print("Error: el correo electrónico ingresado no tiene un formato válido.")

if __name__ == "__main__":
    main()