""" Target calculation logic (ADD, SUB, MUL, DIV) """

from engine.generator import random_numbers


class Numbers():
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        

class Addition(Numbers):
    def __init__(self, a: int, b:int, c: int, d: int, e: int):
        super().__init__(a, b)
        self.answer = a + b + c + d + e

    def check_answer(self,  answer):
        if answer == self.answer:
            return True
        else:
            return False

class Subtraction(Numbers):
    def __init__(self, a: int, b: int):
        super().__init__(a, b)
        self.x = a + b

    def return_answer(self):
        return self.x
    
    def check_ans(self, answer):
        if answer == self.b:
            return True
        else:
            return False
    