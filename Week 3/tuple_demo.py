# Sequence

# immutable

import sys
import os

emptyTuple = ()
anotherEmptyTuple = tuple()

sampleTuple = 1, 2, 3
print(type(sampleTuple))

print(1, 2, 3)
print((1, 2, 3))

# sampleTuple[0] = 10
print(hex(id(sampleTuple)))

sampleTuple = sampleTuple[0], 10, sampleTuple[2]
print(sampleTuple)
print(hex(id(sampleTuple)))

print('=' * 40)

album = 'Homayoun shajarian', 2003, ('nasim-e-vasl', 'sokoot', 'havay-e-geryeh')

artist, year, tracks = album  # tuple unpacking

print(artist)
print(year)
print(tracks)

# ==============================

print('=' * 40)
oddList = list(range(1, 20, 2))
oddTuple = tuple(range(1, 20, 2))

print('size of oddList on memory: {} BYTES'.format(sys.getsizeof(oddList)))
print('size of oddTuple on memory: {} BYTES'.format(sys.getsizeof(oddTuple)))










































