# Author: Ian Ording
# Date: 2/19/20
# Description:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        if self.head == None:
            return
        if self.head.data == val:
            self.head = self.head.next
        else:
            current = self.head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:
                previous.next = current.next

    def is_empty(self):
        return self.head is None

    def contains(self, val):
        if self.head == None:
            return
        if self.head.data == val:
            return True
        else:
            current = self.head
            while current is not None and current.data != val:
                previous = current
                current = current.next
                if current.data == val:
                    return True
                if current.next == None:
                    return False

    def insert(self, val, pos):
        if pos == 0:
            temp = self.head
            print("val:", self.head.data)
            self.head = Node(val)
            self.head.next = temp
        else:
            current = self.head
            counter = 0
            for _ in range(pos - 1):
                if current.next is None:
                    current.next = Node(val)
                    return
                current = current.next
            temp = current.next
            current.next = Node(val)
            current.next.next = temp

    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

def main():
    myList = LinkedList()
    myList.add(13)
    myList.add(9)
    myList.add(81)
    myList.display()
    print(myList.contains(12))
    myList.remove(81)
    myList.display()
    myList.insert(69, 1)
    myList.display()
    myList.reverse()
    myList.display()

if __name__ == "__main__":
    main()