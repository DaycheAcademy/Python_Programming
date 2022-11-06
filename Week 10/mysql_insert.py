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

employees_query = 'INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date) ' \
                  'VALUES(%s, %s, %s, %s, %s)'

salaries_query = "INSERT INTO salaries (emp_no, salary, from_date, to_date) " \
                 "VALUES(%s, %s, %s, %s)"

tomorrow = datetime.datetime.now().date() + datetime.timedelta(days=1)

data_employee = (datetime.date(1980, 6, 13),
                 'Elon',
                 'Musk',
                 'M',
                 tomorrow)

cursor.execute(employees_query, data_employee)
emp_no = cursor.lastrowid

data_salary = (emp_no,
               85000000,
               tomorrow,
               datetime.date(2022, 12, 30))

cursor.execute(salaries_query, data_salary)


cn.commit()
cursor.close()
cn.close()




