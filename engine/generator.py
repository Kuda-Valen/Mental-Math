""" Random Number Sequence generation """

import random

def random_number():
    print("1. Begginer")
    print("2. Intermediate")
    print("3. Advanced")
    print("4. Genius")

    try:
        user_input = int(input("\nChoose your Challenge: "))
    except ValueError as e:
        print(f"\n[SYSTEM]   Encountered Input Error ->: {e}")

    if user_input == 1:
        random_a = random.randint(1, 12)
        random_b = random.randint(1, 12)
        random_c = 0
        random_d = 0
        random_e = 0

    elif user_input == 2:
        random_a = random.randint(1, 12)
        random_b = random.randint(1, 12)
        random_c = random.randint(1, 12)
        random_d = 0
        random_e = 0

    elif user_input == 3:
        random_a = random.randint(1, 12)
        random_b = random.randint(1, 12)
        random_c = random.randint(1, 12)
        random_d = random.randint(1, 12)
        random_e = 0

    elif user_input == 4:
        random_a = random.randint(1, 12)
        random_b = random.randint(1, 12)
        random_c = random.randint(1, 12)
        random_d = random.randint(1, 12)
        random_e = random.randint(1, 12)

    return [random_a, random_b, random_c, random_d, random_e]