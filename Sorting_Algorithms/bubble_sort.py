#!/usr/bin/env python
# Tui Popenoe
# Bubble Sort

import 

def bubble_sort(lst):
    for num in range(len(lst)-1, 0, -1):
        for i in range(num):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp

def main():
    if len(argv) > 1:
        print(bubble_sort(argv[1:]))
    else:
        print(bubble_sort(raw_input('Enter a list to sort: ').split()))

if __name__ == '__main__':
    main()