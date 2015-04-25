from sys import argv

def int_pair_sum(lst, target=10):
    dct = {value: index for (index, value) in enumerate(lst)}
    output = []
    for i, v in enumerate(lst):
        x = dct.get(target - v)
        if x != i and x != None:
            output.append((i, dct[target - lst[i]]))
    return output[:len(output)/2]

def test_int_pair_sum():
    lst = [3, 6, 5, 1, 2, 7, 9, 8, 4, 0]
    correct = [(0, 5), (1, 8), (3, 6), (4, 7)]
    assert correct == int_pair_sum(lst)

def main():
    #test_int_pair_sum()
    if len(argv) > 1:
        print(int_pair_sum(map(int, argv[1:])))
    else:
        print(int_pair_sum(map(int, raw_input().split())))

if __name__ == '__main__':
    main()