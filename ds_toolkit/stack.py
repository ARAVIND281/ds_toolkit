class Stack:
    """Stack implementation using a list."""

    def __init__(self):
        self._stack = []

    def push(self, value):
        """Push an element onto the stack."""
        self._stack.append(value)

    def pop(self):
        """Pop the top element from the stack."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self._stack.pop()

    def top(self):
        """Return the top element of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Top from an empty stack")
        return self._stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self._stack)

    def to_list(self):
        """Return the stack as a list."""
        return self._stack[:]
