numericString = '34,0.86457,-23,0,876587,2,8'

# if numericString[-1] != ',':
#     numericString += ','

number = ''
sumOfNumbers = 0
for char in numericString:
    if char in '0123456789.-':
        number += char
    else:
        sumOfNumbers += float(number)
        number = ''
sumOfNumbers += float(number)
print(sumOfNumbers)

print('=' * 40)

# =====================================

mySum = 0
numericList = numericString.split(',')
print(numericList)
for num in numericList:
    mySum += float(num)
print(mySum)

# ==========================================

# list comprehension
print(sum([float(num) for num in numericString.split(',')]))










