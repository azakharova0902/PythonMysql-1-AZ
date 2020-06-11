import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'Kirill2019@'
)


mycursor = mydb.cursor()
mycursor.execute('USE PY_demodb')


#  ORDER BY

mycursor.execute('SELECT * FROM employees ORDER BY salary DESC')

res = mycursor.fetchall()

print('********* RESULT for ORDER BY ************')

for record in res:
    print('Emp_ID: ', record[0])
    print('First name: ', record[1])
    print('Last name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('-----------------------------')

# WHERE clause example

mycursor.execute('SELECT * FROM employees WHERE emp_id <= 3')

res1 = mycursor.fetchall()

print('********* RESULT # 1 ************')

for record in res1:
    print('Emp_ID: ', record[0])
    print('First name: ', record[1])
    print('Last name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('-----------------------------')



# LIKE with wildcards example

res2 = mycursor.execute('SELECT * FROM employees WHERE job_title LIKE "%sr"')

res2 = mycursor.fetchall()

print('********* RESULT # 2 ************')

for record in res2:
    print('Emp_ID: ', record[0])
    print('First name: ', record[1])
    print('Last name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('-----------------------------')


# OR example

mycursor.execute('SELECT * FROM employees WHERE last_name LIKE "%d" OR first_name LIKE "%r"' )

res3 = mycursor.fetchall()

print('********* RESULT # 3 ************')

for record in res3:
    print('Emp_ID: ', record[0])
    print('First name: ', record[1])
    print('Last name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('-----------------------------')


# AND example

mycursor.execute('SELECT * FROM employees WHERE last_name LIKE "%y" AND emp_id=4' )

res4 = mycursor.fetchall()

print('********* RESULT # 4 ************')

for record in res4:
    print('Emp_ID: ', record[0])
    print('First name: ', record[1])
    print('Last name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('-----------------------------')
