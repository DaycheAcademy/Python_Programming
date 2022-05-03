# Sequence:
# 1 - Ordered
# 2 - Index-able

import copy

emptyList = []  # literal
anotherEmptyList = list()  # constructor

# sampleList = [1, 3.6, 'A', 9]
sampleList = [1, 3.6, 4, 9, 2]

sampleList.append(4.907)
print(sampleList)

sampleString = 'ABCD'
alphabetList = list(sampleString)

print(alphabetList)

# sampleList.sort()

print('=' * 40)
print(hex(id(sampleList)))
print(sampleList.sort())
sampleList.append(20)
print(hex(id(sampleList)))
print(sampleList)


# all variables in python pointer
# list is a mutable object


print('=' * 40)
a = 5
print(hex(id(a)))
print('----------')
b = 5
print(hex(id(b)))

a = a + 1
print(a, b)
print(hex(id(a)))

# =============================
print('=' * 40)

odd = list(range(1, 20, 2))
# print(odd)

backUp = odd
odd.append(101)
print(backUp)

print(odd.index(11))
# =========================
print('=' * 40)
odd = list(range(1, 20, 2))
backUp = odd.copy()
odd.append(101)
print(backUp)
print(odd)
print(hex(id(backUp)))
print(hex(id(odd)))
# ---------
print('=' * 40)
odd = list(range(1, 20, 2))
backUp = list(odd)
odd.append(101)
print(backUp)
print(hex(id(backUp)))
print(hex(id(odd)))
# ----------
print('=' * 40)
odd = list(range(1, 26, 2))

backUp = copy.copy(odd)
odd.append(101)
print(backUp)
print(hex(id(backUp)))
print(hex(id(odd)))

# ----------
print('=' * 40)
odd = [1, 3, 11, 5, 91, 9, [7, 13]]

# shallow copy
backUp = odd.copy()
backUp2 = list(odd)
backUp3 = copy.copy(odd)

fullBackup = copy.deepcopy(odd)

odd[-1].append(15)
odd.append(101)
print('odd:', odd)
print('---------')
print('backUp:', backUp)
print('backUp2:', backUp2)
print('backUp3:', backUp3)
print('fullBackup:', fullBackup)

# ====================================
print('=' * 40)
odd = [1, 3, 11, 5, 91, 9, [7, 13]]

backUp = odd
odd = odd + [101]  # assignment
print(odd)
print('normal assignment:', backUp)

# -------------
print('=' * 40)
odd = [1, 3, 11, 5, 91, 9, [7, 13]]

backUp = odd
odd += [101]  # augmented assignment
print(odd)
print('augmented assignment:', backUp)


































































