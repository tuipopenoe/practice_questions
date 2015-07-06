#!/usr/bin/env python
# Tui Popenoe
# 1.3 String Permutations

from sys import argv

def permute(string):
    """Return a list of all permutations of a string"""
    if len(string) == 0:
        return ['']
    prev_list = permute(string[1:len(string)])
    next_list = []

    for i in range(0, len(prev_list)):
        for j in range(0, len(string)):
            new_string = prev_list[i][0:j] + string[0] + prev_list[i][j:len(string)-1]
            if new_string not in next_list:
                next_list.append(new_string)
    return(next_list)

def test_permute():
    assert permute('code') == ['code', 'ocde', 'odce', 'odec',
                               'cdoe', 'dcoe', 'doce', 'doec',
                               'cdeo', 'dceo', 'deco', 'deoc',
                               'coed', 'oced', 'oecd', 'oedc',
                               'ceod', 'ecod', 'eocd', 'eodc',
                               'cedo', 'ecdo', 'edco', 'edoc']


def main():
    if len(argv) > 1:
        print(permute(argv[1]))
    else:
        print(permute(raw_input('Enter a string: ')))


if __name__ == '__main__':
    main()