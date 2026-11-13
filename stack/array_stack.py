class Stack:
    def __init__(self):
        self.items = []

    # Insert an element
    def push(self, data):
        self.items.append(data)

    # Remove the top element
    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    # Read the top element without removing it
    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    # Check whether stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display stack
    def display(self):
        print(self.items)
