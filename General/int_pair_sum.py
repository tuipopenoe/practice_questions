from sys import argv

def int_pair_sum(lst, target=10):
    dct = {value: index for (index, value) in enumerate(lst)}
    output = []
    for i, v in enumerate(lst):
        x = dct.get(target - v)
        if x != i and x != None:
            output.append((i, dct[target - lst[i]]))
    return output

def test_int_pair_sum():
    lst = [3, 6, 5, 1, 2, 7, 9, 8, 4, 0]
    correct = set([(3, 7), (1, 9), (4, 6), (2, 8)])
    assert correct == set(int_pair_sum(lst, 10))

def main():
    if len(argv) > 1:
        print(int_pair_sum(map(int, argv[1:])))
    else:
        print(int_pair_sum(map(int, raw_input().split())))

if __name__ == '__main__':
    main()