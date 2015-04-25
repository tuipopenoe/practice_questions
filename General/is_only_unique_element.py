#!/usr/bin/env python
# is_only_unique_element.py
# Tui Popenoe

from collections import defaultdict
from sys import argv


def is_only_unique_element(lst):
    dct = defaultdict(list)
    for i, v in enumerate(lst):
        dct[v].append(i)
    for j in dct:
        if len(dct[j]) == 1:
            return j
    return None

def test_is_only_unique_element():
    assert is_only_unique_element([1, 1, 1, 2, 2, 3, 3, 4]) == 4
    assert is_only_unique_element([1, 2, 1, 2]) == None

def main():
    if len(argv) > 1:
        print(is_only_unique_element(map(int, argv[1:])))
    else:
        print(is_only_unique_element(map(int, raw_input().split())))

if __name__ == '__main__':
    main()