
import shelve

sampleList = [1, 2, 3]
sampleTuple = 1, 2, 3
names = ['Mehdi', 'Ahmad', 'Ali']

with shelve.open('test') as sid:
    sid['list'] = sampleList
    sid['tuple'] = sampleTuple
    sid['names'] = names

with shelve.open('test') as sid:
    sid['test'] = 'test'

with shelve.open('test') as sid:
    sid['test'] = 'vatankhah'

with shelve.open('test') as sid:
    for k in sid:
        print(k, sid[k])


