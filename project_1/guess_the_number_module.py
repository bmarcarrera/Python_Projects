import random


def verify_number(message):
    while True:
        user_input = input(message)
        try:
            number = int(user_input)
            if number >= 0:
                return number
            else:
                print(f"{number} is less than 0. Introduce a natural number.")
        except ValueError:
            print(f'The value "{user_input}" is not correct. Try again.')


def number_comparison(secret_number, user_number):
    if secret_number < user_number:
        return "You number is too high, choose a lower one."
    elif secret_number > user_number:
        return "You number is too low, choose a higher one."


def guess_number_game(number_of_tries=1):
    print("Welcome to the Guess The Number game!")
    i_range = verify_number("Plase, introduce the minimum number of the range: ")
    f_range = verify_number(
        f"Now, introduce the maximum number of the range. Must be 2 unit superior to {i_range}: "
    )

    while not f_range > i_range + 1:
        print(
            "The final limit can't be less or equal and can't be less in 1 unit than the initial limit."
        )
        f_range = verify_number("Introduce a valid value: ")

    random_number = random.randint(i_range, f_range)

    while True:
        choosen_number = verify_number(
            f"Guess the number between {i_range} and {f_range}: "
        )
        if choosen_number < i_range or choosen_number > f_range:
            print(
                f"The value {choosen_number} is not in the permitted range. Try again."
            )
        elif choosen_number != random_number:
            print(f"{number_comparison(random_number, choosen_number)}")
        else:
            return f"Congrats! You've made in {number_of_tries}. The random number is {random_number}."

        number_of_tries += 1

    
