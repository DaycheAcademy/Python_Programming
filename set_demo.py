# unordered data type
# mutable

# you 'CANNOT' define empty set using literals
emptySet = set()

sampleSet = {1, 'A', 'g', 3.86, 'Dayche', 'A', 'A'}
for _ in range(10):
    print(sampleSet)

print('+' * 40)

odd = set(range(1, 50, 2))  # members: 25
power = {1, 4, 9, 16, 25, 36, 49}  # members: 7

print(len(odd))
print(odd.intersection(power))
print(len(odd.union(power)))

print('=' * 40)
print(odd.intersection_update(power))
print(odd)

power_frozen = frozenset(power)










