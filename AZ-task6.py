import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'Kirill2019@'
)

mycursor = mydb.cursor()
mycursor.execute('USE PY_demodb')


mycursor.execute('DROP TABLE employees')
