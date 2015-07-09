#!/usr/bin/env python
# Tui Popenoe
# 2.4.py partition around x element

from node import Node
from unordered_list import UnorderedList

class ExtendedList(UnordredList):
    def __init__(self):
        super(UnorderedList, self).__init__()


    def partition(self, x):
        lesser = ExtendedList()
        greater = ExtendedList()
        current_node = self.head
        while current_node.next != None:
            if current_node.data < x:
                lesser.tail = current_node
                lesser.add_node(current_node)
            else:
                greater.add_node(current_node)
            current_node = current_node.next
        lesser.tail.next = greater.head