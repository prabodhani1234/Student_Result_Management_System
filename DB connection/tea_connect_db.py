import sqlite3
def connect ():
    return sqlite3.connect("teacher_data.db")
#connection = sqlite3.connect("teacher_data.db")
#connection.commit()
#with connection:
    #connection.execute("CREATE TABLE IF NOT EXISTS teacher_details(id INTEGER PRIMARY KEY ,user_name TEXT, password TEXT)")
    #connection.commit()

#with connection:
    #connection.execute("DELETE FROM main.teacher_details")
    #connection.commit()
