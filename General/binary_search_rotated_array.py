#!/usr/bin/env python
# Tui Popenoe
# Binary Search Rotated Array

def binary_search_rotated_array(a, x, lo=0, hi=None):
    if not hi:
        hi = len(a) - 1
    val, idx = min((val, idx) for (idx, val) in enumerate(a))
    a = a[idx:] + a[:idx]
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid
        else:
            hi = mid
    return - 1

def main():
    binary_search_rotated_array(map(int, raw_input("Enter a rotated array of int:" )),
        int(raw_input("Enter an int to search for: ")))

if __name__ == '__main__':
    main()