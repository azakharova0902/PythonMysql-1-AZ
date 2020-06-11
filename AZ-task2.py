import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'Kirill2019@'
)


mycursor = mydb.cursor()
mycursor.execute('USE PY_demodb')

my_query = 'INSERT INTO employees (first_name, last_name, email, job_title, date_hired, salary) VALUES (%s, %s, %s, %s, %s, %s)'
my_values = [
    ('Jennifer', 'Coleman', 'jcoleman@gmail.com', 'Assistant Manager', '2015-04-10', 48700),
    ('Kristopher', 'Bond', 'kb@gmail.com', 'HR Manager', '2019-02-09', 49000),
    ('Anna', 'Smith', 'as@yahoo.com', 'FSR', '2018-03-06', 41600),
    ('Katrina', 'Barclay', 'katrbar@gmail.com', 'IQ Rep', '2019-03-07', 43000)
]

mycursor.executemany(my_query, my_values)
mydb.commit()

mycursor.execute('SELECT * FROM employees')
for record in mycursor:  
    print('Emp_ID: ', record[0])
    print('First name: ', record[1])
    print('Last name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('-------------------------------------')