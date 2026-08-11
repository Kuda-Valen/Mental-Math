from datetime import datetime

from interface.cli import operation


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
                operation("addition")


            elif option == 2:
                print("\n== Subtraction ==\n")
                operation("subtraction")

            elif option == 3:
                print("\n== Multiplication ==\n")
                operation("multiplication")

            elif option == 4:
                print("\n== Division ==\n")
                operation("division")

            elif option == 5:
                print("\n== Challenge ==\n")
                operation("challenge")

            elif option == 6:
                print("\n[SYSTEM]   Exiting!...")
                break

            else:
                print("\n[SYSTEM]   Invalid Option!. Select Valid Option!..")

        except ValueError as e:
            print(f"\n[SYSTEM]  Encountered Input Error: {e}")