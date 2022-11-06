
class Duck(object):

    @staticmethod
    def swim():
        print('I swim like a duck !')

    @staticmethod
    def quack():
        print('quack !')

    @staticmethod
    def walk():
        print('I walk like a duck !')


class Penguin(object):

    @staticmethod
    def swim():
        print('I swim fassstttttt !')

    @staticmethod
    def quack():
        print('I do not quack !')

    @staticmethod
    def walk():
        print('I walk like a duck too!')


def ducktest(bird):
    bird.swim()
    bird.quack()
    bird.walk()


if __name__ == '__main__':

    duck = Duck()
    penguin = Penguin()

    ducktest(duck)
    print('=' * 40)
    ducktest(penguin)

# static vs dynamic
# strong vs weak
# strict vs loose
# duck typed


