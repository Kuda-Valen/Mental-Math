""" Random Number Sequence generation """

import random

def random_numbers(user_input):
    if user_input == 1:
        random_a = random.randint(1, 12)
        random_b = random.randint(1, 12)
        return [random_a, random_b]

    elif user_input == 2:
        random_a = random.randint(13, 50)
        random_b = random.randint(13, 50)
        return [random_a, random_b]

    elif user_input == 3:
        random_a = random.randint(51, 120)
        random_b = random.randint(51, 120)
        return [random_a, random_b]

    elif user_input == 4:
        random_a = random.randint(121, 500)
        random_b = random.randint(121, 500)
        return [random_a, random_b]

    else:
        print("Invalid option!!")

def random_challenge():
    operations = []
    i = 0

    while i < 10:
        num = random.randint(1, 4)
        operations.append(num)
        i += 1

    return operations

def decode_challenge(i, operators):
    if operators[i] == 1:
        return "addition"

    elif operators[i] == 2:
        return "subtraction"

    elif operators[i] == 3:
        return "multiplication"

    elif operators[i] == 4:
        return "division"