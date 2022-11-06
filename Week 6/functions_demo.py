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
    # global sampleVariable
    print(type(args))
    print(args)
    # local variable
    sumOfAllValues = 0
    sampleVariable = 5
    print('sampleVariable: ', sampleVariable)

    for ind, arg in enumerate(args, inx):
        print('input #{}{} {}'.format(ind, indicator, arg))
        sumOfAllValues += arg
    print(locals())
    return sumOfAllValues


if __name__ == '__main__':


    # print(sumOfAllValues)

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
    sampleVariable = 10
    print(multiple_adder(3, 87, 3, 8, 901, 654, 4, 7, 6, indicator='-->', inx=0))

    print('sampleVariable in global: ', sampleVariable)

    print('-----------')
    print('-----------')
    print('-----------')

    print('inside functions_demo file:', __name__)  # __main__
    print(globals().keys())
    print(dir())

    print('=' * 40)
    print(globals() == locals())







