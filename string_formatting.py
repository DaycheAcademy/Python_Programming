import math
alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
name = 'Mehdi'
age = 20

print('My name is Mehdi, I am 18')

print('My name is', name, ', I am', age)

# String Formatting
print('My name is {}, I am {}'.format(name, age))
print('My name is {1}, I am {0}'.format(age, name))

print(
"""Farvardin: {2}
Ordibehesht: {2}
Khordad: {2}
Tir: {2}
Mordad: {2}
Shahrivar: {2}
Mehr: {1}
Aban: {1}
Azar: {1}
Dey: {1}
Bahman: {1}
Esfand: {0}""". format(29, 30, 31))

print('=' * 40)

for number in range(16):
    print('{0:<3} to the power of 2 is: {1:>6.2f}'.format(number, number ** 2 / 3))

# Casting : Converting One Data Type to Another
print(float('{:.3f}'.format(math.pi)))

print(int(math.pi))

# Casting: Implicit, Explicit

# =================================
print('=' * 40)
print('My name is %s, I am %s' %(name, age))

# print('My name is {}, I am {}'.format(name, age))
print(f'My name is {name}, I am {age}')

# ========================================
print('hello, my name is Mehdi \nI am 20')

print('hello \\this is fun !')
myFilePath = 'C:\\Users\\DaBigM\\Desktop\\python Dayche'






