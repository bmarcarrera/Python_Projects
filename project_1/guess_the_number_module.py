import random


def verify_number(message):
    """Verifies that the input is a valid number."""
    while True:
        user_input = input(message)
        try:
            number = int(user_input)
            if number >= 0:
                return number
            else:
                print(
                    f"{number} is less than 0. Please, enter a natural number."
                )
        except ValueError:
            print(f'The value "{user_input}" is not correct. Try again.')


def is_valid_range(initial_range, final_range):
    """Verifies the correct format of the range established."""
    return final_range > (initial_range + 1)


def number_comparison(secret_number, user_number):
    """Compares the random and user numbers to check the result."""
    if (secret_number + 10) < user_number:
        return "too high"
    elif secret_number < user_number:
        return "high"
    elif secret_number > (user_number + 10):
        return "too low"
    elif secret_number > user_number:
        return "low"
    else:
        return "correct"


def guess_number_game():
    """Main function that contains the messages and loops to keep the game
    running correctly e efficiently."""
    print("Welcome to the Guess The Number game!")
    i_num = verify_number(
        "Please, introduce the minimum number of the range: "
    )
    f_num = verify_number(
        f"Now, enter the maximum number of the range. It must be 2 unit higher than {i_num}: "
    )

    while not is_valid_range(i_num, f_num):
        f_num = verify_number(
            f"The maximum limit must be at least 2 units higher than {i_num}: "
        )

    random_number = random.randint(i_num, f_num)

    number_of_tries = 1
    while True:
        chosen_number = verify_number(
            f"Guess the number between {i_num} and {f_num}: "
        )
        result = number_comparison(random_number, chosen_number)
        if chosen_number not in range(i_num, f_num + 1):
            print(f"The {chosen_number} is not inside the range. Try again.")
        elif result in ["high", "low", "too hight", "too low"]:
            print(f"Your guess is {result}. Try again.")
        else:
            return f"Congrats! You are correct! You made it in {number_of_tries} tries. The random number was {random_number}."

        number_of_tries += 1
