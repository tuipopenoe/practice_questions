#!/bin/env/python
# quicksort.py
# Tui Popenoe

def quicksort(lst):
    """Quicksort using list comprehensions"""
    if not lst:
        return []
    else:
        pivot = lst[0]
        lesser = quicksort([x for x in lst[1:] if x < pivot])
        greater = quicksort([x for x in lst[1:] if x >= pivot])
    return lesser + [pivot] + greater