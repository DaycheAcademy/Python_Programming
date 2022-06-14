def handle_order(order, dictionary):
    return str(order) + ': ' + str(dictionary[order])


a = list()

for val in range(10):
    a.append(val)

# a = list(range(10))

a = [val for val in range(10)]

# comprehension

# [conditional statement / loop / filter]
# ternary


menu = {'sabzijat': ['gharch', 'felfel dolmeh', 'reyhoon', 'zorrat', 'bademjoon', 'sosis'],
        'morgh va gharch': ['morgh', 'gharch', 'goje', 'reyhoon', 'sosis'],
        'pepperoni': ['pepperoni', 'jalapino', 'gharch', 'sosis'],
        'makhloot': ['sosis', 'kalbas', 'zorrat', 'gharch', 'felfel dolmeh'], }

sauces = ['ketchup', 'mayo', 'french']

ordered = 'yes'
out = [pizza for pizza in menu if 'zorrat' in menu[pizza]
       and 'sosis' in menu[pizza] and 'kalbas' not in menu[pizza]]

print(out)

print('=' * 40)

out = [pizza if ordered == 'yes' else None for pizza in menu if 'zorrat' in menu[pizza]
       and 'sosis' in menu[pizza] and 'kalbas' not in menu[pizza]]


out1 = [handle_order(pizza, menu) for pizza in menu if 'zorrat' in menu[pizza]
        and 'sosis' in menu[pizza] and 'kalbas' not in menu[pizza]]


out_nested = ({(pizza, sauce) for pizza in menu} for sauce in sauces)

print(out_nested)
for item in out_nested:
    print(item)








