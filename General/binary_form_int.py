#!/usr/bin/env python
# Tui Popenoe
# Binary Form of Int

def binary_form(val):
    return str(bin(val))[2:]

def main():
    binary_form(int(raw_input("Enter an integer to get the binary format: ")))

if __name__ == '__main__':
    main()
