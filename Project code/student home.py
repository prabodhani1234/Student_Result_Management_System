from tkinter import*

student_window = Tk()
student_window.title("Exam Result Management System")
student_window.configure(bg='#DFD6D6')
student_window.geometry("700x470")  # window size
student_window.maxsize(width=700, height=470)  # window maximize


# main text
text1 = Label(student_window, text="STUDENT RESULT MANAGEMENT SYSTEM", font=("Times New Roman", 22, "bold"),
            fg="white", bg="#285C9F", width=700, height=3)
text1.pack()

text2=Label(student_window,text="WELCOME STUDENT...",font=("Times New Roman", 18),
            fg="#E33737", bg="#DFD6D6")
text2.place(y=110,x=10)

image1 = PhotoImage(file="C:/Users/user/Desktop/EXAM RESULT SYSTEM/IMAGES/student.png")
label1 = Label(student_window, image=image1)
label1.pack(padx=0,pady=60)

label2=Label(student_window,text="INDEX NUMBER :",font=("verdana", 11), fg="#333333", bg="#797979",padx=20,pady=8)
label2.place(x=180,y=260)

entry_1=Entry(student_window,font=11)
entry_1.place(x=350,y=260,width=200, height=37)

button1 = Button(student_window, text="Search", font=("arial", 11),bg="#5E96D2",padx=25,pady=1)
button1.place(x=440, y=320)

#lable1=Label
student_window.mainloop()