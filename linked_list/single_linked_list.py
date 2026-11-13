class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self,data):
        element = Node(data)

        if self.head is None:
            self.head = element
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = element

    def prepend(self, data):

        element = Node(data)
        element.next = self.head
        self.head = element

    def find(self, data):
        current = self.head
        while current:
            if data == current.data:
                return True
            current = current.next

        return False


    def pop_front(self):
        if self.head:
            self.head = self.head.next

    def length(self):
        counter = 0
        current = self.head
        while current:
            counter+=1
            current = current.next  
        return counter      

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
