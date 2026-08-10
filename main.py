from datetime import datetime

from interface.cli import addition_functions, subtraction_functions


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
                print("Calling Multiplication method")

            elif option == 4:
                print("Calling Division method")

            elif option == 5:
                print("Calling Challenge method")

            elif option == 6:
                print("\n[SYSTEM]   Exiting!...")
                break

            else:
                print("\n[SYSTEM]   Invalid Option!. Select Valid Option!..")

        except ValueError as e:
            print(f"\n[SYSTEM]  Encountered Input Error: {e}")