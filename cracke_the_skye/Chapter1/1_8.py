#!/usr/bin/env python
# Tui Popenoe
# Check if string is a rotation of another string, using only 1 call to is_substring

def is_rotation(string1, string2):
    if len(string1) == len(string2):
        doubled = '%s%s' % (string1, string1)
        if is_substring(doubled, string2):
            return True
    else:
        return False

def is_substring(string1, string2):
    if string2 in string1:
        return True
    else:
        return False

def test_is_rotation():
    assert is_rotation('taxsyn', 'syntax') == True
    assert is_rotation('grammar' 'margram') == True
    assert is_rotation('casting', 'rounding') == False

def test_is_substring():
    assert is_substring('megalomaniacal', 'mega') == True
    assert is_substring('convoluted', 'complex') == False

def main():
    test_is_substring()
    test_is_rotation()
    if len(argv) > 1:
        inp = ''.join(argv[1:]).split()
        print(is_rotation(inp[0], inp[1]))
    else:
        print(is_rotation(raw_input('Enter rotated word: '),
                          raw_input('Enter word to compare against: ')))

if __name__ == '__main__':
    main()