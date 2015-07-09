#!/usr/bin/env python
# Tui Popenoe
# 2.1 Remove duplicates from an unsorted list

from node import Node
from unordered_list import UnorderedList

class ExtendedList(UnorderedList):
    def __init__(self):
        super(UnorderedList, self).__init__()


    def remove_duplicates():
        node_data = {}
        duplicates = {}
        current_node = self.head
        # Iterate through nodes, if a duplicate is found, add it to the dict
        while current_node.next != None:
            if current_node.data not in node_data:
                node_data[current_node.data] = current_node.data
            else:
                duplicates.get(current_node.data, 0) += 1
            # increment current node
            current_node = current_node.next
        # reset current node
        current_node = self.head
        # Iterate through nodes, removing duplicates
        while current_node.next != None:
            check_data = current_node.next.data
            if check_data in duplicates:
                # skip pointer 
                current_node.next = current_node.next.next
                # decrement or remove from duplicates dict
                if duplicates[check_data] <= 1:
                    del duplicates[check_data]
                else:
                    duplicates[check_data] -= 1
