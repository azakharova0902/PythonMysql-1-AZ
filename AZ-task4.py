import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'Kirill2019@'
)


mycursor = mydb.cursor()
mycursor.execute('USE PY_demodb')


mycursor.execute('UPDATE employees SET first_name = "Hope", last_name = "Golberg", email ="hopeg@gmail.com" WHERE emp_id = 2')

mydb.commit()

print('********* RESULT ************')

mycursor.execute('SELECT * FROM employees')
for record in mycursor:
    print('Emp_ID: ', record[0])
    print('First name: ', record[1])
    print('Last name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('-----------------------------')