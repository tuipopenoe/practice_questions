#!/usr/bin/env python
# Tui Popenoe
# 2.7 Check if linked       q2

from node import Node
from unordered_list import UnorderedList

class ExtendedList(UnordredList):
    def __init__(self):
        super(UnorderedList, self).__init__()

    def is_palindrome(self):
        lst = []
        current_node = self.head
        while current_node.next != None:
            lst.append(current_node.data)
            current_node = current_node.next

        if lst == lst[::-1]:
            return True
        return False