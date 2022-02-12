"""An iterator that will return the Fibonacci numbers indefinitely."""


class Fib:
    """An iterator that returns Fibonacci numbers."""

    def __init__(self):
        self.value1 = 0
        self.value2 = 1

    def __iter__(self):
        """Return self."""
        return self

    def __next__(self):
        """Return next Fibonacci number."""
        value = self.value1 + self.value2
        self.value1 = self.value2
        self.value2 = value
        return value
