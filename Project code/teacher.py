from tkinter import *

teacher_window = Tk()
teacher_window.title("Exam Result Management System")
teacher_window.configure(bg='#DFD6D6')
teacher_window.geometry("700x570")  # window size
teacher_window.maxsize(width=700, height=570)  # window maximize

# main text
text1 = Label(teacher_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
              fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

text2 = Label(teacher_window, text="INSERT STUDENT RESULT...", font=("Times New Roman", 17),
              fg="#E33737", bg="#DFD6D6")
text2.place(y=110, x=20)

label1 = Label(teacher_window, text="Index Number\t   :", font=("arial", 11), fg="#333333", bg='#DFD6D6', padx=10,
               pady=4)
label1.place(x=115, y=242)

entry1 = Entry(teacher_window, font=16)
entry1.place(x=280, y=242, width=280, height=30)

label2 = Label(teacher_window, text="Subject \t\t   :", font=("arial", 11), fg="#333333", bg='#DFD6D6', padx=10, pady=4)
label2.place(x=115, y=274)

subject_list = ['fuvu', 'yuguyg']
subject = StringVar()
subject.set('Select Subject')
drop_list = OptionMenu(teacher_window, subject, *subject_list)
drop_list.place(x=280,y=306,width=280, height=30)

entry2 = Entry(teacher_window, font=16)
entry2.place(x=280, y=335, width=280, height=30)


subject_list = ['fuvu', 'yuguyg']
subject = StringVar()
subject.set('Select Subject')
drop_list1 = OptionMenu(teacher_window, subject, *subject_list)
drop_list1.place(x=280,y=367,width=280, height=30)

entry3 = Entry(teacher_window, font=16)
entry3.place(x=280, y=396, width=280, height=30)

subject_list = ['fuvu', 'yuguyg']
subject = StringVar()
subject.set('Select Subject')
drop_list2 = OptionMenu(teacher_window, subject, *subject_list)
drop_list2.place(x=280,y=428,width=280, height=30)

entry4 = Entry(teacher_window, font=16)
entry4.place(x=280, y=457, width=280, height=30)

button2 = Button(teacher_window, text="SUBMIT", font=("arial", 11), bg="#5E96D2", padx=14, pady=1)
button2.place(x=467, y=495)

teacher_window.mainloop()
