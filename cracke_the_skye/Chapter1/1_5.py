#!/usr/bin/env python
# Tui Popenoe
# 1.5 String Compression

from sys import argv

def compress(string):
    output = []
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            count += 1
        else:
            output.append('%s%s' % (string[i], str(count)))
            count = 1
    if count == 1:
        output.append('%s%s' % (string[-1], '1'))
    else:
        output.append('%s%s' % (string[i], str(count)))
    if len(''.join(output)) < len(string):
        return ''.join(output)
    else:
        return string

def test_compress():
    assert compress('aaabccddddee') == 'a3b1c2d4e2'
    assert compress('aabbccd') == 'aabbccd'
    assert compress('aaabbbccd') == 'a3b3c2d1'

def main():
    test_compress()
    if len(argv) > 1:
        print(compress(''.join(argv[1:])))
    else:
        print(compress(raw_input('Enter a string to compress: ')))

if __name__ == '__main__':
    main()
