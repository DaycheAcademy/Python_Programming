# Sequence
# Generator
import sys

smallRange = range(10)
# print(smallRange)

smallList = list(range(10))
# print(smallList)

bigRange = range(1000)
bigList = list(range(1000))

print('size of smallRange in memory: {}'.format(sys.getsizeof(smallRange)))
print('size of bigRange in memory: {}'.format(sys.getsizeof(bigRange)))
print('size of smallList in memory: {}'.format(sys.getsizeof(smallList)))
print('size of bigList in memory: {}'.format(sys.getsizeof(bigList)))

# ==================================

a = 98720532405760234650983250983264
print(a in range(0, 9999999999999999999999999999999999999999, 1401))


















