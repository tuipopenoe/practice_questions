#!/usr/bin/env python
# Tui Popenoe
# hash_table.py

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] = None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                next_slot = self.rehash(hashvalue, len(self.slots))
                while self.slots[next_slot] != None and \
                    self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhas + 1) % size

    def get(self, key):
        start_slot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)