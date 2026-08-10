""" Target calculation logic (ADD, SUB, MUL, DIV) """

from engine.generator import random_number


class Numbers():
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

class Addition(Numbers):
    def __init__(self, a, b, c, d, e):
        super().__init__(a, b, c, d, e)

    def sum(self):
        self.answer = self.a + self.b + self.c + self.d + self.e

    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False
    