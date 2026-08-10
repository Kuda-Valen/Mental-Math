""" User input, Main Menu, & Time formatting """
from config import challenge
from engine.generator import random_numbers
from engine.evaluator import Addition, Subtraction
from datetime import datetime

def get_time(start_time):
    end_time = datetime.now()
    duration = end_time - start_time
    total_seconds = int(duration.total_seconds())

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{minutes:02d}:{seconds:02d}"

def addition_functions():
    corrects = 0
    i = 0
    user_input = challenge()
    start_time = datetime.now()
    while i < 10:
        numbers = random_numbers(user_input)
        a = numbers[0]
        b = numbers[1]
        c = numbers[2]
        d = numbers[3]
        e = numbers[4]

        if user_input == 1:
            print(f"\n{a} + {b}")

        elif user_input == 2:
            print(f"\n{a} + {b} + {c}")

        elif user_input == 3:
            print(f"\n{a} + {b} + {c} + {d}")

        elif user_input == 4:
            print(f"\n{a} + {b} + {c} + {d} + {e}")

        user_ans = int(input("Answer: "))
        addition = Addition(a, b, c, d, e)
        check = addition.check_answer(user_ans)
        if check == True:
            print("Correct!!")
            corrects += 1
        else:
            print("Incorrect!!")
        i += 1
    duration = get_time(start_time)
    print(f"\nYou got {corrects} correct out of 10..")
    print(f"Time: {duration}")

def subtraction_functions():
    corrects = 0
    i = 0
    user_input = challenge()
    start_time = datetime.now()
    while i < 10:
        numbers = random_numbers(user_input)
        a = numbers[0]
        b = numbers[1]
        subtraction = Subtraction(a, b)
        difference = subtraction.return_answer()

        print(f"\n{difference} - {a}")

        user_ans = int(input("Answer: "))
        check = subtraction.check_ans(user_ans)
        if check == True:
            print("Correct!!")
            corrects += 1
        else:
            print("Incorrect!!")
        i += 1
    duration = get_time(start_time)
    print(f"\nYou got {corrects} correct out of 10.")
    print(f"Time: {duration}")