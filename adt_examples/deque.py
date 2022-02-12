"""An implementation of a Deque."""


class Deque:
    """A deque with allocated space n."""

    def __init__(self, n):
        self.buffer = [None for _ in range(n)]
        self.left = 0
        self.right = 0

    def __getitem__(self, key):
        """Return the number in the Deque using modular arithmetic."""
        return self.buffer[key % len(self.buffer)]

    def __setitem__(self, key, value):
        """Pop or push the number in the Deque or allocate more space."""
        if value is None:
            self.buffer[key % len(self.buffer)] = None
        elif self.buffer[key % len(self.buffer)] is None:
            self.buffer[key % len(self.buffer)] = value
        else:
            new_buffer = [None for _ in range(len(self) * 2)]
            for i in range(self.left, self.right):
                new_buffer[i % len(self)] = self.buffer[i % len(self)]

            self.buffer = new_buffer
            self.right -= self.left
            self.left = 0

    def append(self, x):
        """Append x to the end of the Deque."""
        self.right += 1
        self[self.right - 1] = x

    def appendleft(self, x):
        """Append x to the start of the Deque."""
        self.left -= 1
        self[self.left] = x

    def pop(self):
        """Remove the last item in the Deque and return it."""
        self.right -= 1
        x = self[self.right]
        self[self.right] = None
        return x

    def popleft(self):
        """Remove the first item in the Deque and return it."""
        self.left += 1
        x = self[self.left - 1]
        self[self.left - 1] = None
        return x

    def peek(self):
        """Return the last item in the Deque without removing it."""
        return self[self.right - 1]

    def peekleft(self):
        """Return the first item in the Deque without removing it."""
        return self[self.left]

    def __len__(self):
        """Return the number of items in the Deque."""
        return self.right - self.left

    def __iter__(self):
        """Return an iterator to iterate over self."""
        return DequeIterator(self)


class DequeIterator:
    """An iterator that iterates over a Deque."""

    def __init__(self, deque):
        self.deque = deque
        self.left = deque.left
        self.right = deque.right

    def __iter__(self):
        """Return self."""
        return self

    def __next__(self):
        """Return next number in a Deque."""
        if self.left == self.right:
            raise StopIteration
        else:
            x = self.deque[self.left]
            self.left += 1
            return x
