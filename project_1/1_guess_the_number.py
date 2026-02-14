"""
 # Consisten en pedirle al usuario que adivine
un número elegido aleatoriamente por el programa.

 # El objetivo es que el usuario (quien dara el input) adivine correctamente el número
(elegido aleatoriamente por el programa) en la menor cantidad de intentos posible.

 # El programa establece un rango de números posibles y
elige aleatoriamente un número dentro de ese rango.

 # Luego, el programa le pide al usuario que adivine el número
y le da una pista sobre si el número a adivinar es mayor o menor que el número
que el usuario ha ingresado. De esta manera, el usuario puede ajustar sus conjeturas para acercarse al número correcto.

 # El juego continúa hasta que el usuario adivine el número correcto,
momento en el que el programa le da una felicitación y le muestra
el número de intentos que le tomó adivinar el número.
"""

import random

print("Bienvenido al juego de adivinar el número.")
num_i = int(input("Elige el número inicial del rango: "))
num_f = int(input("Elige el número final del rango: "))
numero_elegido = int(
    input(f"Elige un número final dentro del rango ({num_i}, {num_f}): ")
)
numero_aleatorio = random.randint(num_i, num_f)
numero_intentos = 0
while numero_aleatorio != numero_elegido:
    if numero_elegido < numero_aleatorio:
        print("Tu número es más pequeño.")
        numero_elegido = int(input(f"Elige otro más grande: "))
    elif numero_elegido > numero_aleatorio:
        print("Tu número es más grande.")
        numero_elegido = int(input("Elige otro número más pequeño: "))
    numero_intentos += 1
print(f"¡¡Felicidades!! Lo has hecho has conseguido en {numero_intentos} intentos.")
print(f"El número aleatorio era el {numero_aleatorio}")


