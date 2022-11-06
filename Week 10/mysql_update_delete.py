import sys
import datetime
import mysql.connector
from mysql.connector import connection
from mysql.connector import errorcode


def create_database(cur, dbname):
    try:
        cur.execute('CREATE DATABASE {}'.format(dbname))
    except mysql.connector.Error as er:
        print('Could not create database successfully')
        print(er)
        sys.exit(-1)


DB_NAME = 'demodb'

config = {'user': 'sqluser',
          'password': 'P@ssw0rd',
          'host': '192.168.1.201',
          'raise_on_warnings': True}

try:
    cn = mysql.connector.connect(**config)
    cursor = cn.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print('database does not exist')
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('username and/or password is incorrect !')
    elif err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
        print('you do not have permission to access this DB / or DB name invalid')
    else:
        print(err)

try:
    cursor.execute('USE {}'.format(DB_NAME))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, DB_NAME)
        print('Created database {}'.format(DB_NAME))
    else:
        print('Unknown error occured')
        print(err)
        sys.exit(-1)
else:
    print('Database changed to {}'.format(DB_NAME))

update_query = 'UPDATE salaries ' \
               'SET salary=%s ' \
               'WHERE salaries.emp_no=(SELECT emp_no FROM employees WHERE first_name=%s)'

delete_query = 'DELETE s, e FROM ' \
               'salaries as s ' \
               'INNER JOIN employees as e ' \
               'ON s.emp_no=e.emp_no ' \
               'WHERE e.first_name=%s'

salary_range = [i * 3500000 for i in range(1, 11)]  # comprehension

update_data = (salary_range[5], 'Mehdi')

cursor.execute(update_query, update_data)
cursor.execute(delete_query, ('Elon',))


cn.commit()
cursor.close()
cn.close()




