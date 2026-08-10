""" User input, Main Menu, & Time formatting """
from config import challenge
from engine.generator import random_numbers, random_challenge, decode_challenge
from engine.evaluator import Addition, Subtraction, Multiplication, Division
from datetime import datetime

def get_user_answer():
    user_ans = input("Answer: ").strip()

    if user_ans == "":
        user_ans = 0

    return int(user_ans)

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
   
        print(f"\n{a} + {b}")

        user_ans = get_user_answer()

        addition = Addition(a, b)
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

        user_ans = get_user_answer()

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

def multiplication_functions():
    corrects = 0
    i = 0
    user_input = challenge()
    start_time = datetime.now()
    while i < 10:
        numbers = random_numbers(user_input)
        a = numbers[0]
        b = numbers[1]
        print(f"\n{a} x {b}")

        user_ans = get_user_answer()

        multiplication = Multiplication(a, b)
        check = multiplication.check_ans(user_ans)
        if check == True:
            print("Correct!!")
            corrects += 1
        else:
            print("Incorrect!!")
        i += 1

    duration = get_time(start_time)
    print(f"\nYou got {corrects} correct out of 10.")
    print(f"Time: {duration}")

def division_functions():
    corrects = 0
    i = 0
    user_input = challenge()
    start_time = datetime.now()
    while i < 10:
        numbers = random_numbers(user_input)
        a = numbers[0]
        b = numbers[1]

        division = Division(a, b)
        divident = division.return_divident()

        print(f"\n{divident} / {a}")
        user_ans = get_user_answer()
        check = division.check_ans(user_ans)

        if check == True:
            corrects += 1
            print("Correct!!")
        else:
            print("Incorrect!!")
        i += 1

    duration = get_time(start_time)
    print(f"\nYou got {corrects} correct out of 10")
    print(f"Time: {duration}")

def challenge_functions():
    operators = random_challenge()
    corrects = 0
    i = 0
    user_input = challenge()
    start_time = datetime.now()
    while i < 10:
        numbers = random_numbers(user_input)
        a = numbers[0]
        b = numbers[1]
    
        operation = decode_challenge(i, operators)

        if operation == "addition":
            print(f"\n{a} + {b}")
            user_ans = get_user_answer()
            addition = Addition(a, b)
            check = addition.check_answer(user_ans)

            if check == True:
                print("Correct!!")
                corrects += 1
            else:
                print("Incorrect!!")

        elif operation == "subtraction":
            subtraction = Subtraction(a, b)
            difference = subtraction.return_answer()

            print(f"\n{difference} - {a}")
            user_ans = get_user_answer()

            check = subtraction.check_ans(user_ans)

            if check == True:
                print("Correct!!")
                corrects += 1
            else:
                print("Incorrect!!")

        elif operation == "multiplication":
            print(f"\n{a} x {b}")
            user_ans = get_user_answer()

            multiplication = Multiplication(a, b)
            check = multiplication.check_ans(user_ans)

            if check == True:
                print("Correct!!")
                corrects += 1
            else:
                print("Incorrect!!")

        else:
            division = Division(a, b)
            divident = division.return_divident()

            print(f"\n{divident} / {a}")
            user_ans = get_user_answer()
            check = division.check_ans(user_ans)

            if check == True:
                corrects += 1
                print("Correct!!")
            else:
                print("Incorrect!!")

        i += 1

    duration = get_time(start_time)
    print(f"\nYou got {corrects} correct out of 10.")
    print(f"Time: {duration}")
