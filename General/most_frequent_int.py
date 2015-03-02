#!/usr/bin/env python
# most_frequent_int.py

def most_frequent_int(lst):
    return max(set(lst), key=lst.count)