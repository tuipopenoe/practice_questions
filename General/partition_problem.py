#!/usr/bin/env python
# Tui Popenoe
# partition_problem.py

def find_partition(int_list):
    """Attempt to partition an integer list into two sublists that
    minimizes the difference between the sums of the two sublists"""
    a = []
    b = []
    for i in sorted(int_list, reverse=True):
        a.append(i) if sum(a) < sum(b) else b.append(i)
    return [a, b]

def main():


if __name__ == '__main__':
    main()