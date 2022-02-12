"""An implementation of a reverse Polish calculator."""

from numbers import Number
import math


class RPCalc:
    """A reverse Polish calculator."""

    def __init__(self,):
        self.stack = []

    def push(self, n):
        """Add to the stack if a number, else perform an operation."""
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
        """Remove and return the top of the stack."""
        return self.stack.pop()

    def peek(self):
        """Return the top of the stack."""
        return self.stack[-1]

    def __len__(self):
        """Return length of stack."""
        return len(self.stack)
