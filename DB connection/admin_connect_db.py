import sqlite3
def admim_connect():
    return sqlite3.connect('admin.db')
#connection=sqlite3.connect('admin.db')
#connection.commit()
#with connection:
    #connection.execute("CREATE TABLE IF NOT EXISTS admin_details(id INTEGER PRIMARY KEY ,user_name TEXT, password TEXT)")
    #connection.commit()

#with connection:
    #connection.execute("DELETE FROM admin_details")
    #connection.commit()
