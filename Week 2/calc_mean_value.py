# force a user to input an integer
# calculate mean of unknown number of integers (q or quit to stop entering data)

counter = 0
sumOfValues = 0

while True:
    inp = input('Enter an Integer: ')
    # print(type(inp))

    if inp.lower() == 'q' or inp.lower() == 'quit':
        break
    if not inp.isdigit():
        continue
    else:
        sumOfValues = sumOfValues + int(inp)
        counter = counter + 1

if counter:
    meanValue = sumOfValues / counter
else:
    meanValue = None
print(meanValue)


# print(inp.isdigit())


