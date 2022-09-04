"""
Name:
Matric Number:
Department:
Program:
Level:
"""

# Task 1:                                                 Total: 7 marks
from datastructures.LinkedLists import SingleLinkedList
from nodes.Node import Node  # DO NOT REMOVE IMPORTANT FOR DEBUGGING task_1c_i()


class HashTable:  # 2 mark (declare: bonus)
    found: tuple

    def __init__(self, ksize, h_func):  # a) and b):        2 marks (Modify)
        """
        @:parameter: found, @:parameter: ksize, @:parameter: h_func
        @:type tuple: found, @:type int: h_func, @:type int: ksize
        """
        # Task 1: b): htable, ksize, found                       3 marks (declaration)
        pass

    # Task 1: c) i.                                                Total: 8 marks (Debug)
    def task_1c_i(self):   # Separate Chaining
        # Hint: Study the code very well to find the bug.
        for j in range(self.h_func):
            self.htable.append(SingleLinkedList())

        for i in range(self.ksize):
            ind = i % self.h_func
            self.htable[ind].append()

    # Task 1: c) ii.                                                Total: 8 marks (implementation)
    def task_1c_ii(self):
        pass

    def display(self):
        print('displaying content(s) of hash table...')
        print('[', end='')
        for i in range(len(self.htable)):
            self.htable[i].display()
            if i == len(self.htable) - 1:
                print(']', end='')
