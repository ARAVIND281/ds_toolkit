class Queue:
    """Queue implementation using a list."""
    
    def __init__(self):
        self._queue = []

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        self._queue.append(value)

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self._queue.pop(0)

    def front(self):
        """Return the element at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self._queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self._queue)

    def to_list(self):
        """Return the queue as a list."""
        return self._queue[:]
