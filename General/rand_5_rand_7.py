#!/usr/bin/env python
# Tui Popenoe
# Rand5Rand7

from random import randint

def rand_7():
    return (rand_5() + rand_5() + rand_5() + rand_5() + rand_5()) % 7

def rand_5():
    return randint(0,5)

def main():
    return rand_7()

if __name__ == '__main__':
    main()
