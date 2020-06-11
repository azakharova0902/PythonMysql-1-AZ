import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'Kirill2019@'
)


mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE PY_demodb')

mycursor.execute('USE PY_demodb')

mycursor.execute('CREATE TABLE employees (emp_id INT primary key auto_increment, first_name VARCHAR(40) not null, last_name varchar(40) not null, email varchar(50) not null unique, job_title varchar(40) not null, date_hired date not null, salary float check (salary >= 15000 and salary <= 50000))')


mycursor.execute('SHOW TABLES')
for table in mycursor:
    print(table)