class Stack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) == self._capacity

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def push(self, value):
        if self.is_full():
            return False
        self._data.append(value)
        return True

    def top(self):
        if self.is_empty():
            return None
        return self._data[-1]
