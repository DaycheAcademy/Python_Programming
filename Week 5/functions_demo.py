# def <function_name>(parameters):
#     1-
#     2-

def temp():
    print('inside temp function')
    return {'Dayche', 5}


def adder(a, b, c=1, d=2):  # parameters
    return a + b + c + d


# **kwargs --> double star unpacks a dictionary
def multiple_adder(*args, indicator=':', inx=1):
    print(type(args))
    print(args)
    sumOfAllValues = 0
    for ind, arg in enumerate(args, inx):
        print('input #{}{} {}'.format(ind, indicator, arg))
        sumOfAllValues += arg
    return sumOfAllValues

# * ---> star unpacks a tuple

# non_default arguments --> positional arguments
# default arguments --> keyword arguments


# all functions in python return 'None' by default
print(temp())
print('-----------')
print(temp)

# print:
# str()
# repr()

sumOfTwoNumbers = adder(b=4, a=5, d=7)  # arguments
print(sumOfTwoNumbers)

# =======================
print('-----------')
print(multiple_adder(3, 87, 3, 8, 901, 654, 4, 7, 6, indicator='-->', inx=0))

