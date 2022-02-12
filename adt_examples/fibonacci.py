"""An iterator that will iterate over the Fibonacci numbers indefinitely."""


class Fib:
    def __init__(self):
        self.value1 = 0
        self.value2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value1 + self.value2
        self.value1 = self.value2
        self.value2 = value
        return value
