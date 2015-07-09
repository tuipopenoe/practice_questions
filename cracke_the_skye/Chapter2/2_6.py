#!/usr/bin/env python
# Tui Popenoe
# 2.4.py partition around x element

from node import Node
from unordered_list import UnorderedList

class ExtendedList(UnordredList):
    def __init__(self):
        super(UnorderedList, self).__init__()

    def correct_circular_list(self):
        current_node = self.head
        nodes = {}
        while current_node.next != None:
            current_node = current_node.next
            # Correct 
            if current_node.next.data in nodes:
                current_node.next = None
            else:
                nodes[current_node.next.data] = current_node.next.data


