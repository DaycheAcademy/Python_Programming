import sys


def my_range(n: int):
    print('calling generator')
    start = 0
    while start < n:
        print('my_range returns: {}'.format(start))
        yield start
        start += 1


if __name__ == '__main__':
    temp = my_range(10)
    print(temp)
    r = range(10)
    print('size of temp in memory: {}'.format(sys.getsizeof(temp)))
    print('size of range(10) in memory: {}'.format(sys.getsizeof(r)))
    print('=' * 40)
    for val in temp:
        # _ = input('we are at line 21')
        print(val)
    print('=' * 40)
    for val in temp:
        # _ = input('we are at line 21')
        print(val)





