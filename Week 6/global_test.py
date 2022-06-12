
sampleVariable = 10
sampleList = [1, 2, 3]

print(globals())

for item in sorted(globals()):
    print(item)
print(globals().keys())


