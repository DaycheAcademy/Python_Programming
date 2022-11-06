# demouser / sqluser
# demodb / dayche

import mysql.connector
from mysql.connector import connection
from mysql.connector import errorcode

# cn = mysql.connector.connect(user='sqluser',
#                              password='P@ssw0rd',
#                              host='192.168.1.201',
#                              database='demodb')

# cn = connection.MySQLConnection(user='sqluser',
#                                 password='P@ssw0rd',
#                                 host='192.168.1.201',
#                                 database='demodb')

config = {'user': 'demouser',
          'password': 'P@ssw0rd',
          'host': '192.168.1.201',
          'database': 'demodb',
          'raise_on_warnings': True}

try:
    cn = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print('database does not exist')
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('username and/or password is incorrect !')
    elif err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
        print('you do not have permission to access this DB / or DB name invalid')
    else:
        print(err)
else:
    cn.close()



