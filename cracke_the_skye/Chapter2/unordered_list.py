#!/usr/bin/env python
# Tui Popenoe
# unordered_list.py

class UnordredList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return item
            else:
                current = current.get_next()
        return None

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not Found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
