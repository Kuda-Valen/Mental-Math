""" Difficulty ranges & global settings """

def challenge():
    print("1. Begginer")
    print("2. Intermediate")
    print("3. Advanced")
    print("4. Genius")

    try:
        user_input = int(input("\nChoose your Challenge: "))
        return user_input
    except ValueError as e:
        print(f"\n[SYSTEM]   Encountered Input Error ->: {e}")