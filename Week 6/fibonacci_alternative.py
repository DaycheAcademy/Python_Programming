
def fibo(n):
    previous, current = 0, 1
    for _ in range(n):
        print(current)
        previous, current = current, previous + current


# Generators
def fibonacci(n):
    previous, current = 0, 1
    for _ in range(n):
        # print(current)
        yield current
        # return current
        previous, current = current, previous + current


if __name__ == '__main__':
    fibo(100)
    print('=' * 40)
    for number in fibonacci(50):
        print(number)




