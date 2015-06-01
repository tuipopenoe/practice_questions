#/usr/bin/env python
# Tui Popenoe
# string_reverse.py

from sys import argv

def string_reverse_iterative(string):
    return string[::-1]

def string_reverse_recursive(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + string_reverse_recursive(string[:-1])


def test_reverse():
    assert string_reverse_iterative("Allyourbasearebelongtous") == \
        "suotgnoleberaesabruoyllA"

def main():
    test_reverse()
    if len(argv) > 1:
        print(string_reverse_iterative(argv[1]))
        print(string_reverse_recursive(argv[1]))

if __name__ == '__main__':
    main()
