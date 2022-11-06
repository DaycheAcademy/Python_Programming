import sqlite3

db = sqlite3.connect('employee.sqlite')

people_query = db.execute('SELECT * FROM people')
id_name = db.execute('SELECT id, name FROM people')

salary_query = db.execute('SELECT * FROM salary')
print(people_query)

for item in people_query:
    print(item)


for item in id_name:
    print(item)

print('=' * 40)


for item in salary_query:
    print(item)





