# Mapping

emptyDict = {}
anotherEmptyDict = dict()

sampleDict = {'name': 'Mehdi',
              'surname': 'Shokri',
              'age': 18,
              'city': 'Tehran'}

print(sampleDict['name'])

print(hex(id(sampleDict)))
sampleDict['education'] = 'Diploma'
print(hex(id(sampleDict)))

# Accessing values can ONLY be through 'keys'

# view object
print(sampleDict.keys())
keyList = list(sampleDict.keys())
print(keyList)

print(sampleDict.values())
valueList = list(sampleDict.values())
print(valueList)

print(sampleDict.items())
itemTuple = tuple(sampleDict.items())
print(itemTuple)

newDict = dict(itemTuple)
print(newDict)

# insertion order
# memory order

# someDict = {[1, 2]: 3,
#             'a': 4}


print('=' * 40)
print(hash('name'))
print('=' * 40)
for k in sampleDict:  # O(N)
    print(sampleDict[k])

print('=' * 40)
for v in sampleDict.values():  # O(N^2)
    print(v)










