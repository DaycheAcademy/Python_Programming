
# Sqlite
# self-contained

import sqlite3
import datetime


db = sqlite3.connect('employee.sqlite')

# create_query = 'CREATE TABLE IF NOT EXISTS people (' \
#                'id INTEGER PRIMARY KEY, ' \
#                'name TEXT NOT NULL, ' \
#                'phone TEXT, ' \
#                'department TEXT DEFAULT UNKNOWN)'


create_query = 'CREATE TABLE IF NOT EXISTS salary (' \
               'id INTEGER, ' \
               'amount INTEGER NOT NULL, ' \
               'date TIMESTAMP)'

db.execute(create_query)

# db.execute('INSERT INTO people (id, name, phone, department) '
#            'VALUES(1001, "Mehdi Shokri", "09121234567", "IT")')

# db.execute('INSERT INTO people VALUES(1002, "Ali Roozbeh", "09129876543", "SUPPORT")')

today = datetime.date.today()
# db.execute('INSERT INTO salary VALUES(1001, 15000000, "{}")'.format(today))
# db.execute('INSERT INTO salary VALUES(1002, 17500000, "{}")'.format(today))
# db.execute('INSERT INTO salary VALUES(1003, 18000000, "{}")'.format(today))

# db.execute('DELETE FROM salary WHERE id=1001')
# db.execute('DELETE FROM salary WHERE id=1003')
# db.execute('DELETE FROM salary WHERE id=1002')

db.execute('UPDATE salary SET amount=25000000 WHERE id=1002')


db.commit()
db.close()


# CRUD
# ------
# Create Table / Record (insert)
# Retrieve Data (select)
# Update Data (update)
# Delete Data (delete)
