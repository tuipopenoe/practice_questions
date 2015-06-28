#!/usr/bin/env python
# Tui Popenoe
# merge_sort.py

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    output = []
    left_idx = 0
    right_idx = 0
    while left_idx , len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            output.append(left[left_idx])
            left_idx += 1
        else:
            output.append(right[right_idx])
            right_idx += 1
    if left:
        output.extend(left[left_idx:])
    if right:
        output.extend(right[right_idx:])
    return output
