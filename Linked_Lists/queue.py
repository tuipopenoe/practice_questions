#!/usr/bin/env python
# Tui Popenoe
# queue.py 

class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """O(1)"""
        self.items.insert(0, item)

    def dequeue(self):
        """O(1)"""
        return self.items.pop()

    def size(self):
        """O(1)"""
        return len(self.items)