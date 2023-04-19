from tkinter import*
# from tkinter import Entry


class startpage():
    def __init__(self):
        main_window=Tk()
        main_window.title("Exam Result Management System")
        main_window.geometry("700x450")  # window size
        main_window.maxsize(width=700, height=450)  # window maximize

        # background image for system home page
        mainbg = PhotoImage(file="C:/Users/user/Desktop/EXAM RESULT SYSTEM/IMAGES/mainwindow.png")
        main_label = Label(main_window, image=mainbg)
        main_label.place(x=0, y=0)

        # main text
        text1 = Label(main_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
                      fg="white", bg="#285C9F", width=700, height=3)
        text1.pack()

        image1 = PhotoImage(file="C:/Users/Today/Desktop/exam result system/image12.png")
        label1 = Label(main_window, image=image1)
        label1.place(y=135, x=300)

        # Button
        button1 = Button(main_window, text="HOME", font=("arial", 16), padx=75, pady=1)
        button1.place(y=175, x=0)

        button1 = Button(main_window, text="STUDENT", font=("arial", 16), padx=58, pady=1)
        button1.place(y=230, x=0)

        button1 = Button(main_window, text="TEACHERS", font=("arial", 16), padx=50, pady=1)
        button1.place(y=285, x=0)

        button1 = Button(main_window, text="ADMINISTRATOR", font=("arial", 16), padx=22, pady=1)
        button1.place(y=340, x=0)

        main_window.mainloop()

class studentpage():
    def __init__(self):
        student_window = Tk()
        student_window.title("Exam Result Management System")
        student_window.configure(bg='red')
        student_window.geometry("700x450")  # window size
        student_window.maxsize(width=700, height=450)  # window maximize

        # main text
        text1 = Label(student_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
                      fg="white", bg="#285C9F", width=700, height=3)
        text1.pack()

        #lable1=Label
        student_window.mainloop()