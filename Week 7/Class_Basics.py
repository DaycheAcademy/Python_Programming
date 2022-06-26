
# class <ClassName>(object):
     # Body of the class
import time

# old type vs new type classes


class Kettle(object):

    # class attribute
    power = 'electric'

    # constructor
    def __init__(self, brand, price):
        # instance attributes
        self.brand = brand
        self.price = price
        self.model = '2020'
        self.on = False
        self.temp = 15

    # def __init__(self):
    #     pass

    def turn_on(self):
        self.on = True

    def set_temperature(self, degree):
        while self.temp < degree:
            self.temp += 1
            time.sleep(1)
        print('temperature is set to {} degrees'.format(degree))


if __name__ == '__main__':

    smeg = Kettle('smeg', 5000000)  # instantiate   (smeg is an 'instance' of class Kettle)
    pars_khazar = Kettle('pars khazar', 2000000)

    print(smeg.brand)
    print(smeg.price)
    print(pars_khazar.model)
    pars_khazar.model = '2022Alpha'
    print(pars_khazar.model)
    print(smeg.model)
    smeg.turn_on()
    print(smeg.on)

    print('=' * 40)
    print(smeg.__dict__)
    print(Kettle.__dict__)
    print(smeg.power)
    print(Kettle.power)

    pars_khazar.power = 'gas'
    print(pars_khazar.__dict__)
    print('=' * 40)

    smeg.handle = 'plastic'
    print(smeg.__dict__)








