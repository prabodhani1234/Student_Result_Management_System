import sqlite3
def res_connect():
    return sqlite3.connect("result.db")
#connection = sqlite3.connect("result.db")
#connection.commit()
#with connection:
    #connection.execute("CREATE TABLE result_details(index_number TEXT ,marks1 TEXT,marks2 TEXT,marks3 TEXT,total TEXT,average TEXT)")
    #connection.commit()
#with connection:
    #x=connection.execute("SELECT * FROM result_details").fetchall()
    #print(x)

#with connection:
    #connection.execute("DELETE FROM result_details")
    #connection.commit()