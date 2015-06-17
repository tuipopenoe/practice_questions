#!/usr/bin/env python
# Tui Popenoe
# palindrome.py

from sys import argv

def is_palindrome(string):
    if string[::-1] == string:
        return True
    return False

def main():
    if len(argv) > 1:
        print(is_palindrome(argv[1]))
    else:
        print(is_palindrome(raw_input("Enter a string to check if it is a palindrome: ")))

if __name__ == '__main__':
    main()
