import random


def verify_number(message):
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            else:
                print(f"{number} is less than 0. Introduce positive number.")
        except ValueError as ve:
            print(f"{ve}: The value {number} is not correct. Try again.")


def number_comparison(secret_number, user_number):
    if secret_number < user_number:
        return "You number is too high, choose a lower one."
    elif secret_number > user_number:
        return "You number is too low, choose a higher one."


def guess_number_game(number_of_tries=1):
    i_range = verify_number("Introduce the minimum number of the range: ")
    f_range = verify_number("Introduce the maximum number of the range: ")
    random_number = random.randint(i_range, f_range)
    while True:
        choosen_number = verify_number(
            f"Guess the number between {i_range} and {f_range}: "
        )
        if choosen_number < i_range or choosen_number > f_range:
            print(
                f"El valor {choosen_number} no está dentro del rango permitido. Inténtalo de nuevo."
            )
            continue
        elif choosen_number != random_number:
            print(f"{number_comparison(random_number, choosen_number)}")
        else:
            return f"Congrats! You've made in {number_of_tries}. The random number is {random_number}."

        number_of_tries += 1
