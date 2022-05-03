
alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for even, odd in zip(alphabetString[::2], alphabetString[1::2]):
    print(even, odd)

print(alphabetString[::-1])


