#!/usr/bin/env python
# Tui Popenoe
# Binary Search

def binary_search(a, x, lo=0, hi=None):
    if not hi:
        hi = len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        print(mid)
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid
        else:
            hi = mid
    return -1

def main():
    binary_search(map(int, raw_input("Enter a sorted series of int: ")),
                  int(raw_input("Enter a value to search for: ")))

if __name__ == '__main__':
    main()