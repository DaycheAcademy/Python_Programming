import sys


def get_int(prompt):
    inp = None
    while True:
        try:
            inp = int(input(prompt))
            break
        except ValueError:  # catch
            print('we need an int !')
            continue
        except EOFError:
            print('Please do not try to break the program !')
            sys.exit(-1)
        except Exception:
            print('we do not know what happened ! something is wrong !')

        # except:
        #     print('Please do not try to break the program !')
        #     continue

        else:  # optional
            print('age be exception nakhorim ejra mishe')
        finally:
            print('man asab nadaram ! dar har halati ejra misham')

    return inp


in1 = get_int('enter first number: ')
in2 = get_int('enter second number: ')

try:
    print('result: ', in1 / in2)
except ZeroDivisionError:
    print('second number cannot be ZERO !')

