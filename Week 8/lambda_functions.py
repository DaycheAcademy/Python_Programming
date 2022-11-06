# Alonzo Church 1930's : lambda calculus
# computational based, pure, abstract, stateless ----> functional programming
# Haskell, Lisp, Erlang

# Alan Turing ---> Turing Machine
# Imperative Coding --> C / Python

# lambda <bind variable(s)>: body

from itertools import islice


def add_one(n):
    return n + 1


# inline function
one_adder = lambda n: n + 1
print(one_adder(3))

adder = lambda x, y: x + y
print(adder(2, 3))

print(lambda x, y: x * y(3, 4))

# can be anonymous
# single line
# no support for statements, only expressions
# IIFE: Immediately Invoked Function Execution
# no support for annotation

sampleList = [('apple', 4, 3.78, 9), ('orange', 8, 1.25, 2),
              ('banana', 2, 8.46, 7), ('cherry', 1, 5.14, 5)]

sampleList.sort(key=lambda x: x[1])
print(sampleList)

sampleList.sort(key=lambda x, d_type=str: x[[int(isinstance(i, d_type)) for i in x].index(1)])
print(sampleList)

print('=' * 40)

sampleList.sort(key=lambda x, n=1, d_type=int: x[next(islice([ind for ind, val in enumerate(x) if isinstance(val, d_type)], n-1, n), None)])
print(sampleList)

