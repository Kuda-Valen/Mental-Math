""" User input, Main Menu, & Time formatting """

def addition_functions():
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
                    