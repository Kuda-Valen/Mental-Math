""" Random Number Sequence generation """

import random


def random_numbers(user_input):
    if user_input == 1:
        random_a = random.randint(1, 12)
        random_b = random.randint(1, 12)
        random_c = 0
        random_d = 0
        random_e = 0

    elif user_input == 2:
        random_a = random.randint(13, 50)
        random_b = random.randint(13, 50)
        random_c = random.randint(13, 50)
        random_d = 0
        random_e = 0

    elif user_input == 3:
        random_a = random.randint(51, 120)
        random_b = random.randint(51, 120)
        random_c = random.randint(51, 120)
        random_d = random.randint(51, 120)
        random_e = 0

    elif user_input == 4:
        random_a = random.randint(121, 500)
        random_b = random.randint(121, 500)
        random_c = random.randint(121, 500)
        random_d = random.randint(121, 500)
        random_e = random.randint(121, 500)

    return [random_a, random_b, random_c, random_d, random_e]