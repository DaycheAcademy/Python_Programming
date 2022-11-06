# Flow Control
# ===================
# if, elif, else  ---> Conditionals
# for, else  ---> Loops
# while

# ---------------------

# if <condition>:
#     1 -
#     2 -
#     3 -


# linter
age = 18

# Chained Conditioning
if age > 18:  # bool(age > 18)
    print('be senne ghanooni residin, mitoonin ray bedin')
elif 15 < age <= 18:
    print('yekam dige moonde be senne ghanooni beresi')
elif 12 < age <= 15:
    print('hanooz zamane ziadi moonde !')
else:
    print('hanooz be senne ghanooni naresidi !')

# --------------------
if age > 18:  # bool(age > 18)
    print('be senne ghanooni residin, mitoonin ray bedin')
if 15 < age <= 18:
    print('yekam dige moonde be senne ghanooni beresi')
if 12 < age <= 15:
    print('hanooz zamane ziadi moonde !')
else:
    print('hanooz be senne ghanooni naresidi !')


# int: 0
# float: 0.0
# string: ''    ""    """"""
# list: []
# tuple: ()
# dictionary: {}
# set: set()
# False
if age:  # bool(age)
    print('we are inside condition block')

# if not age - 18:

# ternary operator:

vote = True if age > 18 else False
print(vote)

temp = 'some string'
myString = 'ABC' if temp else 'XYZ'
print(myString)

# ========================================







































