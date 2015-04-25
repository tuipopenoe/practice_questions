def is_rotated_array(lst1, lst2):
    for i, v in enumerate(lst2):
        if lst1 == lst2[i:] + lst2[:i]:
            return True
    return False

def test_is_rotated_array():
    assert is_rotated_array([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 7, 8, 1, 2, 3, 4])

def main():
    test_is_rotated_array()
    print(is_rotated_array(map(int, raw_input().split()), map(int, raw_input().split())))

if __name__ == '__main__':
    main()