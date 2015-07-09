#!/usr/bin/env python
# Tui Popenoe
# 2.3.py remove the middle element 

from node import Node
from unordered_list import UnorderedList

class ExtendedList(UnordredList):
    def __init__(self):
        super(UnorderedList, self).__init__()

    def remove_middle_element(self):
        current_node = self.head
        if current_node.next:
            skip_node = current_node.next
        else:
            skip_node = None
        while current_node.next != None:
            # skip 2 nodes for every 1 current_node
            if skip_node.next.next != None and skip_node.next != None:
                skip_node.next = skip_node.next.next
            # Reached the end of the list
            # remove current_node
            else:
                current_node.next = current_node.next.next
                break
            current_node= current_node.next