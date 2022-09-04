from nodes.Node import Node

"""
Name:
Matric Number:
Department:
Program:
Level:
"""


class SingleLinkedList:
    def __init__(self):
        self.newNode: Node = None
        self.head: Node = None
        self.tail: Node = None
        self.curr: Node = None
        self.__counter = -1

    def display(self):
        self.curr = self.head
        if self.curr is None:
            print("Empty")

        print('[', end='')
        while self.curr is not None:
            print('{}'.format(self.curr.data), end='-->')
            self.curr = self.curr.next
        print(']', end=',')

    def append(self, node: Node):
        self.newNode = node
        self.curr = self.head
        if self.curr is None:
            self.head = self.newNode
            self.tail = self.head
        else:
            self.tail.next = self.newNode
            self.tail = self.tail.next

        self.__counter += 1

    def search(self, value):
        self.curr = self.head
        self.__cnt = 0
        if self.curr is None:
            return None
        while self.curr is not None:
            if self.curr.data is value:
                # print('value at location {}'.format(self.__cnt))
                return [True, self.__cnt]
            self.curr = self.curr.next
            self.__cnt += 1
        return [False]
