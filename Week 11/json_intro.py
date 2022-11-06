# JSON: Javascript Object Notation
# File Format

# Python Native
import json

data = {'name': 'Mehdi',
        'surname': 'Shokri Zadeh',
        'age': 20,
        'city': 'Tehran'}

with open('details.json', 'w') as j_file:
    json.dump(data, j_file)

json_values = json.dumps(data)
print(json_values)
print(type(json_values))








