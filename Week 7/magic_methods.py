
# meta class
class Foo(object):

    def __new__(cls):
        print('new is called')
        return object.__new__(cls)

    def __init__(self):
        self.a = 1
        print('init is called')

    def __str__(self):
        return 'a has now the value of: {}'.format(self.a)

    def __call__(self):
        print('method call is initiated')

    # getters and setters
    def set_a(self, val):
        self.a = val

    def get_a(self):
        return self.a


if __name__ == '__main__':

    f = Foo()
    f.set_a(5)
    print(f)
    f()






