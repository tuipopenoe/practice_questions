#!/usr/bin/env python
# Tui Popenoe
# 1.2

from sys import argv

def reverse(string):
    return string[::-1]


def reverse_c_style(string):
    length = len(string)
    string = list(string)
    for i in range(length - 1):
        temp = string[i]
        string[i] = string[i+1]
        string[i+1] = temp
    return ''.join(string)


def test_reverse():
    assert reverse('hello') == 'olleh'


def test_reverse_c_style():
    assert reverse_c_style('hello') == 'olleh'


def main():
    test_reverse()
    test_reverse_c_style()
    if len(argv) > 1:
        print(reverse(argv[1:]))
    else:
        print(reverse(raw_input('Enter a string to reverse: ')))

if __name__ == '__main__':
    main()
