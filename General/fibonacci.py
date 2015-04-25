from sys import argv

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def test_fibonacci_iterative():
    assert fibonacci_iterative(7) == 13

def test_fibonacci_recursive():
    assert fibonacci_recursive(6) == 8

def main():
    test_fibonacci_recursive()
    test_fibonacci_iterative()
    if len(argv) > 1:
        print(fibonacci_iterative(int(argv[1])))
    else:
        print(fibonacci_recursive(int(raw_input())))

if __name__ == '__main__':
    main()