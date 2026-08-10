from datetime import datetime

from engine.evaluator import Addition
from engine.generator import random_numbers
from config import challenge


if __name__ == "__main__":

    while True:
        print("\n === MENTAL MATH ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Challenge")
        print("6. Exit")

        try:
            option = int(input("\nChoose an Option: "))

            if option == 1:
                corrects = 0
                i = 0

                print("\n== ADDITION ==\n")
                user_input = challenge()
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

                print(f"\nYou Got {corrects} correct out of 10!")
                

            elif option == 2:
                print("Calling Subtraction method")

            elif option == 3:
                print("Calling Multiplication method")

            elif option == 4:
                print("Calling Division method")

            elif option == 5:
                print("Calling Challenge method")

            elif option == 6:
                print("\n[SYSTEM]   Exiting!...")

            else:
                print("\n[SYSTEM]   Invalid Option!. Select Valid Option!..")

        except ValueError as e:
            print(f"\n[SYSTEM]  Encountered Input Error: {e}")