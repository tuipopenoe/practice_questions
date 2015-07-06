#!/usr/bin/env python
# Tui Popenoe
# 1.1a Determine if a string has all unique characters.
# 1.1b Do it without using an external datastructure


# 1.1a
def all_unique(string):
    """Determine if all the characters in the given string are unique."""
    str_dct = {}
    for char in string:
        if char in str_dct:
            return False
        else:
            str_dct[char] = char
    return True


# 1.1b
def all_unique_no_datastructures(string):
    """Determine if all the characters in the given string are unique 
    without using another data structure."""
    for i in string:
        for j in string:
            if i == j:
                return False
    return True


def format_string(string):
    if isinstance(string, basestring):
        return string:
    else:
        return ""


def test_all_unique():
    """Test the all_unique() method."""
    assert test_all_unique('Hello') == False
    assert test_all_unique('World') == True


def test_all_unique_no_datastructures():
    """Test the all_unique_no_datastructures() method."""
    assert test_all_unique_no_datastructures('Hello') == False
    assert test_all_unique_no_datastructures('World') == True

def test_format_string():
    """Test the format string method."""
    string = 'The String'
    not_string = 42
    assert format_string(not_string) == ""
    assert format_string(string) == "The String"


def main():
    if len(argv) > 1:
        print(all_unique(format_string(argv[1:])))
    else:
        print(all_unique(format_string(raw_input('Enter a string: '))))


if __name__ == '__main__':
    main()