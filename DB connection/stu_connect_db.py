import sqlite3
def stu_connect():
   return sqlite3.connect("student.db")
#connection=sqlite3.connect("student.db")
#connection.commit()

#with connection:
   #connection.execute("CREATE TABEL student_details(registration_number TEXT, index_number TEXT, full_name TEXT, address TEXT, gender TEXT, email_address TEXT, phone_number TEXT, subject1 TEXT, subject2 TEXT, subject3 TEXT)")
   #connection.commit()

#with connection:
    #connection.execute("DELETE FROM student_details")
    #connection.commit()

#with connection:
   #x=connection.execute("SELECT * FROM student_details").fetchall()
   #for y in x:
     # print(y)

