
try:
    a = input('please enter a number: ')
    a = int(a)
    b = input('please enter a number: ')
    b = int(b)
    print(a / b)
except ValueError:
    print('input is not in base 10 format')
except ZeroDivisionError:
    print('cannot perform division by zero')
except Exception:
    print('unknown error')

