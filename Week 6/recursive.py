# Recursive


# 1 - must call function name inside the recursive function
# 2 - must have a condition for which at some point recursion could finish

# Limitations:
# 1 - Recursion Depth : -> RecursionError
# 2 - Memory Overflow

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# Fibonacci Series
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(factorial(998))
    print('=' * 40)

    for i in range(15):
        print(fibonacci(i))




