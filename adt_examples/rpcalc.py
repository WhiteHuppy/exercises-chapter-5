from numbers import Number
import math

"""An implementation of a reverse Polish calculator."""


class RPCalc:
    def __init__(self,):
        self.stack = []

    def push(self, n):
        if isinstance(n, Number):
            self.stack.append(n)
        elif isinstance(n, str):
            if n in ("+", "-", "*", "/"):
                operand2 = self.pop()
                operand1 = self.pop()
                self.push(eval(f"{operand1} {n} {operand2}"))
            elif n in ("sin", "cos"):
                operand = self.pop()
                self.push(getattr(math, n)(operand))

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)
