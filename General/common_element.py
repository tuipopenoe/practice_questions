#!/usr/bin/env python
# Tui Popenoe
# Common Elements in 2 Lists

def common_element(lst1, lst2):
    dct = {v: i for (i, v) in enumerate(lst1)}
    output = [i for i in lst2 if i in dct]
    return output

def main():
    print(common_element(map(int, raw_input()), map(int, raw_input())))

if __name__ == '__main__':
    main()