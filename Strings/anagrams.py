#/usr/bin/env python
# Tui Popenoe
# anagrams

from sys import argv

def is_anagram(word1, word2):
    dct1 = {}
    dct2 = {}
    for i in word1:
        dct1[i] = dct1.get(i, 0) + 1
    for j in word2:
        dct2[j] = dct2.get(j, 0) + 1
    if dct1 == dct2:
        return True
    return False

def test_is_anagram():
    assert is_anagram("elvis", "lives") == True
    assert is_anagram("dictionary", "indicatory") == True

def main():
    test_is_anagram()
    if len(argv) > 1:
        print(is_anagram(argv[1], argv[2]))
    else:
        print(is_anagram(raw_input("Enter word1: "),
                         raw_input("Enter word2: ")))

if __name__ == '__main__':
    main()
