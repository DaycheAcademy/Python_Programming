
def create_odd_numbers():
    num = 1
    while True:
        yield num
        num += 2


def create_consecutive_numbers():
    num = 2
    while True:
        yield num
        yield num + 1
        yield num + 2
        num += 2


def gregory_leibniz(n):
    odds = create_odd_numbers()

    pi_approximate = 0
    for _ in range(n):
        pi_approximate += 4 / next(odds)
        yield pi_approximate
        pi_approximate -= 4 / next(odds)
        yield pi_approximate


def nilakantha(n):
    sequence = create_consecutive_numbers()

    pi_approximate = 3
    for _ in range(n):
        pi_approximate += 4 / (next(sequence) * next(sequence) * next(sequence))
        yield pi_approximate
        pi_approximate -= 4 / (next(sequence) * next(sequence) * next(sequence))
        yield pi_approximate


if __name__ == '__main__':

    for val in gregory_leibniz(5):
        print(val)
    print('----------------')
    for val in nilakantha(5):
        print(val)
