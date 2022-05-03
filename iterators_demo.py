# iterators
sampleString = 'ABCDE'
sampleList = [1, 2, 3]

for char in sampleString:
    print(char)

# i: iterator
# sampleString: iterable object

elem = iter(sampleList)
char = iter(sampleString)
print(type(char))
print(type(elem))

print('=' * 40)
print(next(char))  # A
print(next(char))  # B
print(next(char))  # C
print(next(char))  # D
print(next(char))  # E

print(next(char))  # ?





















