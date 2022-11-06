
# Sequence:
# 1 - Ordered
# 2 - Indexable  ---> Default : start from Zero

alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Indexing
print(alphabetString[0])
print(alphabetString[12])

# Slicing
print(alphabetString[0: 13])
print(alphabetString[0: 13: 2])
# print(alphabetString[start: stop: step])

print('=' * 40)
print(alphabetString[:13])
print(alphabetString[2:])
print('=' * 40)

print(alphabetString[-1])
print(alphabetString[-13])
print(alphabetString[13])
print('=' * 40)

# alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabetString[-1: -10])
print(alphabetString[-3: 5])
print('-------')

print(alphabetString[3: -5])
print(alphabetString[-2: 3: -1])















