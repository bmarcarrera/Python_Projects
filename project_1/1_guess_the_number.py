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

import guess_the_number_modules

guess_number = guess_the_number_modules.guess_number_game()
print(guess_number)
1