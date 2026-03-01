import random
import string


def condiciones_contraseña(mensaje_usuario):
    minusculas = string.ascii_lowercase not in mensaje_usuario
    mayusculas = string.ascii_uppercase not in mensaje_usuario
    numeros = string.digits not in mensaje_usuario
    simbolos = string.punctuation not in mensaje_usuario
    espacios = string.whitespace not in mensaje_usuario

    condiciones = {
        minusculas: "La contraseña ha de tener al menos una minúscula.",
        mayusculas: "La contraseña ha de tener al menos una mayúscula.",
        numeros: "La contraseña ha de tener al menos un número.",
        simbolos: "La contraseña ha de tener al menos un caracter especial.",
        espacios: "La contraseña no puede tener espacios.",
    }
    return condiciones


def password_parameters(mensaje):
    input_usuario = input(mensaje)
    condiciones = condiciones_contraseña(input_usuario)
    while len(input_usuario) < 8:
        print("Introduce mínimo 8 caracteres.")
        input_usuario = input(mensaje)

    while True:
        if not (all(condiciones)):
            print("Caracteres introducidos correctamente")
            break
        for condicion in condiciones:
            if condicion:
                print(condiciones[condicion])
        input_usuario = input("Introduce de nuevo caracteres válidos: ")


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
