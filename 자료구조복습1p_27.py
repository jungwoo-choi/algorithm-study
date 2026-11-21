class Node:
    def __init__(self, data): "전달받은 값을 node의 data에 저장하고, prev와 next를 None으로 초기화"
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data):
        new_node = Node(data)

        if self.head is None:
           self.head = new_node
           self.tail = new_node
        else:
           new_node.next = self.head
           self.head.prev = new_node
           self.head = new_node


def insert_last(self, data):
    new_node = Node(data)

    if self.tail is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node


def insert_after(self, target, data):
    current = self.head

    while current is not None:
        if current.data == target:
            new_node = Node(data)

            new_node.prev = current
            new_node.next = current.next

            if current.next is not None:
                current.next.prev = new_node
            else:
                self.tail = new_node

            current.next = new_node
            return

        current = current.next


def delete_first(self):
    if self.head is None:
        return

    if self.head == self.tail:
        self.head = None
        self.tail = None
    else:
        self.head = self.head.next
        self.head.prev = None


def delete_last(self):
    if self.tail is None:
        return

    if self.head == self.tail:
        self.head = None
        self.tail = None
    else:
        self.tail = self.tail.prev
        self.tail.next = None


def delete(self, data):
    current = self.head

    while current is not None:
        if current.data == data:
            if current == self.head:
                self.delete_first()
            elif current == self.tail:
                self.delete_last()
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
            return

        current = current.next


def search(self, data):
    current = self.head

    while current is not None:
        if current.data == data:
            return current
        current = current.next

    return None


def print_forward(self):
    current = self.head

    while current is not None:
        print(current.data, end=" ")
        current = current.next

    print()


def print_backward(self):
    current = self.tail

    while current is not None:
        print(current.data, end=" ")
        current = current.prev

    print()
    
