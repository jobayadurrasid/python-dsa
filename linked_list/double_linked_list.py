class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new = Node(data)
        if self.tail is None:
            self.head = self.tail = new
            return
        new.previous = self.tail
        self.tail.next = new
        self.tail = new

    def pop(self):
        if self.tail is None:
            return None

        removed = self.tail
        self.tail = removed.previous

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        removed.previous = None
        removed.next = None

        return removed.data
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end="<->")
            current = current.next

        print("None")
    def reversed(self):
        current = self.tail
        while current:
            print(current.data, end="<->")
            current = current.previous
        print("None")
