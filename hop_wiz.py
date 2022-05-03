
# multiples of 3 --> Hop
# multiples of 7 --> Wiz
# multiples of 3 and 7 --> HopWiz

# MRV: Most Repeated Value
for num in range(1, 100):
    decision = 'HopWiz' if not num % 21 else 'Hop' if not num % 3 else 'Wiz' if not num % 7 else str(num)
    print(decision)





