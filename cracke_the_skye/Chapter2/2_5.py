#!/usr/bin/env python
# Tui Popenoe
# 2.5.py Add two number represented by linked lists

from node import Node
from unordered_list import UnorderedList

class ExtendedList(UnordredList):
    def __init__(self):
        super(UnorderedList, self).__init__()

    def add_numbers(self, lst1, lst2):
        lst_sum = 0
        current1 = lst1.head
        current2 = lst2.head
        count = 0
        while lst1.next != None:
            lst_sum += current1.data * 10 ** count
            count += 1
        count = 0
        while lst2.next != None:
            lst_sum += current2.data * 10 ** count
            count += 1
        return lst_sum
