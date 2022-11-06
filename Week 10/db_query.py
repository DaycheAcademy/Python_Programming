import datetime
import sqlite3


db = sqlite3.connect('employee.sqlite')
cursor = db.cursor()

for item in cursor.execute('SELECT * FROM salary'):
    print(item)

print('=' * 40)
salary_records = cursor.execute('SELECT * FROM salary')
print(salary_records)
print(type(salary_records))

for item in salary_records:
    print(item)

print('=' * 40)

for item in salary_records:
    print(item)
print('=' * 40)
salary_records = cursor.execute('SELECT * FROM salary')

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

print('=' * 40)
salary_records = cursor.execute('SELECT * FROM salary')
print(cursor.rowcount)
print(cursor.fetchall())

print('=' * 40)
cursor.execute('UPDATE salary SET amount=? WHERE id=?', (13000000, 1003))
print(cursor.rowcount)

print('=' * 40)
today = datetime.date.today()
cursor.execute('INSERT INTO salary VALUES(?, ?, ?)', (1004, 28000000, today))
print(cursor.lastrowid)






