# force a user to input an integer
# calculate mean of unknown number of integers (q or quit to stop entering data)

sumOfValues = 0
counter = 0
while True:
    inp = input("Enter an integer: ")
    if inp.lower() == 'q' or inp.lower() == 'quit':
        break
    if not inp.isdigit():
        continue
    else:
        sumOfValues += float(inp)
        counter += 1
if counter:
    meanValue = sumOfValues / counter
    print(f'The mean of numbers is equal to {meanValue:.2f}')
else:
    meanValue = None
print(meanValue)


