from datetime import datetime

from interface.cli import addition_functions, subtraction_functions, multiplication_functions, division_functions, challenge_functions


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
                print("\n== ADDITION ==\n")
                addition_functions()


            elif option == 2:
                print("\n== Subtraction ==\n")
                subtraction_functions()

            elif option == 3:
                print("\n== Multiplication ==\n")
                multiplication_functions()

            elif option == 4:
                print("\n== Division ==\n")
                division_functions()

            elif option == 5:
                print("\n== Challenge ==\n")
                challenge_functions()

            elif option == 6:
                print("\n[SYSTEM]   Exiting!...")
                break

            else:
                print("\n[SYSTEM]   Invalid Option!. Select Valid Option!..")

        except ValueError as e:
            print(f"\n[SYSTEM]  Encountered Input Error: {e}")