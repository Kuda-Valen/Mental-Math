from interface.cli import operation

def menu():
    while True:
        print("\n-- Mental Math --\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Challenge")
        print("6. Back to Menu")

        try:
            option = int(input("\nChoose an Option: "))

            if option == 1:
                print("\n-- Addition --\n")
                operation("addition")

            elif option == 2:
                print("\n--Subtraction\n")
                operation("subtraction")

            elif option == 3:
                print("\n-- Multiplication --\n")
                operation("multiplication")

            elif option == 4:
                print("\n-- Division --\n")
                operation("division")

            elif option == 5:
                print("\n-- Challenge --\n")
                operation("challenge")

            elif option == 6:
                print("\n[SYSTEM]   Back to Main Menu..")
                break

            else:
                print("\n[SYSTEM]   Invalid Option. Select a Valid Option!!..")
        except ValueError as e:
            print(f"\n[SYSTEM]  Encountered Input Error: {e}")