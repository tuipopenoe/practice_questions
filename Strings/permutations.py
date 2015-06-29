#!/usr/bin/env python
# Tui Popenoe
# permutations.py

from sys import argv

def permute(string):
    """Return a list of all permutations of a string"""
    # If the string is empty, return a list with an empty string
    if len(string) == 0:
        return ['']
    # Otherwise recurse down the next smallest substring
    prev_list = permute(string[1:len(string)])
    next_list = []
    # For each item in the previous list
    for i in range(0, len(prev_list)):
        # For each permutation in the string
        for j in range(0, len(string)):
            # Add new character to every position in previous string
            new_string = prev_list[i][0:j] + string[0] + prev_list[i][j:len(string)-1]
            if new_string not in next_list:
                next_list.append(new_string)
    print(next_list)
    return next_list


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