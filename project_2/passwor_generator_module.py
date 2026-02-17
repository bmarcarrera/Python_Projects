"""
Consiste en hacer un programa que genere contraseñas
seguras de manera aleatoria.

El objetivo es ayudar al usuario a crear contraseñas fuertes
que sean difíciles de adivinar por hackers o programas maliciosos.

El programa permite al usuario personalizar la longitud de la contraseña,
así como elegir qué caracteres incluir, como letras mayúsculas y minúsculas,
números y caracteres especiales.

Una vez que se han establecido las preferencias del usuario,
el programa genera una contraseña aleatoria
que cumple con los criterios especificados.
"""

from random import shuffle

password = "sdf234(9·)"
lista_contraseña = list(contraseña)
shuffle(lista_contraseña)

clave_encriptacion = "".join(lista_contraseña)
print(clave_encriptacion)


def contraseña_usuario():
    password = input(
        """
    Escribe tu contraseña. Incluye al menos los siguientes puntos:
        - Mínimo 8 caracteres
         - Una letra mayúscula.              
         - Una letra minúscula.
         - Un número.
         - Un caracter especial.              
    """
    )
    password_list = list(password)
    shuffle(password_list)
    password_encriptada = "".join(password_list)
