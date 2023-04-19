import sqlite3
def sub_connect():
    return sqlite3.connect("subject.db")
#connection=sqlite3.connect("subject.db")
#connection.commit()
#with connection:
    #connection.execute("CREATE TABLE subject_details(subject_code TEXT ,subject_name TEXT)")
    #connection.commit()

#with connection:
    #connection.execute("DELETE FROM subject_details")
    #connection.commit()

#with connection:
    #x=connection.execute("SELECT * FROM subject_details ").fetchall()
    #for i in x:
        #print(i)




