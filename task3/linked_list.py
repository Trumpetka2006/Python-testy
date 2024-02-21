from pytest import warns


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

        self.maxIndex = 0
        self.minIndex = 0

    def append(self, item):
        node = Node(item)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return
        else:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node
            self.length += 1

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        if key >= self.length or key <= -self.length:
            raise IndexError
        if key >= 0:
            node = self.head
            for i in range(key):
                node = node.next_node
        else:
            node = self.tail
            for i in range(abs(key)):
                node = node.prev_node
        return node.data

    def __setitem__(self, index, data):
        if index == 0:
            self.head = Node(data)
        else:
            node = self.head
            for position in range(index):
                node = node.next_node
            node.data = data

    def __delitem__(self, index):
        self.length -= 1
        if index == 0:
            self.head = self.head.next_node
            self.head.prev_node = None
        else:
            node = self.head
            for i in range(index - 1):
                node = node.next_node
            prev = node
            for i in range(2):
                node = node.next_node
            node.prev_node = prev
            prev.next_node = node

    def insert(self, data, index):
        if index > self.length:
            raise IndexError
        if index == 0:
            if self.length != 0:
                node = self.head
                self.head = Node(data)
                node.prev_node = self.head
                self.head.next_node = node
            else:
                self.head = Node(data)
        else:
            node = self.head
            for i in range(index - 1):
                node = node.next_node
            newNode = Node(data)
            if self.length != index:
                newNode.next_node = node.next_node
            newNode.prev_node = node
            node.next_node = newNode

        self.length += 1
