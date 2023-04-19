##########################################################
# NAME          - H.M.T.P.HETATH                         #
# AR NUMBER     - AR/96753                               #
# AF NUMBER     - AF/18/14787                            #
# PROJECT TOPIC _ EXAM RESULT MANAGEMENT SYSTEM          #
##########################################################

from tkinter import *
import tea_connect_db
from tkinter import messagebox
import result_db
import sub_connect_db
import sqlite3
from tkinter import PhotoImage
import admin_connect_db
import stu_connect_db

main_window = Tk()
main_window.title("Exam Result Management System")
main_window.geometry("1366x768")  # window size
main_window.maxsize(width=1366, height=768)  # window maximize

# background image for system home page
mainbg = PhotoImage(file="image/mainwindow.png")
main_label = Label(main_window, image=mainbg)
main_label.place(x=0, y=0)

# main text
text1 = Label(main_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

# side image
image1 = PhotoImage(file="image/home.png")
label1 = Label(main_window, image=image1)
label1.place(x=525, y=160)



def admin_signup():
    def signup_database():
        conn = admin_connect_db.admim_connect() # connect Database
        cursor = conn.cursor()
        # insert into database user name and password for login admin dashboard
        cursor.execute("INSERT INTO admin_details VALUES (NULL,:user_name,:password)",
                       {
                           'user_name': entry_1.get(),
                           'password': entry_2.get()
                       })
        messagebox.showinfo("Successful Message", "Account Created") # getting Successful massage
        conn.commit()
        conn.close()


    signup_window = Toplevel()
    signup_window.title("Sing up")
    signup_window.configure(bg='#DFD6D6')
    signup_window.geometry("1366x768")  # window size
    signup_window.maxsize(width=1366, height=768)

    # main text
    text1 = Label(signup_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()


    text2 = Label(signup_window, text="ADMIN SIGN UP...", font=("Times New Roman", 20), fg="#E33737",
                  bg="#DFD6D6")
    text2.place(y=140, x=40)

    # set icon image
    image1 = PhotoImage(file="image/login.png")
    label1 = Label(signup_window, image=image1)
    label1.pack(padx=0, pady=38)


    label2 = Label(signup_window, text="SIGN UP", font=("arial", 16), bg='#DFD6D6')
    label2.place(x=640, y=250)

    # enter user name and password label
    username_label = Label(signup_window, text="User Name\t:", font=("arial", 11), fg="#333333", bg='#DFD6D6', padx=20,pady=8)
    username_label.place(x=515, y=290)
    password_label = Label(signup_window, text="Password\t:", font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=20, pady=8)
    password_label.place(x=515, y=330)


    # enter user name and password in sing up window
    entry_1 = Entry(signup_window, font=11)
    entry_1.place(x=680, y=290, width=250, height=37)
    entry_2 = Entry(signup_window, font=16)
    entry_2.place(x=680, y=330, width=250, height=37)

    # create button for user name and password insert into the database
    button1 = Button(signup_window, text="SING UP", font=("arial", 11), bg="#5E96D2", padx=18, pady=1,command=signup_database )
    button1.place(x=837, y=380)

    signup_window.mainloop()


def admin_loging_screen():
    def loging():
        connection = sqlite3.connect("admin.db") # connect admin database
        cursor = connection.cursor()
        select = ("SELECT * FROM admin_details WHERE user_name=? AND password=?") # get user name and password from admin database
        cursor.execute(select, (entry_1.get(), entry_2.get())) # checked user entered user name and password similar to enter user name and password
        result = cursor.fetchall() # get all user name and password
        if result:
            x = admin_screen()
        elif entry_1=='' and entry_2=='': # if entry box are empty get message
            messagebox.showinfo("error","Enter User Name and Password")
        else: # if user name or password is incorrect
            messagebox.showinfo("error","Invalid User name and Password")
        connection.commit() # commit change
        connection.close() # connection close


    main_window.destroy() # go to the login window main window is delete
    login_window = Tk()
    login_window.title("Login")
    login_window.configure(bg='#DFD6D6')
    login_window.geometry("1366x768")  # window size
    login_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(login_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(login_window, text="WELCOME...", font=("Times New Roman", 20),
                  fg="#E33737", bg="#DFD6D6")
    text2.place(y=140, x=40)

    # loging window icon
    image1 = PhotoImage(file="image/login.png")
    label1 = Label(login_window, image=image1)
    label1.pack(padx=0, pady=44)

    label2 = Label(login_window, text="ADMIN LOGIN", font=("arial", 16), bg='#DFD6D6')
    label2.place(x=617, y=250)


    username_label = Label(login_window, text="User Name\t:", font=("arial", 11), fg="#333333", bg='#DFD6D6', padx=20,pady=8)
    username_label.place(x=515, y=290)

    entry_1 = Entry(login_window, font=11) # enter user name
    entry_1.place(x=680, y=290, width=250, height=37)


    password_label = Label(login_window, text="Password\t:", font=("arial", 11), fg="#333333", bg='#DFD6D6', padx=20,pady=8)
    password_label.place(x=515, y=330)

    entry_2 = Entry(login_window, show="*", font=16) # enter password
    entry_2.place(x=680, y=330, width=250, height=37)

    # create loging button
    button1 = Button(login_window, text="LOGIN", font=("arial", 11), bg="#5E96D2", padx=18, pady=1, command=loging )
    button1.place(x=837, y=380)

    # create sing up button for go to sign up window
    button1 = Button(login_window, text=" SIGN UP", font=("arial", 11), bg="#5E96D2", padx=16, pady=1,command=admin_signup)
    button1.place(x=725, y=380)
    login_window.mainloop()

def add_new_student():
    def student_submit_info():
        conn = stu_connect_db.stu_connect()  # connect student database
        cur = conn.cursor()
        # insert entry data student database
        cur.execute(
            "INSERT INTO student_details VALUES (:registration_number,:index_number,:full_name,:address,:gender,:email_address,:phone_number,:subject1,:subject2,:subject3)",
            {
                'registration_number': reg_entry.get(),
                'index_number': index_entry.get(),
                'full_name': fn_entry.get(),
                'address': address_entry.get(),
                'gender': var.get(),
                'email_address': email_entry.get(),
                'phone_number': phone_entry.get(),
                'subject1': subject1.get(),
                'subject2': subject2.get(),
                'subject3': subject3.get()

            }
        )

        conn.commit()
        conn.close()

        # clean entry box
        reg_entry.delete(0, END)
        index_entry.delete(0, END)
        fn_entry.delete(0, END)
        address_entry.delete(0, END)
        email_entry.delete(0, END)
        phone_entry.delete(0, END)

    addstudent_window = Toplevel()
    addstudent_window.title("Register Student")
    addstudent_window.configure(bg='#DFD6D6')
    addstudent_window.geometry("1366x768")  # window size
    addstudent_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(addstudent_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(addstudent_window, text="ADD NEW STUDENT...", font=("Times New Roman", 20), fg="#E33737",
                  bg="#DFD6D6")
    text2.place(y=140, x=40)

    label1 = Label(addstudent_window, text="Registration Form", width=20, font=("bold", 22), bg="#DFD6D6")
    label1.pack(pady=85)

    # create entry data and it label
    label2 = Label(addstudent_window, text="Registration Number   :", font=("arial", 14), fg="#333333", bg='#DFD6D6',padx=15, pady=4)
    label2.place(x=150, y=290)
    reg_entry = Entry(addstudent_window, font=11)
    reg_entry.place(x=380, y=290, width=300, height=35)

    label3 = Label(addstudent_window, text="Index Number\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6',padx=15,pady=4)
    label3.place(x=150, y=330)
    index_entry = Entry(addstudent_window, font=11)
    index_entry.place(x=380, y=330, width=300, height=35)

    label4 = Label(addstudent_window, text="Full Name \t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6', padx=15,pady=4)
    label4.place(x=150, y=370)
    fn_entry = Entry(addstudent_window, font=11)
    fn_entry.place(x=380, y=370, width=300, height=35)

    label5 = Label(addstudent_window, text="Address\t\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6', padx=15,pady=4)
    label5.place(x=150, y=410)
    address_entry = Entry(addstudent_window, font=11)
    address_entry.place(x=380, y=410, width=300, height=35)

    label5 = Label(addstudent_window, text="Gender\t\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6', padx=15,pady=4)
    label5.place(x=150, y=450)

    # creat radiobutton
    var = IntVar() # create integer variable for radiobutton
    Radiobutton(addstudent_window, text="Male", padx=5, variable=var, value=1, font=('arial', 11), bg='#DFD6D6').place(
        x=380, y=450)
    Radiobutton(addstudent_window, text="Female", padx=20, variable=var, value=2, font=('arial', 11),bg="#DFD6D6").place(
        x=450, y=450)

    label6 = Label(addstudent_window, text="Email Address\t    :", font=("arial", 14), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
    label6.place(x=150, y=490)
    email_entry = Entry(addstudent_window, font=11)
    email_entry.place(x=380, y=490, width=300, height=35)

    label7 = Label(addstudent_window, text="Phone Number\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6',padx=10,pady=4)
    label7.place(x=150, y=530)
    phone_entry = Entry(addstudent_window, font=11)
    phone_entry.place(x=380, y=530, width=300, height=35)

    # getting subject from subject database
    def list_subject():
        sub_conn = sub_connect_db.sub_connect()
        sub_cursor = sub_conn.cursor()
        x = sub_cursor.execute("SELECT subject_name FROM subject_details")
        subjects = [] # create list
        for row in x.fetchall():
            for sub in (row): # all subject name one by one get
                subjects.append(sub) # subject name append subject list
        return subjects # return subject list

    subject_list = list_subject()  # created subject list function similar to subject list

    label7 = Label(addstudent_window, text="Select Subject\t :", font=("arial", 14), fg="#333333", bg='#DFD6D6',padx=10, pady=4)
    label7.place(x=720, y=290)

    # create drop down list
    subject1 = StringVar() # create variable
    subject1.set("Select Subject ")
    drop1 = OptionMenu(addstudent_window, subject1, *subject_list)
    drop1.place(x=980, y=290, width=280, height=35)

    label7 = Label(addstudent_window, text="Select Subject\t :", font=("arial", 14), fg="#333333", bg='#DFD6D6',padx=10, pady=4)
    label7.place(x=720, y=330)
    subject2 = StringVar()
    subject2.set("Select Subject")
    drop2 = OptionMenu(addstudent_window, subject2, *subject_list)
    drop2.place(x=980, y=330, width=280, height=35)

    label7 = Label(addstudent_window, text="Select Subject\t :", font=("arial", 14), fg="#333333", bg='#DFD6D6',padx=10, pady=4)
    label7.place(x=720, y=370)
    subject3 = StringVar()
    subject3.set("Select Subject")
    drop3 = OptionMenu(addstudent_window, subject3, *subject_list)
    drop3.place(x=980, y=370, width=280, height=35)

    # create back button for go to previous window and delete addstudent window
    button1 = Button(addstudent_window, text="BACK", font=("arial", 11), bg="#5E96D2", padx=18, pady=1,
                     command=addstudent_window.destroy)
    button1.place(x=715, y=590)

    # insert all student details student window
    button2 = Button(addstudent_window, text="SUBMIT", font=("arial", 11), bg="#5E96D2", padx=14, pady=1,
                     command=student_submit_info)
    button2.place(x=811, y=590)

    addstudent_window.mainloop()


def add_new_subject_window():
    def subject_submit_Info():

        sub_conn = sub_connect_db.sub_connect() # connect subject database
        sub_cursor = sub_conn.cursor()
        # insert subject details
        sub_cursor.execute("INSERT INTO  subject_details VALUES (:sub_code,:sub_name) ",
                    {
                        'sub_code':sub_code_entry1.get(),
                        'sub_name':sub_name_entry2.get()
                    }
                    )

        sub_conn.commit()
        sub_conn.close()

        # clean entry box
        sub_code_entry1.delete(0,END)
        sub_name_entry2.delete(0,END)

    addsubject_window = Tk()
    addsubject_window.title("Add New Subject")
    addsubject_window.configure(bg='#DFD6D6')
    addsubject_window.geometry("1366x768") # window size
    addsubject_window.maxsize(width=1366, height=5768)  # window maximize

    # main text
    text1 = Label(addsubject_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(addsubject_window, text="ADD NEW STUDENT...", font=("Times New Roman", 20), fg="#E33737",
                  bg="#DFD6D6")
    text2.place(y=140, x=40)

    # create subject details label and entry box
    label1 = Label(addsubject_window, text="Subject Code\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6',
                   padx=15, pady=4)
    label1.place(x=386, y=300)
    sub_code_entry1 = Entry(addsubject_window, font=11)
    sub_code_entry1.place(x=605, y=300, width=330, height=35)

    label2 = Label(addsubject_window, text="Subject Name \t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6',
                   padx=15, pady=4)
    label2.place(x=386, y=345)
    sub_name_entry2 = Entry(addsubject_window, font=11)
    sub_name_entry2.place(x=605, y=345, width=335, height=35)

    # create back button for go to previous window and delete addstudent window
    button1 = Button(addsubject_window, text="BACK", font=("arial", 11), bg="#5E96D2", padx=18, pady=1,command=addsubject_window.destroy)
    button1.place(x=715, y=390)

    # create submit button for submit subject details
    button2 = Button(addsubject_window, text="SUBMIT", font=("arial", 11), bg="#5E96D2", padx=14, pady=1,
                     command=subject_submit_Info)
    button2.place(x=811, y=390)

    addsubject_window.mainloop()


def view_student_details():
    stu_details_window = Tk()
    stu_details_window.title("Registered Student")
    stu_details_window.configure(bg='#DFD6D6')
    stu_details_window.geometry("1366x768") # window size
    stu_details_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(stu_details_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2=Label(stu_details_window,text="REGISTERED STUDENT...",font=("Times New Roman", 19),fg="#E33737", bg="#DFD6D6")
    text2.place(y=140,x=40)

    # create column label
    label1=Label(stu_details_window,text='REG-NUMBER',font=('arial',11),bg='#797979')
    label1.place(x=50,y=212,width=120,height=30)

    label2=Label(stu_details_window,text='INDEX NUMBER',font=('arial',11),bg='#797979')
    label2.place(x=172,y=212,width=120,height=30)

    label3=Label(stu_details_window,text='FULL NAME',font=('arial',11),bg='#797979')
    label3.place(x=295,y=212,width=300,height=30)

    label4=Label(stu_details_window,text='ADDRESS',font=('arial',11),bg='#797979')
    label4.place(x=598,y=212,width=220,height=30)

    label5=Label(stu_details_window,text='GENDER',font=('arial',11),bg='#797979')
    label5.place(x=821,y=212,width=130,height=30)

    label6=Label(stu_details_window,text='EMAIL ADDRESS',font=('arial',11),bg='#797979')
    label6.place(x=954,y=212,width=200,height=30)

    label7=Label(stu_details_window,text='PHONE NUMBER',font=('arial',11),bg='#797979')
    label7.place(x=1157,y=212,width=150,height=30)

    # getting student information from student database
    stu_conn = stu_connect_db.stu_connect() #connect student database
    stu_cursor = stu_conn.cursor()
    stu_cursor.execute("SELECT * FROM student_details") # select student details
    x = stu_cursor.fetchall()

    gap = 245 # fist row
    for row in x: # get student details one by one
        reg_number=Label(stu_details_window,text=row[0],font=('arial',11))
        reg_number.place(x=50,y=gap,width=120,height=30)

        index_number=Label(stu_details_window,text=row[1],font=('arial',11))
        index_number.place(x=172,y=gap,width=120,height=30)

        full_name=Label(stu_details_window,text=row[2],font=('arial',11))
        full_name.place(x=295,y=gap,width=300,height=30)

        address=Label(stu_details_window,text=row[3],font=('arial',11))
        address.place(x=598,y=gap,width=220,height=30)

        gender=Label(stu_details_window,text=row[4],font=('arial',11))
        gender.place(x=821,y=gap,width=130,height=30)

        email=Label(stu_details_window,text=row[5],font=('arial',11))
        email.place(x=954,y=gap,width=200,height=30)

        phone = Label(stu_details_window, text=row[6], font=('arial', 11))
        phone.place(x=1157,y=gap,width=150,height=30)

        gap+=33 # create next row

    # create back button for go to previous window and delete student details window
    button1 = Button(stu_details_window, text="BACK", font=("arial", 11),bg="#5E96D2",padx=18,pady=1,command=stu_details_window.destroy)
    button1.place(x=1260, y=650)

    stu_details_window.mainloop()

def view_subject_details():
    sub_details_window = Tk()
    sub_details_window.title("All Subject Details")
    sub_details_window.configure(bg='#DFD6D6')
    sub_details_window.geometry("1366x768") # window size
    sub_details_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(sub_details_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=80, height=3)
    text1.grid(row=0,column=0)

    text2=Label(sub_details_window,text="ALL SUBJECT DETAILS...",font=("Times New Roman", 20),
                fg="#E33737", bg="#DFD6D6")
    text2.place(y=140,x=40)

    # subject
    label1=Label(sub_details_window,text='SUBJECT CODE',font=('arial',11),bg='#797979')
    label1.place(x=456,y=212,width=200,height=30)

    label1=Label(sub_details_window,text='SUBJECT NAME',font=('arial',11),bg='#797979')
    label1.place(x=660,y=212,width=300,height=30)

    # getting subject details form subject database
    sub_conn = sub_connect_db.sub_connect()
    sub_cursor = sub_conn.cursor()
    sub_cursor.execute("SELECT * FROM subject_details") # select subject details
    x=sub_cursor.fetchall() # select all subject
    gap=245 # first row
    for row in x: # getting subject information one by one

        # create column label
        subject_code=Label(sub_details_window,text=row[0],font=('arial',11),height=5,width=20)
        subject_code.place(x=456,y=gap,width=200,height=30)

        subject_name=Label(sub_details_window,text=row[1],font=('arial',11),height=5,width=20)
        subject_name.place(x=660,y=gap,width=300,height=30)

        gap+= 33 # create next row

    # create back button for go to previous window and delete subject details window
    button1 = Button(sub_details_window, text="BACK", font=("arial", 11),bg="#5E96D2",padx=18,pady=1,command=sub_details_window.destroy)
    button1.place(x=1000, y=600)

    sub_details_window.mainloop()


def view_result():
    res_details_window = Tk()
    res_details_window.title("Student Result")
    res_details_window.configure(bg='#DFD6D6')
    res_details_window.geometry("1366x768")  # window size
    res_details_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(res_details_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(res_details_window, text="RESULT DETAILS...", font=("Times New Roman", 20),
                  fg="#E33737", bg="#DFD6D6")
    text2.place(y=140, x=40)

    # create column label
    label1 = Label(res_details_window, text='INDEX NUMBER', font=('arial', 11), bg='#797979')
    label1.place(x=30, y=212, width=120, height=30)

    label1 = Label(res_details_window, text='NAME ', font=('arial', 11), bg='#797979')
    label1.place(x=152, y=212, width=220, height=30)

    label1 = Label(res_details_window, text='SUBJECT  ', font=('arial', 11), bg='#797979')
    label1.place(x=374, y=212, width=120, height=30)

    label1 = Label(res_details_window, text='MARKS', font=('arial', 11), bg='#797979')
    label1.place(x=496, y=212, width=120, height=30)

    label1 = Label(res_details_window, text='SUBJECT', font=('arial', 11), bg='#797979')
    label1.place(x=618, y=212, width=120, height=30)

    label1 = Label(res_details_window, text='MARKS', font=('arial', 11), bg='#797979')
    label1.place(x=740, y=212, width=120, height=30)

    label1 = Label(res_details_window, text='SUBJECT', font=('arial', 11), bg='#797979')
    label1.place(x=862, y=212, width=120, height=30)

    label1 = Label(res_details_window, text='MARKS', font=('arial', 11), bg='#797979')
    label1.place(x=984, y=212, width=120, height=30)

    label1 = Label(res_details_window, text='TOTAL', font=('arial', 11), bg='#797979')
    label1.place(x=1106, y=212, width=120, height=30)

    label1 = Label(res_details_window, text='AVERAGE', font=('arial', 11), bg='#797979')
    label1.place(x=1228, y=212, width=120, height=30)

    res_conn = result_db.res_connect() # connect result databaqse
    res_cursor = res_conn.cursor()
    res_cursor.execute("SELECT * FROM result_details")
    x = res_cursor.fetchall() # getting all student result data from result database
    gap = 242
    for row in x: # one by one get data
        reg_number = Label(res_details_window, text=row[0], font=('arial', 11))
        reg_number.place(x=30, y=gap, width=120, height=30)

        marks1 = Label(res_details_window, text=row[1], font=('arial', 11))
        marks1.place(x=496, y=gap, width=120, height=30)

        marks2 = Label(res_details_window, text=row[2], font=('arial', 11))
        marks2.place(x=740, y=gap, width=120, height=30)

        marks3 = Label(res_details_window, text=row[3], font=('arial', 11))
        marks3.place(x=984, y=gap, width=120, height=30)

        total = Label(res_details_window, text=row[4], font=('arial', 11))
        total.place(x=1106, y=gap, width=120, height=30)

        total = Label(res_details_window, text=row[5], font=('arial', 11))
        total.place(x=1228, y=gap, width=120, height=30)

        gap += 33 # create next row

    student_conn = stu_connect_db.stu_connect() #connect student table
    student_cursor = student_conn.cursor()
    student_cursor.execute("SELECT name,subject1,subject2,subject3 FROM student_details")
    x = student_cursor.fetchall()
    gap = 242
    for row in x: # getting one by one student name,subject1,subject2,subject3
        name = Label(res_details_window, text=row[0], font=('arial', 11))
        name.place(x=152, y=gap, width=220, height=30)

        subject1 = Label(res_details_window, text=row[1], font=('arial', 11))
        subject1.place(x=374, y=gap, width=120, height=30)

        subject2 = Label(res_details_window, text=row[2], font=('arial', 11))
        subject2.place(x=618, y=gap, width=120, height=30)

        subject3 = Label(res_details_window, text=row[3], font=('arial', 11))
        subject3.place(x=862, y=gap, width=120, height=30)
        gap += 33

    button1 = Button(res_details_window, text="BACK", font=("arial", 11), bg="#5E96D2", padx=18, pady=1,
                     command=res_details_window.destroy)
    button1.place(x=1260, y=650)

    res_details_window.mainloop()

def admin_screen():

    admin_window = Toplevel()
    admin_window.title("Admin Dashboard")
    admin_window.configure(bg='#DFD6D6')
    admin_window.geometry("1366x768")  # window size
    admin_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(admin_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                    fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(admin_window, text="ADMIN DASHBOARD...", font=("Times New Roman", 20),
                    fg="#E33737", bg="#DFD6D6")
    text2.place(y=140, x=40)

    # set admin page image
    image1 = PhotoImage(file="image/admin image.png")
    label1 = Label(admin_window, image=image1)
    label1.place(y=164, x=525)

    # create button and window connect
    button1 = Button(admin_window, text="ADD NEW STUDENT", font=("arial", 16), padx=50, pady=4,command=add_new_student)
    button1.place(y=250, x=20)

    button2 = Button(admin_window, text="ADD NEW SUBJECT", font=("arial", 16), padx=50, pady=4,command=add_new_subject_window)
    button2.place(y=310, x=20)

    button3 = Button(admin_window, text="ALL SUBJECT DETAILS", font=("arial", 16), padx=36, pady=4,command=view_subject_details)
    button3.place(y=370, x=20)

    button4 = Button(admin_window, text="REGISTERED STUDENT ", font=("arial", 16), padx=29, pady=4,command=view_student_details)
    button4.place(y=430, x=20)

    button5 = Button(admin_window, text="ALL STUDENT RESULT ", font=("arial", 16), padx=35, pady=4,command=view_result)
    button5.place(y=490, x=20)

    admin_window.mainloop()


def teacher_signup():
    def signup_database():
        conn = tea_connect_db.connect() # connect teacher database
        cursor = conn.cursor()
        # insert teachers user name and password
        cursor.execute("INSERT INTO teacher_details VALUES (NULL,:user_name,:password)",
                       {
                           'user_name': entry_1.get(),
                           'password': entry_2.get()
                       })
        messagebox.showinfo("Successful Message", "Account Created") # insert user name and password for login
        conn.commit()
        conn.close()


    signup_window = Toplevel()
    signup_window.title("Teacher Sign Up")
    signup_window.configure(bg='#DFD6D6')
    signup_window.geometry("1366x768")  # window size
    signup_window.maxsize(width=1366, height=768)

    text1 = Label(signup_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(signup_window, text="SIGN UP...", font=("Times New Roman", 20), fg="#E33737",
                  bg="#DFD6D6")
    text2.place(y=140, x=40)

    # teacher sign up icon image
    image1 = PhotoImage(file="image/login.png")
    label1 = Label(signup_window, image=image1)
    label1.pack(padx=0, pady=38)

    label2 = Label(signup_window, text="SING UP", font=("arial", 16), bg='#DFD6D6')
    label2.place(x=645, y=250)

    # Create user name password label
    username_label = Label(signup_window, text="User Name\t:", font=("arial", 11), fg="#333333", bg='#DFD6D6', padx=20,pady=8)
    username_label.place(x=515, y=290)
    password_label = Label(signup_window, text="Password\t:", font=("arial", 11), fg="#333333", bg='#DFD6D6',padx=20, pady=8)
    password_label.place(x=515, y=330)

    # creat variable for accessing entries and labels
    name_text=StringVar()
    password_text=StringVar()

    # create entry box
    entry_1 = Entry(signup_window, font=11, textvariable=name_text)
    entry_1.place(x=680, y=290, width=250, height=37)
    entry_2 = Entry(signup_window, font=16, textvariable=password_text)
    entry_2.place(x=680, y=330, width=250, height=37)

    # create button for user name and password insert into the database
    button1 = Button(signup_window, text="SING UP", font=("arial", 11), bg="#5E96D2", padx=18, pady=1,command=signup_database)
    button1.place(x=837, y=380)

    signup_window.mainloop()


def teacher_loging_screen():
    def loging():
        connection = sqlite3.connect("teacher_data.db") # connect teacher database
        cursor = connection.cursor()
        select = ("SELECT * FROM teacher_details WHERE user_name=? AND password=?") # get username and password
        cursor.execute(select, (entry_1.get(), entry_2.get()))
        result = cursor.fetchall()
        if result:
            x = teacher() # set click after the loging button go to teacher window

        elif entry_1=='' and entry_2=='': # if entry box are empty get message
            messagebox.showinfo("error","Enter User Name and Password")
        else:
            messagebox.showinfo("error","Invalid User name and Password")

        connection.commit()
        connection.close()

    main_window.destroy()
    login_window = Tk()
    login_window.title("Teacher Login")
    login_window.configure(bg='#DFD6D6')
    login_window.geometry("1366x768")  # window size
    login_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(login_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(login_window, text="WELCOME TEACHER...", font=("Times New Roman", 20),
                  fg="#E33737", bg="#DFD6D6")
    text2.place(y=140, x=40)

    # teacher login window icon image
    image1 = PhotoImage(file="image/login.png")
    label1 = Label(login_window, image=image1)
    label1.pack(padx=0, pady=44)

    label2 = Label(login_window, text="TEACHER LOGIN", font=("arial", 16), bg='#DFD6D6')
    label2.place(x=605, y=250)

    # create user name, password label and entry box
    username_label = Label(login_window, text="User Name\t:", font=("arial", 11), fg="#333333", bg='#DFD6D6', padx=20,
                           pady=8)
    username_label.place(x=515, y=290)
    user_name = StringVar() # create variable for accessing entry
    entry_1 = Entry(login_window, font=11, textvariable=user_name)
    entry_1.place(x=680, y=290, width=250, height=37)


    password_label = Label(login_window, text="Password\t:", font=("arial", 11), fg="#333333", bg='#DFD6D6', padx=20,
                           pady=8)
    password_label.place(x=515, y=330)
    password = StringVar()
    entry_2 = Entry(login_window, show="*", font=16, textvariable=password)
    entry_2.place(x=680, y=330, width=250, height=37)

    # create button for login teacher window
    button1 = Button(login_window, text="LOGIN", font=("arial", 11), bg="#5E96D2", padx=18, pady=1, command=loging)
    button1.place(x=837, y=380)

    # create button for go to sing up window
    button1 = Button(login_window, text="SIGN UP", font=("arial", 11), bg="#5E96D2", padx=16, pady=1, command=teacher_signup)
    button1.place(x=725, y=380)

    login_window.mainloop()


def teacher():

    def result_submit_info():

        def result_submit_info():

            res_conn = result_db.res_connect()  # connect result db python code
            res_cur = res_conn.cursor()
            res_cur.execute("INSERT INTO result_details VALUES(:index_number,:subject1,:subject2,:subject3,:total,:average)",
                {
                    'index_number': index_entry.get(),
                    'subject1': s1_marks_entry.get(),
                    'subject2': s2_marks_entry.get(),
                    'subject3': s3_marks_entry.get(),
                    'total': total_get.get(),
                    'average': average_get.get()

                }
                )

            res_conn.commit()
            res_conn.close()

            # clean entry box
            index_entry.delete(0, END)
            s1_marks_entry.delete(0, END)
            s2_marks_entry.delete(0, END)
            s3_marks_entry.delete(0, END)
            total_get.delete(0, END)
            average_get.delete(0, END)

        def add_clculation(): # calculation in system
            sub1 = int(marks1.get())
            sub2 = int(marks2.get())
            sub3 = int(marks3.get())
            tot = sub1 + sub2 + sub3  # getting total marks
            avg = tot / 3  # getting average
            total.set(tot)
            average.set('%.2f' % (avg)) # get average and set floating point number two decimal

        def creat_reset():
            marks1.set(" ")
            marks2.set(" ")
            marks3.set(" ")
            total.set(" ")
            average.set(" ")
            index.set(" ")

        teacher_window = Toplevel()
        teacher_window.title("Teacher Home Page")
        teacher_window.configure(bg='#DFD6D6')
        teacher_window.geometry("1366x768")  # window size
        teacher_window.maxsize(width=1366, height=768)  # window maximize

        # main text
        text1 = Label(teacher_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                      fg="white", bg="#285C9F", width=700, height=3)
        text1.pack()
        text2 = Label(teacher_window, text="INSERT STUDENT RESULT...", font=("Times New Roman", 20), fg="#E33737",
                      bg="#DFD6D6")
        text2.place(y=140, x=40)

        def list_subject():
            sub_conn = stu_connect_db.stu_connect() # connect student database
            sub_cursor = sub_conn.cursor()
            x = sub_cursor.execute("SELECT * FROM student_details") # select student all data in database
            for row in x.fetchall():
                if row[1] == index_entry.get(): # checked student index number similar to entry index number
                    # create subject set label
                    s1_label = Label(teacher_window, text=row[7], font=("arial", 12, 'bold'), fg="#333333",
                                     bg='#FFFFFF')
                    s1_label.place(x=641, y=272, width=280, height=35)
                    s2_label = Label(teacher_window, text=row[8], font=("arial", 12, 'bold'), fg="#333333",
                                     bg='#FFFFFF')
                    s2_label.place(x=641, y=344, width=280, height=35)
                    s3_label = Label(teacher_window, text=row[9], font=("arial", 12, 'bold'), fg="#333333",
                                     bg='#FFFFFF')
                    s3_label.place(x=641, y=416, width=280, height=35)

            sub_conn.commit()
            sub_conn.close()

        label1 = Label(teacher_window, text="Index Number\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6',
                       padx=10, pady=4)
        label1.place(x=420, y=200)
        index = StringVar()
        index_entry = Entry(teacher_window, font=16, textvariable=index)
        index_entry.place(x=641, y=200, width=280, height=35)

        label2 = Label(teacher_window, text="Subject \t\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6', padx=10,
                       pady=4)
        label2.place(x=420, y=236)

        # create variable for accessing entry
        marks1 = StringVar()
        marks2 = StringVar()
        marks3 = StringVar()
        total = StringVar()
        average = StringVar()

        # create entry box
        s1_marks_entry = Entry(teacher_window, font=11, textvariable=marks1)
        s1_marks_entry.place(x=641, y=308, width=280, height=35)
        s2_marks_entry = Entry(teacher_window, font=11, textvariable=marks2)
        s2_marks_entry.place(x=641, y=380, width=280, height=35)
        s3_marks_entry = Entry(teacher_window, font=11, textvariable=marks3)
        s3_marks_entry.place(x=641, y=452, width=280, height=35)

        # Create all calculation label and entry
        label1 = Label(teacher_window, text="Total\t\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6', padx=10,pady=4)
        label1.place(x=420, y=488)
        total_get = Entry(teacher_window, font=('arial', 11, 'bold'), textvariable=total)
        total_get.place(x=641, y=488, width=280, height=35)

        label1 = Label(teacher_window, text="Average\t\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6', padx=10,pady=4)
        label1.place(x=420, y=524)
        average_get = Entry(teacher_window, font=('arial', 11, 'bold'), textvariable=average)
        average_get.place(x=641, y=524, width=280, height=35)

        # create button for view subject
        button0 = Button(teacher_window, text="VIEW SUBJECT", font=("arial", 12), command=list_subject)
        button0.place(x=641, y=236, width=280, height=35)

        # Create button for reset entry box
        button1 = Button(teacher_window, text="RESET", font=("arial", 11), bg="#5E96D2", padx=14, pady=1,
                         command=creat_reset)
        button1.place(x=616, y=580)

        # create button for getting result
        button2 = Button(teacher_window, text="RESULT", font=("arial", 11), bg="#5E96D2", padx=14, pady=1,
                         command=add_clculation)
        button2.place(x=720, y=580)

        # create button for submit result data in to the result database
        button3 = Button(teacher_window, text="SUBMIT", font=("arial", 11), bg="#5E96D2", padx=14, pady=1,
                         command=result_submit_info)
        button3.place(x=829, y=580)
        teacher_window.mainloop()

    result_submit_info()

def result_sheet():
    def print_massage():
        messagebox.showinfo('Successful Massage', 'Print Successful')

    result_window = Toplevel()
    result_window.title("Exam Result Management System")
    result_window.configure(bg='#DFD6D6')
    result_window.geometry("1366x768")  # window size
    result_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(result_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                    fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(result_window, text="RESULT", font=("Times New Roman", 21, 'bold'),
                    fg="#E33737", bg="#DFD6D6")
    text2.pack()

    # create student information label
    label1 = Label(result_window, text="Registration Number\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6',
                    padx=10, pady=4)
    label1.place(x=480, y=190)
    label3 = Label(result_window, text="Index Number\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6',
                    padx=10, pady=4)
    label3.place(x=480, y=222)
    label5 = Label(result_window, text="Name\t\t   :", font=("arial", 14), fg="#333333", bg='#DFD6D6', padx=10,
                    pady=4)
    label5.place(x=480, y=254)

    student_conn = stu_connect_db.stu_connect() # connect student database
    student_cur = student_conn.cursor()
    student_cur.execute("SELECT registration_number,index_number,name,subject1,subject2,subject3 FROM student_details")
    x = student_cur.fetchall()
    for row in x: # one by one getting student data
        if index.get()==row[1]: # if entry index number similar to student table index number
            # create label
            label2 = Label(result_window, text=row[0], font=("arial", 11), fg="#333333")
            label2.place(x=700, y=190, width=300, height=30)

            label4 = Label(result_window, text=row[1], font=("arial", 11), fg="#333333")
            label4.place(x=700, y=222, width=300, height=30)

            label5 = Label(result_window, text=row[2], font=("arial", 11), fg="#333333")
            label5.place(x=700, y=254, width=300, height=30)

            label6 = Label(result_window, text=row[3], font=("arial", 11), bg='#FFFFFF')
            label6.place(x=597, y=383, width=200, height=30)

            label7 = Label(result_window, text=row[4], font=("arial", 11), bg='#FFFFFF')
            label7.place(x=597, y=416, width=200, height=30)

            label8 = Label(result_window, text=row[5], font=("arial", 11), bg='#FFFFFF')
            label8.place(x=597, y=449, width=200, height=30)

    # create column label
    label9 = Label(result_window, text="SUBJECT", font=11, bg='#797979')
    label9.place(x=597, y=350, width=200, height=30)

    label10 = Label(result_window, text="MARKS ", font=11, bg='#797979')
    label10.place(x=800, y=350, width=100, height=30)

    label11 = Label(result_window, text='TOTAL', font=10, bg='#FFFFFF')
    label11.place(x=597, y=500, width=200, height=30)

    label12 = Label(result_window, text='AVERAGE', font=10, bg='#FFFFFF')
    label12.place(x=597, y=533, width=200, height=30)

    res_sheet_conn = result_db.res_connect() # connect result database
    res_sheet_cur = res_sheet_conn.cursor()
    res_sheet_cur.execute("SELECT * FROM result_details") # get all student result
    x = res_sheet_cur.fetchall()
    for row in x:
        if index.get()==row[0]: # if entry index number similar to result table index number

            label13 = Label(result_window, text=row[1], font=("arial", 11), bg='#FFFFFF')
            label13.place(x=800, y=383, width=100, height=30)

            label14 = Label(result_window, text=row[2], font=("arial", 11), bg='#FFFFFF')
            label14.place(x=800, y=416, width=100, height=30)

            label15 = Label(result_window, text=row[3], font=("arial", 11), bg='#FFFFFF')
            label15.place(x=800, y=449, width=100, height=30)

            label16 = Label(result_window, text=row[4], font=("arial", 11), bg='#FFFFFF')
            label16.place(x=800, y=500, width=100, height=30)

            label17 = Label(result_window, text=row[5], font=("arial", 11), bg='#FFFFFF')
            label17.place(x=800, y=533, width=100, height=30)

    # print result sheet
    button1 = Button(result_window, text="Print", font=("arial", 11), bg="#5E96D2", command=print_massage, padx=15,
                        pady=1)
    button1.place(x=930, y=600)
    result_window.mainloop()



def student_home():
    global index
    #main_window.destroy()
    student_window = Toplevel()
    student_window.title("Student Home ")
    student_window.configure(bg='#DFD6D6')
    student_window.geometry("1366x768")  # window size
    student_window.maxsize(width=1366, height=768)  # window maximize

    # main text
    text1 = Label(student_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    text2 = Label(student_window, text="WELCOME STUDENT...", font=("Times New Roman", 20),
                  fg="#E33737", bg="#DFD6D6")
    text2.place(x=40, y=140)

    # set student image
    image1 = PhotoImage(file="image/student.png")
    label1 = Label(student_window, image=image1)
    label1.pack(padx=0, pady=60)

    label2 = Label(student_window, text="INDEX NUMBER :", font=("verdana", 14), fg="#333333", bg="#797979", padx=20,
                   pady=8)
    label2.place(x=470, y=360)
    index=StringVar()
    entry_1 = Entry(student_window, font=11,textvariable=index)
    entry_1.place(x=682, y=360, width=250, height=43)

    # create button for search result
    button1 = Button(student_window, text="Search", font=("arial", 11), bg="#5E96D2", padx=25, pady=1,command=result_sheet)
    button1.place(x=824, y=420)

    button2=Button(student_window,text="Back",font=("arial", 11), bg="#5E96D2", padx=25, pady=1)
    button2.place(x=725,y=420)

    student_window.mainloop()

def home():
    home_window = Toplevel()
    home_window.title("Wellcome Home")
    home_window.configure(bg='#DFD6D6')
    home_window.geometry("1366x768")  # window size
    home_window.maxsize(width=1366,height=768) # window maximize

    homebg = PhotoImage(file="image/home_window.png")
    home_label = Label(home_window, image=homebg)
    home_label.place(x=0, y=115)


    # main text
    text1 = Label(home_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 24, "bold"),
                  fg="white", bg="#285C9F", width=700, height=3)
    text1.pack()

    introduction=Label(home_window,
                       text="Best Wishers For Your Future.\n We Think You Got High Marks For The Exam.\n "
                            "In The Even Of Reaching Your Goal You Have To Take The Rough With Smooth.\n "
                            "Some Day Some How Your Dream Will Come Ture.\nYou can Work Hard For It.",
                       font=("Lucida Calligraphy",20),bg='#DFD6D6'

                       )
    introduction.place(x=100,y=450)

    home_window.mainloop()

# create all home window button
button1 = Button(main_window, text="HOME", font=("arial", 16), padx=150, pady=4,command=home)
button1.place(y=220, x=0)

button1 = Button(main_window, text="STUDENT", font=("arial", 16), padx=132, pady=4, command=student_home)
button1.place(y=290, x=0)

button1 = Button(main_window, text="TEACHERS", font=("arial", 16), padx=125, pady=4, command=teacher_loging_screen)
button1.place(y=360, x=0)

button1 = Button(main_window, text="ADMINISTRATOR", font=("arial", 16), padx=97, pady=4,
                     command=admin_loging_screen)
button1.place(y=430, x=0)

main_window.mainloop()

