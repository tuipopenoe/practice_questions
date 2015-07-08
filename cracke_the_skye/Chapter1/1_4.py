#!/usr/bin/env python
# Tui Popenoe
# 1.4 String Replace


from sys import argv

def string_replace(string, char=' ', rep='%20'):
    return string.replace(char, rep)

def string_replace_in_place(string, char=' ', rep='%20'):
    string = string.replace(char, rep)

def test_string_replace():
    assert string_replace('hello world') == 'hello%20world'

def test_string_replace_in_place():
    assert string_replace_in_place('hello world') == 'hello%20world'

def main():
    if len(argv) > 1:
        print(string_replace(argv[1:]))
    else:
        print(string_replace(raw_input('Enter a string to replace: ')))

if __name__ == '__main__':
    main()