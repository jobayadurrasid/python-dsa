class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new = Node(data)
        if self.tail is None:
            new.previous = new
            new.next = new
            self.head = self.tail = new
            return
        new.previous = self.tail
        self.tail.next = new
        self.tail = new
        self.tail.next = self.head
        self.head.previous = self.tail 

    def pop(self):
        if self.tail is None:
            return None
    
        removed = self.tail
    
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = removed.previous
            self.tail.next = self.head
            self.head.previous = self.tail
    
        removed.previous = None
        removed.next = None
        return removed.data
        
    def display(self):
        if self.head is None:
            print("Empty")
            return
        current = self.head
        while True:
            print(current.data, end="<->")
            current = current.next
            if current is self.head:
                break
        print("(back to head)")

    def reversed(self):
        current = self.tail
        while True:
            print(current.data, end="<->")
            current = current.previous
            if current is self.tail:
                break
        print("(back to tail)")
