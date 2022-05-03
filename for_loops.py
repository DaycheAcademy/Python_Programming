
# for <iterator> in <iterable object>:
#     1 -
#     2 -
#     3 -

# for (int i=0; i<10; i++){
#     # do some actions
# }

# for i in range(10):
#     print(i)

alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for char in alphabetString:
#     print(char)

print('=' * 40)
# for i in range(len(alphabetString)):
#     print(alphabetString[i])

# print(len(alphabetString))


# ==============================
# alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for char in alphabetString:
    if char in 'cQmnr':
        break
    if char in 'CFGJK':
        continue
    print(char)
else:
    print('agar halghe shekaste nashe man chap misham !')
# =====================================

for ind, char in enumerate(alphabetString, 1):
    print('character #{}: {}'.format(ind, char))

print('=' * 40)
sampleAlphabet = 'ABCDEF'
sampleNumbers = '123456'

for num, char in zip(sampleNumbers, sampleAlphabet):
    print(f'{num}: {char}')

# operators in python
# int and float and string methods
# Hop Wiz (1 - 100)
# scape character ---> list
# format character
# prime numbers (1 - 1000) ---> for and else
# anything else to use in place of (enumerate and zip)
# for loop to iterate backwards
# for loop to iterate between odd elements and even elements






































