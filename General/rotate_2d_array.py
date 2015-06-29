#!/usr/bin/env python
# Tui Popenoe
# rotate_2d_array.py

def rotate2darray(array):
    """Rotates the 2d array 90 degrees"""
    return zip(*array[::-1])


def test_rotate_2d_array():
    test_array = [[1, 2, 3],
                  [4, 5, 6,],
                  [7, 8, 9]]
    outcome = [[7, 4, 1],
               [8, 5, 2],
               [9, 6, 3]]
    assert rotate2darray(test_array) == outcome

def main():
    test_rotate_2d_array()

if __name__ == '__main__':
    main()
