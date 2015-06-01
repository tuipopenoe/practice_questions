#!/usr/bin/env python
# Tui Popenoe
# Is Palindrome?

def is_palindrome(word):
    w_len = len(word)//2 - len(word) % 2
    return word[w_len:] == word[:w_len:-1]

def main():
    print(is_palindrome(raw_input("Enter a word to check if palindrome: ")))

if __name__ == '__main__':
    main()
