#!/usr/bin/env python
# Tui Popenoe
# 1.6 Rotate 2D array 90 degrees

from sys import argv

def rotate_2d_array_90(array):
    return [list(a) for a in zip(*array[::-1])]


def rotate_2d_array_negative_90(array):
    return [list(a) for a in zip(*array)[::-1]]


def test_rotate_2d_array_90():
    test_array = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    test_result = [[7, 4, 1],
                   [8, 5, 2],
                   [9, 6, 3]]
    print(rotate_2d_array_90(test_array))
    assert rotate_2d_array_90(test_array) == test_result


def test_rotate_2d_array_negative_90():
    test_array = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    test_result = [[3, 6, 9],
                   [2, 5, 8],
                   [1, 4, 7]]
    print(rotate_2d_array_negative_90(test_array))
    assert rotate_2d_array_negative_90(test_array) == test_result


def main():
    test_rotate_2d_array_90()
    test_rotate_2d_array_negative_90()

if __name__ == '__main__':
    main()
