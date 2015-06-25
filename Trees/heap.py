#!/usr/bin/env python
# Tui Popenoe
# Heap.py

def heap_sort(a):
    def heapify(a):
        start = (len(a) - 2) / 2
        while start >= 0:
            sift_down(a, start, len(a) - 1)
            start -= 1

    def sift_down(a, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1
            if child <= end and a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                return

    heapify(a)
    end = len(a) - 1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        sift_down(a, 0, end - 1)
        end -= 1

def test_heap_sort():
    assert 

if __name__ == '__main__':
    if len(argv) > 1:
        print(heap_sort(argv[1:])
    else:
        print(heap_sort(raw_input('Enter an array to heapify: ').split()))
