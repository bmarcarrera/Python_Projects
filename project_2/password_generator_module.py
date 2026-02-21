import random
import string


def password_parameters(mensaje):

    while True:
            input_usuario = input(mensaje)
            if len(input_usuario) < 8:
                print("mínimo 8 caracteres.")
                continue
            if len(input_usuario) >= 8:
                for caracter in input_usuario:
                    for espacios in string.whitespace:
                    print(
                        "La contraseña no puede contener espacios o saltos de línea."
                    )
                elif string.ascii_lowercase not in input_usuario:
                    print("La contraseña ha de tener al menos una minúscula.")
                elif string.ascii_uppercase not in input_usuario:
                    print("La contraseña ha de tener al menos una mayúscula.")
                elif string.digits not in input_usuario:
                    print("La contraseña ha de tener al menos un número.")
                elif string.punctuation not in input_usuario:
                    print(
                        "La contraseña ha de tener al menos un caracter especial."
                    )
            else:
                print("Los caracteres introducidos son correctos.")
                break
            print(
                "El valor introducido no corresponde al tipo de valor necesario."
            )


def contraseña_usuario():
    print(
        """
Escribe tu contraseña. Incluye al menos los siguientes puntos:
- Mínimo 8 caracteres
    - Una letra mayúscula.              
    - Una letra minúscula.
    - Un número.
    - Un caracter especial.              
"""
    )
    caracteres = password_parameters("Introduce los caracteres: ")
    contraseña = "".join(random.shuffle(caracteres))
    return f"Tu contraseña es: {contraseña}"
