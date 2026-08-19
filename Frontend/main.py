# Main app first page
from authentication.login import login
from authentication.signup import signup


if __name__ == "__main__":

    while True:
        print("\n== MENTAL MATH ==\n")
        print("1. Login")
        print("2. SignUp")
        print("3. About")
        print("5. Exit")

        try:
            user_input = int(input("\nChoose an option: "))

            if user_input == 1:
                print("\nLogin")
                login()

            elif user_input == 2:
                print("\nSignup")
                signup()

            elif user_input == 3:
                print("\nAbout Section")

            elif user_input == 5:
                print("Exiting...")
                break

            else:
                print("\n[SYSTEM]       Invalid Option!!.. Choose a valid option!!")

        except ValueError as e:
            print(f"\n[SYSTEM]      Encountered input Error: {e}")