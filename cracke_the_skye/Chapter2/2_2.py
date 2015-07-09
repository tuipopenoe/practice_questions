#!/usr/bin/env python
# Tui Popenoe
# 2.2.py find kth to last element of singly linked list

from node import Node
from unordered_list import UnorderedList

class ExtendedList(UnordredList):
    def __init__(self):
        super(UnorderedList, self).__init__()

    def find_kth_to_last_element(self, k):
        current_node = self.head
        counter = 1 if current_node else counter = 0
        while current_node.next != None:
            counter += 1
        counter = counter - k
        while current_node.next != None:
            counter -= 1
            if counter == 0:
                return current_node
            current_node = current_node.next
        return None