#!/usr/bin/env python
# fizzbuzz

def fizzbuzz(n=100):
    for i in range(n):
        if fizzbuzz(i):
            print('fizzbuzz')
        elif fizz(i):
            print('fizz')
        elif buzz(i):
            print('buzz')
        else:
            print(n)

def fizz(n):
    return True if n % 5 == 0 else False

def buzz(n):
    return True if n % 3 == 0 else False

def fizzbuzz(n):
    return True if n % 3 == 0 and n % 5 == 0 else False